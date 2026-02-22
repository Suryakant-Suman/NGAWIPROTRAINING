import pytest
import os
from datetime import datetime
from utilities.driver_factory import get_driver
from utilities.config_reader import get_url


# ---------------------------
# DRIVER FIXTURE
# ---------------------------
@pytest.fixture
def driver():
    driver = get_driver()
    driver.get(get_url())
    yield driver
    driver.quit()


# ---------------------------
# ATTACH SCREENSHOT TO HTML REPORT
# ---------------------------
@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):

    outcome = yield
    rep = outcome.get_result()

    # We only act after test execution
    if rep.when == "call":

        # Access pytest-html plugin
        pytest_html = item.config.pluginmanager.getplugin("html")

        if rep.failed:
            driver = item.funcargs.get("driver", None)

            if driver:
                screenshot_dir = "reports/screenshots"
                os.makedirs(screenshot_dir, exist_ok=True)

                timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
                file_name = f"{item.name}_{timestamp}.png"
                file_path = os.path.join(screenshot_dir, file_name)

                driver.save_screenshot(file_path)

                # Attach screenshot to HTML report
                extra = getattr(rep, "extra", [])
                extra.append(pytest_html.extras.image(file_path))
                rep.extra = extra