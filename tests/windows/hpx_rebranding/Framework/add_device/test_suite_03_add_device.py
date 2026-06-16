import pytest
from MobileApps.libs.flows.windows.hpx_rebranding.flow_container import FlowContainer

pytest.app_info = "MOBILE"
pytest.set_info = "HPX"

@pytest.mark.usefixtures("class_setup_fixture_ota_regression", "function_setup_myhp_launch")
class Test_Suite_03_Add_Device(object):
    @pytest.fixture(scope="class", autouse=True)
    def class_setup(cls, request, windows_test_setup):
        cls = cls.__class__
        request.cls.driver = windows_test_setup
        request.cls.fc = FlowContainer(request.cls.driver)
        request.cls.fc.kill_hpx_process()
        request.cls.fc.kill_chrome_process()
        cls.profile= request.cls.fc.fd["profile"]
        cls.devices_details_pc_mfe = request.cls.fc.fd["devices_details_pc_mfe"]
        cls.devicesMFE = request.cls.fc.fd["devicesMFE"]
        cls.add_device= request.cls.fc.fd["add_device"]

    @pytest.mark.regression
    def test_101_verify_add_device_button_clickable_and_opens_sidebar_page_C55687256(self):
        assert self.devices_details_pc_mfe.verify_pc_device_name_show_up(), "PC name on homepage not loaded/visible"
        assert self.profile.verify_add_device_button(), "add device button is not found"
        self.profile.click_add_device_button()
        assert self.add_device.verify_add_device_page(), "add device page is not found"
