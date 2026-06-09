# PRE-FLIGHT FUNCTION INVENTORY LOG

**Inventory for test_suite_01_bell_notifications.py:** Found 6 total functions/methods:
1. class_setup (fixture)
2. test_01_verify_global_header_navigation_C60336078
3. test_02_verify_global_header_navigation_includes_bellicon_C53303694
4. test_03_verify_bellicon_can_be_clicked_C53303695
5. test_04_verify_notifications_sidepanel_opened_upon_clicking_bellicon_C53303696
6. test_05_verify_empty_bell_state_when_user_not_logged_in_C53303697

---

# EXHAUSTIVE DOCUMENTATION REPORT

## test_suite_01_bell_notifications.py

### MODULE SUMMARY DETAILS

[MODULE_PURPOSE_START]

This test module implements automated regression test cases for the Bell Notifications feature within the HPX Desktop application's global header navigation system. It validates the visibility, interactivity, and state management of the bell icon notification component across authenticated and unauthenticated user states, ensuring proper UI element rendering and side panel behavior through pytest-driven Windows automation testing.

[MODULE_PURPOSE_END]

### 1. File Header (Module-Level Documentation)

- **Primary Responsibility:** Executes automated UI regression tests for the bell notification icon feature in the HPX Desktop application, verifying global header navigation elements, bell icon clickability, notification side panel rendering, and empty state behavior for non-authenticated users.

- **Dependencies:** 
  - `pytest` - Testing framework for test execution, fixtures, and markers
  - `logging` - Standard Python logging module (imported but not actively used in visible code)
  - `MobileApps.libs.flows.windows.hpx_rebranding.flow_container.FlowContainer` - Custom flow container class managing test driver initialization and page object access

- **Module Configuration:** 
  - `pytest.app_info = "DESKTOP"` - Global configuration identifying the target application platform as Desktop
  - `pytest.set_info = "HPX"` - Global configuration specifying the HPX application context

---

### 2. Class Documentation: Test_Suite_01_Bell_Notifications

- **Role:** Serves as the primary test class container encapsulating all bell notification feature test cases, managing shared test fixtures and page object instances across the test suite lifecycle.

- **Purpose:** Organizes regression test methods validating bell icon functionality, coordinates class-level setup through pytest fixtures, and maintains shared state for driver instances and page object references used across multiple test scenarios.

---

#### Fixture: class_setup

- **Scope:** Class

- **Purpose:** Initializes and configures the test environment at the class level before any test methods execute, establishing the Windows test driver, instantiating the FlowContainer, terminating conflicting processes, and loading page object references for use across all test methods in the class.

- **Annotation or Markers:** 
  - `@pytest.fixture(scope="class", autouse=True)` - Declares this as a class-scoped fixture that executes automatically before test methods run

- **Dependencies:** 
  - `request` - Pytest request object providing access to the test class context
  - `windows_test_setup` - External fixture providing the Windows automation driver instance
  - `FlowContainer` - Custom framework class managing driver lifecycle and page object dictionary access

- **Parameter:** 
  - `cls` - Reference to the test class instance being configured
  - `request` - Pytest fixture providing metadata and context about the requesting test class
  - `windows_test_setup` - Injected fixture supplying the initialized Windows application driver

- **Set-up Action:** 
  1. Assigns the class reference using `cls = cls.__class__`
  2. Attaches the Windows test driver to the class via `request.cls.driver = windows_test_setup`
  3. Instantiates FlowContainer with the driver: `request.cls.fc = FlowContainer(request.cls.driver)`
  4. Terminates any running HPX application processes: `request.cls.fc.kill_hpx_process()`
  5. Terminates any running Chrome browser processes: `request.cls.fc.kill_chrome_process()`
  6. Extracts and assigns the profile page object: `cls.profile = request.cls.fc.fd["profile"]`
  7. Extracts and assigns the devicesMFE page object: `cls.devicesMFE = request.cls.fc.fd["devicesMFE"]`
  8. Extracts and assigns the device_card page object: `cls.device_card = request.cls.fc.fd["device_card"]`
  9. Extracts and assigns the bell_icon page object: `cls.bell_icon = request.cls.fc.fd["bell_icon"]`

- **State Management:** 
  - `cls.driver` - Stores the Windows automation driver instance for application interaction
  - `cls.fc` - Maintains the FlowContainer instance managing test flow orchestration
  - `cls.profile` - Page object reference for profile-related UI interactions
  - `cls.devicesMFE` - Page object reference for devices micro-frontend UI elements
  - `cls.device_card` - Page object reference for device card UI components
  - `cls.bell_icon` - Page object reference for bell notification icon interactions

---

#### Method Level: test_01_verify_global_header_navigation_C60336078

- **Scope:** Instance Method

- **Purpose:** Validates the presence and visibility of all critical global header navigation elements including the profile icon, sign-in button, and bell notification icon in their default rendered state.

- **Annotation or Markers:** 
  - `@pytest.mark.regression` - Tags this test as part of the regression test suite

- **Dependencies:** 
  - `self.devicesMFE` - Page object providing verification methods for global header UI elements

- **Module Configurations:** Inherits class-level fixtures `class_setup_fixture_ota_regression` and `function_setup_myhp_launch` applied via the class decorator.

- **Input Parameters:** 
  - `self` - Instance reference to the test class providing access to initialized page objects and driver

- **Return Parameter:** None (pytest test methods return implicitly; assertions determine pass/fail status)

- **Functional Flow:** 
  1. Invokes `self.devicesMFE.verify_profile_icon_show_up()` to check profile icon visibility
  2. Asserts the profile icon is visible; raises AssertionError with message "profile icon invisible" if verification fails
  3. Invokes `self.devicesMFE.verify_sign_in_button_show_up()` to check sign-in button visibility
  4. Asserts the sign-in button is visible; raises AssertionError with message "sign-in button invisible" if verification fails
  5. Invokes `self.devicesMFE.verify_bell_icon_show_up()` to check bell icon visibility
  6. Asserts the bell icon is visible; raises AssertionError with message "bell icon invisible" if verification fails

- **Assertions:** 
  - Profile icon must be visible in the global header navigation
  - Sign-in button must be visible in the global header navigation
  - Bell notification icon must be visible in the global header navigation

- **Boundary Conditions:** Assumes the application has launched successfully and the global header is rendered in the default state without user authentication.

- **Exception Handling:** No explicit try-except blocks; pytest captures AssertionError exceptions with custom failure messages for test reporting.

---

#### Method Level: test_02_verify_global_header_navigation_includes_bellicon_C53303694

- **Scope:** Instance Method

- **Purpose:** Verifies that the bell notification icon remains consistently visible across navigation contexts, specifically validating its persistence when navigating from a device detail view back to the main devices view.

- **Annotation or Markers:** 
  - `@pytest.mark.regression` - Tags this test as part of the regression test suite

- **Dependencies:** 
  - `self.devicesMFE` - Page object for global header element verification
  - `self.device_card` - Page object for device navigation and back button interactions

- **Module Configurations:** Inherits class-level fixtures `class_setup_fixture_ota_regression` and `function_setup_myhp_launch` applied via the class decorator.

- **Input Parameters:** 
  - `self` - Instance reference to the test class providing access to initialized page objects

- **Return Parameter:** None (pytest test methods return implicitly; assertions determine pass/fail status)

- **Functional Flow:** 
  1. Verifies profile icon visibility using `self.devicesMFE.verify_profile_icon_show_up()`
  2. Asserts profile icon is visible with failure message "profile icon invisible"
  3. Verifies sign-in button visibility using `self.devicesMFE.verify_sign_in_button_show_up()`
  4. Asserts sign-in button is visible with failure message "sign-in button invisible"
  5. Verifies bell icon visibility using `self.devicesMFE.verify_bell_icon_show_up()`
  6. Asserts bell icon is visible with failure message "bell icon invisible"
  7. Verifies PC devices back button visibility using `self.device_card.verify_pc_devices_back_button()`
  8. Asserts back button is visible with failure message "device back button invisible"
  9. Executes back navigation action using `self.device_card.click_pc_devices_back_button()`
  10. Re-verifies bell icon visibility after navigation using `self.devicesMFE.verify_bell_icon_show_up()`
  11. Asserts bell icon remains visible post-navigation with failure message "bell icon invisible"

- **Assertions:** 
  - Profile icon must be visible in initial state
  - Sign-in button must be visible in initial state
  - Bell icon must be visible in initial state
  - PC devices back button must be visible indicating device detail view context
  - Bell icon must remain visible after navigating back to main devices view

- **Boundary Conditions:** Requires the application to be in a device detail view state where the back button is available; validates UI element persistence across view transitions.

- **Exception Handling:** No explicit try-except blocks; pytest captures AssertionError exceptions with custom failure messages for test reporting.

---

#### Method Level: test_03_verify_bellicon_can_be_clicked_C53303695

- **Scope:** Instance Method

- **Purpose:** Validates the interactive functionality of the bell notification icon by verifying it can be clicked and successfully triggers the opening of the notification side panel, confirmed by the appearance of the avatar close button.

- **Annotation or Markers:** 
  - `@pytest.mark.regression` - Tags this test as part of the regression test suite

- **Dependencies:** 
  - `self.devicesMFE` - Page object for global header element verification
  - `self.device_card` - Page object for navigation and bell icon click interactions
  - `self.profile` - Page object for verifying side panel close button visibility

- **Module Configurations:** Inherits class-level fixtures `class_setup_fixture_ota_regression` and `function_setup_myhp_launch` applied via the class decorator.

- **Input Parameters:** 
  - `self` - Instance reference to the test class providing access to initialized page objects

- **Return Parameter:** None (pytest test methods return implicitly; assertions determine pass/fail status)

- **Functional Flow:** 
  1. Verifies profile icon visibility using `self.devicesMFE.verify_profile_icon_show_up()`
  2. Asserts profile icon is visible with failure message "profile icon invisible"
  3. Verifies sign-in button visibility using `self.devicesMFE.verify_sign_in_button_show_up()`
  4. Asserts sign-in button is visible with failure message "sign-in button invisible"
  5. Verifies bell icon visibility using `self.devicesMFE.verify_bell_icon_show_up()`
  6. Asserts bell icon is visible with failure message "bell icon invisible"
  7. Verifies PC devices back button visibility using `self.device_card.verify_pc_devices_back_button()`
  8. Asserts back button is visible with failure message "device back button invisible"
  9. Executes back navigation using `self.device_card.click_pc_devices_back_button()`
  10. Re-verifies bell icon visibility after navigation using `self.devicesMFE.verify_bell_icon_show_up()`
  11. Asserts bell icon remains visible with failure message "bell icon invisible"
  12. Executes bell icon click action using `self.device_card.click_bell_icon()`
  13. Verifies avatar close button appears using `self.profile.verify_avatar_close_btn()`
  14. Asserts close button is visible confirming side panel opened with failure message "avatar close button invisible"

- **Assertions:** 
  - Profile icon must be visible in initial state
  - Sign-in button must be visible in initial state
  - Bell icon must be visible in initial state
  - PC devices back button must be visible
  - Bell icon must remain visible after back navigation
  - Avatar close button must appear after clicking bell icon, confirming side panel opened

- **Boundary Conditions:** Requires successful navigation to main view and assumes bell icon click event properly triggers side panel rendering; validates event handler functionality.

- **Exception Handling:** No explicit try-except blocks; pytest captures AssertionError exceptions with custom failure messages for test reporting.

---

#### Method Level: test_04_verify_notifications_sidepanel_opened_upon_clicking_bellicon_C53303696

- **Scope:** Instance Method

- **Purpose:** Validates that clicking the bell notification icon successfully opens the notifications side panel and renders the expected panel content, specifically verifying both the close button and the notifications title are displayed.

- **Annotation or Markers:** 
  - `@pytest.mark.regression` - Tags this test as part of the regression test suite

- **Dependencies:** 
  - `self.devicesMFE` - Page object for global header element verification
  - `self.device_card` - Page object for navigation and bell icon click interactions
  - `self.profile` - Page object for verifying side panel close button
  - `self.bell_icon` - Page object for verifying notification panel content elements

- **Module Configurations:** Inherits class-level fixtures `class_setup_fixture_ota_regression` and `function_setup_myhp_launch` applied via the class decorator.

- **Input Parameters:** 
  - `self` - Instance reference to the test class providing access to initialized page objects

- **Return Parameter:** None (pytest test methods return implicitly; assertions determine pass/fail status)

- **Functional Flow:** 
  1. Verifies profile icon visibility using `self.devicesMFE.verify_profile_icon_show_up()`
  2. Asserts profile icon is visible with failure message "profile icon invisible"
  3. Verifies sign-in button visibility using `self.devicesMFE.verify_sign_in_button_show_up()`
  4. Asserts sign-in button is visible with failure message "sign-in button invisible"
  5. Verifies bell icon visibility using `self.devicesMFE.verify_bell_icon_show_up()`
  6. Asserts bell icon is visible with failure message "bell icon invisible"
  7. Verifies PC devices back button visibility using `self.device_card.verify_pc_devices_back_button()`
  8. Asserts back button is visible with failure message "device back button invisible"
  9. Executes back navigation using `self.device_card.click_pc_devices_back_button()`
  10. Re-verifies bell icon visibility after navigation using `self.devicesMFE.verify_bell_icon_show_up()`
  11. Asserts bell icon remains visible with failure message "bell icon invisible"
  12. Executes bell icon click action using `self.device_card.click_bell_icon()`
  13. Verifies avatar close button appears using `self.profile.verify_avatar_close_btn()`
  14. Asserts close button is visible with failure message "avatar close button invisible"
  15. Verifies notifications title is displayed using `self.bell_icon.verify_notifications_title()`
  16. Asserts notifications title is visible confirming panel content rendered with failure message "notification title invisible"

- **Assertions:** 
  - Profile icon must be visible in initial state
  - Sign-in button must be visible in initial state
  - Bell icon must be visible in initial state
  - PC devices back button must be visible
  - Bell icon must remain visible after back navigation
  - Avatar close button must appear after clicking bell icon
  - Notifications title must be displayed within the opened side panel

- **Boundary Conditions:** Requires successful side panel rendering with complete content loading; validates both structural panel elements (close button) and content elements (title) are properly displayed.

- **Exception Handling:** No explicit try-except blocks; pytest captures AssertionError exceptions with custom failure messages for test reporting.

---

#### Method Level: test_05_verify_empty_bell_state_when_user_not_logged_in_C53303697

- **Scope:** Instance Method

- **Purpose:** Validates the empty state behavior of the bell notification panel when accessed by an unauthenticated user, verifying that the panel displays appropriate empty state content including a sign-in button prompt and allows proper panel closure.

- **Annotation or Markers:** 
  - `@pytest.mark.regression` - Tags this test as part of the regression test suite

- **Dependencies:** 
  - `self.devicesMFE` - Page object for global header element verification
  - `self.device_card` - Page object for bell icon click interactions
  - `self.bell_icon` - Page object for verifying notification panel empty state content
  - `self.profile` - Page object for verifying and interacting with side panel close button

- **Module Configurations:** Inherits class-level fixtures `class_setup_fixture_ota_regression` and `function_setup_myhp_launch` applied via the class decorator.

- **Input Parameters:** 
  - `self` - Instance reference to the test class providing access to initialized page objects

- **Return Parameter:** None (pytest test methods return implicitly; assertions determine pass/fail status)

- **Functional Flow:** 
  1. Verifies profile icon visibility using `self.devicesMFE.verify_profile_icon_show_up()`
  2. Asserts profile icon is visible with failure message "profile icon invisible"
  3. Verifies sign-in button visibility in header using `self.devicesMFE.verify_sign_in_button_show_up()`
  4. Asserts sign-in button is visible with failure message "sign-in button invisible"
  5. Verifies bell icon visibility using `self.devicesMFE.verify_bell_icon_show_up()`
  6. Asserts bell icon is visible with failure message "bell icon invisible"
  7. Executes bell icon click action using `self.device_card.click_bell_icon()`
  8. Verifies notifications title is displayed using `self.bell_icon.verify_notifications_title()`
  9. Asserts notifications title is visible with failure message "notification title invisible"
  10. Verifies sign-in button appears within notification panel using `self.bell_icon.verify_notifications_panel_sign_in_btn()`
  11. Asserts panel sign-in button is visible confirming empty state with failure message "sign-in button in notification panel invisible"
  12. Verifies avatar close button is present using `self.profile.verify_avatar_close_btn()`
  13. Asserts close button is visible with failure message "avatar close button invisible"
  14. Executes close action using `self.profile.click_close_avatar_btn()` to dismiss the notification panel

- **Assertions:** 
  - Profile icon must be visible in initial unauthenticated state
  - Sign-in button must be visible in global header
  - Bell icon must be visible and accessible to unauthenticated users
  - Notifications title must be displayed when panel opens
  - Sign-in button must appear within the notification panel indicating empty state for unauthenticated users
  - Avatar close button must be present allowing panel dismissal
  - Close button click action must execute successfully

- **Boundary Conditions:** Validates unauthenticated user experience; assumes application is in logged-out state; verifies empty state UI rendering and panel dismissal functionality.

- **Exception Handling:** No explicit try-except blocks; pytest captures AssertionError exceptions with custom failure messages for test reporting.

---

## Missing Artifacts

None

---

# PRE-FLIGHT FUNCTION INVENTORY LOG

**Inventory for test_suite_02_bell_notifications.py:** Found 3 total functions/methods:
1. `class_setup` (fixture)
2. `test_01_verify_back_button_visible_on_navigation_side_panel_C42631068`
3. `test_02_verify_back_button_named_as_close_can_be_clicked_C42631069`

---

# COMPREHENSIVE DOCUMENTATION REPORT

## test_suite_02_bell_notifications.py

### MODULE SUMMARY DETAILS

[MODULE_PURPOSE_START]

This test module implements automated regression test cases for the Bell Notifications feature within the HPX Desktop application. It validates the visibility, interaction, and navigation behavior of the notification bell icon and its associated panel UI components, ensuring proper sign-in button display, close button functionality, and panel navigation controls in a Windows desktop environment.

[MODULE_PURPOSE_END]

### 1. File Header (Module-Level Documentation)

- **Primary Responsibility:** Automated UI regression testing for Bell Notifications panel functionality in the HPX Desktop application, verifying notification icon visibility, panel navigation controls, close button behavior, and sign-in button presence across different UI states.

- **Dependencies:** 
  - `pytest` - Core testing framework for test execution, fixtures, and markers
  - `SAF.misc.saf_misc` - SAF framework utility module for JSON loading and configuration management
  - `MobileApps.libs.ma_misc.ma_misc` - Mobile Apps library utility for absolute path resolution
  - `MobileApps.resources.const.windows.const.HPX_ACCOUNT` - Windows platform constant definitions for HPX account credential paths
  - `MobileApps.libs.flows.windows.hpx_rebranding.flow_container.FlowContainer` - Flow container orchestration class managing page object instances and driver interactions

- **Module Configuration:** 
  - `pytest.app_info = "DESKTOP"` - Global pytest configuration identifying the target application platform as Desktop
  - `pytest.set_info = "HPX"` - Global pytest configuration specifying the HPX application context for test execution

---

### 2. Class Documentation: Test_Suite_02_Bell_Notifications

- **Role:** Test suite container class encapsulating all automated regression test cases for Bell Notifications feature validation, managing shared test fixtures, page object instances, and driver lifecycle for Windows desktop HPX application testing.

- **Purpose:** Provides structured test organization for notification panel UI verification scenarios, maintains class-level test state through fixtures, coordinates page object interactions for bell icon and notification panel elements, and ensures proper test environment setup and teardown for OTA regression testing workflows.

---

#### Fixture: class_setup

- **Scope:** Class

- **Purpose:** Initializes and configures the test environment for all test methods within the Test_Suite_02_Bell_Notifications class, establishing driver instances, page object references, credential loading, and pre-test application state preparation.

- **Annotation or Markers:** 
  - `@pytest.fixture(scope="class", autouse=True)` - Declares this method as a pytest fixture with class-level scope that executes automatically before any test methods run

- **Dependencies:** 
  - `request` - Pytest request object providing access to test context and class attributes
  - `windows_test_setup` - Fixture providing initialized Windows application driver instance
  - `utility_web_session` - Fixture providing web driver session for utility operations
  - `FlowContainer` - Flow orchestration class managing page object dictionary and driver operations
  - `saf_misc.load_json` - SAF utility function for loading JSON configuration files
  - `ma_misc.get_abs_path` - Mobile Apps utility function for resolving absolute file paths
  - `HPX_ACCOUNT.account_details_path` - Constant defining the path to HPX account credentials JSON file

- **Parameter:** 
  - `cls` - Class reference parameter (self-referential) for accessing class-level attributes
  - `request` - Pytest request fixture providing test context and class attribute injection capabilities
  - `windows_test_setup` - Pre-configured Windows application driver instance for UI automation
  - `utility_web_session` - Web driver session instance for web-based utility operations

- **Set-up Action:** 
  1. Reassigns `cls` to reference the actual class object via `cls.__class__`
  2. Injects Windows test driver into class via `request.cls.driver = windows_test_setup`
  3. Injects web driver session into class via `request.cls.web_driver = utility_web_session`
  4. Instantiates FlowContainer with driver and assigns to `request.cls.fc`
  5. Terminates any existing HPX processes via `request.cls.fc.kill_hpx_process()`
  6. Extracts page object references from FlowContainer's flow dictionary: `profile`, `devicesMFE`, `device_card`, `bell_icon`
  7. Deletes stored web password credentials via `request.cls.fc.web_password_credential_delete()`
  8. Loads HPID credentials from JSON file using absolute path resolution
  9. Extracts and stores username and password as class-level attributes
  10. Minimizes Chrome browser window via `cls.profile.minimize_chrome()`

- **State Management:** 
  - `cls.profile` - Page object instance for profile-related UI interactions
  - `cls.devicesMFE` - Page object instance for devices micro-frontend UI components
  - `cls.device_card` - Page object instance for device card UI element interactions
  - `cls.bell_icon` - Page object instance for bell notification icon and panel interactions
  - `cls.user_name` - String storing HPID username credential for authentication operations
  - `cls.password` - String storing HPID password credential for authentication operations
  - `request.cls.driver` - Windows application driver instance for UI automation
  - `request.cls.web_driver` - Web driver session for utility web operations
  - `request.cls.fc` - FlowContainer instance managing page objects and driver lifecycle

---

#### Method Level: test_01_verify_back_button_visible_on_navigation_side_panel_C42631068

- **Scope:** Instance Method

- **Purpose:** Validates that the bell notification icon is visible, clickable, and that upon interaction, the notifications panel displays correctly with all required UI elements including the notification title, sign-in button within the panel, and the avatar close button for panel dismissal.

- **Annotation or Markers:** 
  - `@pytest.mark.regression` - Marks this test as part of the regression test suite for automated execution in regression testing workflows

- **Dependencies:** 
  - `self.devicesMFE` - Page object for devices micro-frontend UI verification methods
  - `self.device_card` - Page object for device card UI element interaction and verification methods
  - `self.bell_icon` - Page object for bell notification icon and panel verification methods
  - `self.profile` - Page object for profile UI element verification methods

- **Module Configurations:** Inherits class-level fixtures `class_setup_fixture_ota_regression` and `function_setup_clear_sign_out` from class decorator, ensuring OTA regression environment setup and sign-out state before test execution.

- **Input Parameters:** 
  - `self` - Instance reference to the test class providing access to class-level page object attributes and driver instances

- **Return Parameter:** None (void method; test passes if all assertions succeed, fails if any assertion raises AssertionError)

- **Functional Flow:** 
  1. Verifies sign-in button visibility on devices MFE page via `self.devicesMFE.verify_sign_in_button_show_up()` and asserts True with failure message "sign-in button invisible"
  2. Verifies bell icon presence on device card via `self.device_card.verify_bell_icon_present()` and asserts True with failure message "bell icon invisible"
  3. Clicks the bell notification icon via `self.device_card.click_bell_icon()` to open the notifications panel
  4. Verifies notifications panel title is displayed via `self.bell_icon.verify_notifications_title()` and asserts True with failure message "notification title invisible"
  5. Verifies sign-in button presence within the notifications panel via `self.bell_icon.verify_notifications_panel_sign_in_btn()` and asserts True with failure message "sign-in button in notification panel invisible"
  6. Verifies avatar close button visibility for panel dismissal via `self.profile.verify_avatar_close_btn()` and asserts True with failure message "avatar close button invisible"

- **Assertions:** 
  - Assert that `devicesMFE.verify_sign_in_button_show_up()` returns True, confirming sign-in button is visible on main page
  - Assert that `device_card.verify_bell_icon_present()` returns True, confirming bell icon is present and visible
  - Assert that `bell_icon.verify_notifications_title()` returns True, confirming notifications panel title is displayed after bell icon click
  - Assert that `bell_icon.verify_notifications_panel_sign_in_btn()` returns True, confirming sign-in button exists within the opened notifications panel
  - Assert that `profile.verify_avatar_close_btn()` returns True, confirming close button is visible for dismissing the notifications panel

- **Boundary Conditions:** 
  - Test assumes application is in signed-out state due to `function_setup_clear_sign_out` fixture
  - Test requires bell icon to be in clickable state before interaction
  - Test validates UI element visibility states before and after bell icon click action
  - Test verifies multiple UI components are rendered simultaneously in the opened notifications panel state

- **Exception Handling:** No explicit try-except blocks; relies on pytest's assertion exception handling where AssertionError is raised on assertion failure with custom failure messages for debugging.

---

#### Method Level: test_02_verify_back_button_named_as_close_can_be_clicked_C42631069

- **Scope:** Instance Method

- **Purpose:** Validates the complete interaction workflow of the notifications panel close button, verifying that the close button displays the correct text label "Close", is clickable, and successfully dismisses the notifications panel, returning the UI to its initial state with the bell icon visible and sign-in button present.

- **Annotation or Markers:** 
  - `@pytest.mark.regression` - Marks this test as part of the regression test suite for automated execution in regression testing workflows

- **Dependencies:** 
  - `self.device_card` - Page object for device card UI element interaction and verification methods
  - `self.bell_icon` - Page object for bell notification icon and panel interaction/verification methods
  - `self.devicesMFE` - Page object for devices micro-frontend UI verification methods

- **Module Configurations:** Inherits class-level fixtures `class_setup_fixture_ota_regression` and `function_setup_clear_sign_out` from class decorator, ensuring OTA regression environment setup and sign-out state before test execution.

- **Input Parameters:** 
  - `self` - Instance reference to the test class providing access to class-level page object attributes and driver instances

- **Return Parameter:** None (void method; test passes if all assertions succeed, fails if any assertion raises AssertionError)

- **Functional Flow:** 
  1. Verifies bell icon presence on device card via `self.device_card.verify_bell_icon_present()` and asserts True with failure message "bell icon invisible"
  2. Clicks the bell notification icon via `self.device_card.click_bell_icon()` to open the notifications panel
  3. Verifies notifications panel title is displayed via `self.bell_icon.verify_notifications_title()` and asserts True with failure message "notification title invisible"
  4. Verifies sign-in button presence within the notifications panel via `self.bell_icon.verify_notifications_panel_sign_in_btn()` and asserts True with failure message "sign-in button in notification panel invisible"
  5. Retrieves close button text via `self.bell_icon.verify_notifications_panel_close_btn()` and stores in variable `close_btn_text`
  6. Asserts that `close_btn_text` equals the string "Close" with failure message "Text on Close button is not matching or its incorrect"
  7. Clicks the notifications panel close button via `self.bell_icon.click_notifications_panel_close_btn()` to dismiss the panel
  8. Verifies sign-in button visibility on devices MFE page via `self.devicesMFE.verify_sign_in_button_show_up()` and asserts True with failure message "sign-in button invisible"
  9. Verifies bell icon presence on device card via `self.device_card.verify_bell_icon_present()` and asserts True with failure message "bell icon invisible"

- **Assertions:** 
  - Assert that `device_card.verify_bell_icon_present()` returns True at test start, confirming bell icon is visible before interaction
  - Assert that `bell_icon.verify_notifications_title()` returns True, confirming notifications panel opened successfully
  - Assert that `bell_icon.verify_notifications_panel_sign_in_btn()` returns True, confirming sign-in button is present in opened panel
  - Assert that `close_btn_text == "Close"`, confirming close button displays exact text "Close" (case-sensitive string comparison)
  - Assert that `devicesMFE.verify_sign_in_button_show_up()` returns True after panel dismissal, confirming UI returned to initial state
  - Assert that `device_card.verify_bell_icon_present()` returns True after panel dismissal, confirming bell icon remains visible post-interaction

- **Boundary Conditions:** 
  - Test assumes application is in signed-out state due to `function_setup_clear_sign_out` fixture
  - Test validates exact string match for close button text with case-sensitive comparison ("Close" vs "close")
  - Test verifies UI state restoration after panel dismissal, ensuring no residual panel elements remain visible
  - Test confirms bell icon remains interactable after one complete open-close cycle
  - Test validates that clicking close button successfully dismisses the panel without requiring additional actions

- **Exception Handling:** No explicit try-except blocks; relies on pytest's assertion exception handling where AssertionError is raised on assertion failure with custom failure messages for debugging and test failure diagnosis.

---

## Missing Artifacts

None

---

# test_suite_03_bell_notifications.py

## MODULE SUMMARY DETAILS

[MODULE_PURPOSE_START]

This pytest test suite validates the bell notification system functionality within the HPX Desktop application, specifically testing notification panel UI behavior, message categorization by severity (urgent, warning, informative), authentication-dependent notification visibility, and message sorting/filtering capabilities across production and staging environment exclusions.

[MODULE_PURPOSE_END]

### 1. File Header (Module-Level Documentation)

- **Primary Responsibility:** Automated regression testing of bell notification icon interactions, notification panel rendering, message type color coding verification, authentication state-dependent notification access control, and account-specific message filtering within the HPX rebranding Windows desktop application framework.

- **Dependencies:** 
  - `pytest` - Test framework and fixture management
  - `logging` - Runtime logging infrastructure
  - `SAF.misc.saf_misc` - SAF framework utility functions for JSON loading
  - `MobileApps.libs.ma_misc.ma_misc` - Mobile apps utility library for absolute path resolution
  - `MobileApps.resources.const.windows.const.HPX_ACCOUNT` - HPX account configuration constants
  - `MobileApps.libs.flows.windows.hpx_rebranding.flow_container.FlowContainer` - Flow container orchestration for page object access

- **Module Configuration:** 
  - `pytest.app_info = "DESKTOP"` - Application platform identifier
  - `pytest.set_info = "HPX"` - Test suite identifier for HPX application context

---

### 2. Class Documentation: Test_Suite_03_Bell_Notifications

- **Role:** Pytest test class container encapsulating all bell notification feature validation test cases with shared fixture dependencies and authentication credential management.

- **Purpose:** Provides structured test execution context with class-level setup for driver initialization, page object instantiation, credential loading, and HPX process lifecycle management to ensure isolated test execution across notification UI verification scenarios.

---

#### Fixture: class_setup

- **Scope:** Class

- **Purpose:** Initializes and configures all required test infrastructure components including Windows driver instances, web session utilities, flow container orchestration, page object references, credential cleanup, and HPID account authentication data loading for all test methods within the class lifecycle.

- **Annotation or Markers:** 
  - `@pytest.fixture(scope="class", autouse=True)`

- **Dependencies:** 
  - `windows_test_setup` - Windows application driver fixture
  - `utility_web_session` - Web driver session fixture
  - `FlowContainer` - Page object flow orchestration container
  - `saf_misc.load_json` - JSON configuration file parser
  - `ma_misc.get_abs_path` - Absolute path resolver
  - `HPX_ACCOUNT.account_details_path` - Account credentials file path constant

- **Parameter:** 
  - `cls` - Class reference for attribute assignment
  - `request` - Pytest request object for class attribute injection
  - `windows_test_setup` - Windows desktop application driver instance
  - `utility_web_session` - Web browser driver session instance

- **Set-up Action:** 
  1. Assigns class reference to `cls` variable
  2. Injects `windows_test_setup` driver into `request.cls.driver`
  3. Injects `utility_web_session` web driver into `request.cls.web_driver`
  4. Instantiates `FlowContainer` with Windows driver and assigns to `request.cls.fc`
  5. Terminates any running HPX processes via `fc.kill_hpx_process()`
  6. Extracts `devicesMFE` page object from flow dictionary
  7. Extracts `css` page object from flow dictionary
  8. Extracts `device_card` page object from flow dictionary
  9. Extracts `bell_icon` page object from flow dictionary
  10. Extracts `profile` page object from flow dictionary
  11. Extracts `devices_details_pc_mfe` page object from flow dictionary
  12. Deletes stored web password credentials via `fc.web_password_credential_delete()`
  13. Loads HPID username from JSON account configuration file
  14. Loads HPID password from JSON account configuration file

- **State Management:** 
  - `cls.driver` - Windows application driver instance
  - `cls.web_driver` - Web browser driver instance
  - `cls.fc` - FlowContainer orchestration object
  - `cls.devicesMFE` - Devices MFE page object reference
  - `cls.css` - CSS page object reference
  - `cls.device_card` - Device card page object reference
  - `cls.bell_icon` - Bell icon page object reference
  - `cls.profile` - Profile page object reference
  - `cls.devices_details_pc_mfe` - Devices details PC MFE page object reference
  - `cls.user_name` - HPID account username string
  - `cls.password` - HPID account password string

---

**PRE-FLIGHT FUNCTION INVENTORY LOG:**

Inventory for test_suite_03_bell_notifications.py: Found 8 total functions:
1. class_setup (fixture)
2. test_01_verify_the_color_of_the_urgent_messages_C60336080
3. test_02_verify_the_color_of_the_warning_messages_C60336081
4. test_03_verify_the_color_of_the_informative_messages_C60336082
5. test_04_notifications_panel_opens_on_bell_click_C67874087
6. test_05_no_notifications_when_logged_out_C60336139
7. test_06_only_account_messages_displayed_C58684361
8. test_07_sort_order_of_messages_C58684367

---

#### Method Level: test_01_verify_the_color_of_the_urgent_messages_C60336080

- **Scope:** Instance Method

- **Purpose:** Validates that urgent notification messages display with correct color coding and icon styling by authenticating user, navigating to notification panel, filtering urgent unread messages, and verifying urgent message icon visibility.

- **Annotation or Markers:** 
  - `@pytest.mark.regression`
  - `@pytest.mark.skip_in_prod`
  - `@pytest.mark.skip_in_stg`

- **Dependencies:** 
  - `self.fc.sign_in` - FlowContainer authentication method
  - `self.devicesMFE.verify_bell_icon_show_up` - Bell icon visibility verification
  - `self.device_card.click_bell_icon` - Bell icon click interaction
  - `self.bell_icon.click_notification_account` - Account notification filter selection
  - `self.bell_icon.verify_urgent_unread_notifs` - Urgent notification type verification
  - `self.bell_icon.click_urgent_unread_notifs` - Urgent notification selection
  - `self.bell_icon.verify_urgent_msg_icon` - Urgent message icon visibility check

- **Module Configurations:** None

- **Input Parameters:** 
  - `self` - Test class instance reference

- **Return Parameter:** None (void test method)

- **Functional Flow:** 
  1. Executes user sign-in flow using `self.user_name`, `self.password`, and `self.web_driver`
  2. Asserts bell icon visibility on page with failure message "bell icon invisible"
  3. Clicks bell icon to open notifications panel
  4. Clicks notification account filter to display account-specific notifications
  5. Calls `verify_urgent_unread_notifs()` and captures returned notification type string
  6. Asserts returned notification type equals "urgent notification" with failure message "urgent unread msgs not found"
  7. Clicks urgent unread notification item to expand details
  8. Asserts urgent message icon is visible with failure message "urgent msg icon invisible"

- **Assertions:** 
  - Bell icon must be visible on the page
  - Urgent unread notification type must return "urgent notification" string
  - Urgent message icon must be visible after selecting urgent notification

- **Boundary Conditions:** 
  - Test skipped in production environment
  - Test skipped in staging environment
  - Requires authenticated user session
  - Requires at least one urgent unread notification present in account

- **Exception Handling:** None (relies on pytest assertion failure handling)

---

#### Method Level: test_02_verify_the_color_of_the_warning_messages_C60336081

- **Scope:** Instance Method

- **Purpose:** Validates that warning notification messages display with correct color coding and icon styling by authenticating user, navigating to notification panel, filtering warning unread messages, and verifying warning message icon visibility.

- **Annotation or Markers:** 
  - `@pytest.mark.regression`
  - `@pytest.mark.skip_in_prod`
  - `@pytest.mark.skip_in_stg`

- **Dependencies:** 
  - `self.fc.sign_in` - FlowContainer authentication method
  - `self.devicesMFE.verify_bell_icon_show_up` - Bell icon visibility verification
  - `self.device_card.click_bell_icon` - Bell icon click interaction
  - `self.bell_icon.click_notification_account` - Account notification filter selection
  - `self.bell_icon.verify_warning_unread_notifs` - Warning notification verification
  - `self.bell_icon.click_warning_unread_notifs` - Warning notification selection
  - `self.bell_icon.verify_warning_msg_icon` - Warning message icon visibility check

- **Module Configurations:** None

- **Input Parameters:** 
  - `self` - Test class instance reference

- **Return Parameter:** None (void test method)

- **Functional Flow:** 
  1. Executes user sign-in flow using `self.user_name`, `self.password`, and `self.web_driver`
  2. Asserts bell icon visibility on page with failure message "bell icon invisible"
  3. Clicks bell icon to open notifications panel
  4. Clicks notification account filter to display account-specific notifications
  5. Asserts warning unread notifications are present with failure message "warning unread msgs not found"
  6. Clicks warning unread notification item to expand details
  7. Asserts warning message icon is visible with failure message "warning msg icon invisible"

- **Assertions:** 
  - Bell icon must be visible on the page
  - Warning unread notifications must be present in notification list
  - Warning message icon must be visible after selecting warning notification

- **Boundary Conditions:** 
  - Test skipped in production environment
  - Test skipped in staging environment
  - Requires authenticated user session
  - Requires at least one warning unread notification present in account

- **Exception Handling:** None (relies on pytest assertion failure handling)

---

#### Method Level: test_03_verify_the_color_of_the_informative_messages_C60336082

- **Scope:** Instance Method

- **Purpose:** Validates that informative notification messages display with correct color coding and icon styling by authenticating user, navigating to notification panel, filtering informative unread messages, and verifying informative message icon visibility.

- **Annotation or Markers:** 
  - `@pytest.mark.regression`
  - `@pytest.mark.skip_in_prod`
  - `@pytest.mark.skip_in_stg`

- **Dependencies:** 
  - `self.fc.sign_in` - FlowContainer authentication method
  - `self.devicesMFE.verify_bell_icon_show_up` - Bell icon visibility verification
  - `self.device_card.click_bell_icon` - Bell icon click interaction
  - `self.bell_icon.click_notification_account` - Account notification filter selection
  - `self.bell_icon.verify_informative_unread_notifs` - Informative notification verification
  - `self.bell_icon.click_informative_unread_notifs` - Informative notification selection
  - `self.bell_icon.verify_info_msg_icon` - Informative message icon visibility check

- **Module Configurations:** None

- **Input Parameters:** 
  - `self` - Test class instance reference

- **Return Parameter:** None (void test method)

- **Functional Flow:** 
  1. Executes user sign-in flow using `self.user_name`, `self.password`, and `self.web_driver`
  2. Asserts bell icon visibility on page with failure message "bell icon invisible"
  3. Clicks bell icon to open notifications panel
  4. Clicks notification account filter to display account-specific notifications
  5. Asserts informative unread notifications are present with failure message "informative unread msgs not found"
  6. Clicks informative unread notification item to expand details
  7. Asserts informative message icon is visible with failure message "informative msg icon invisible"

- **Assertions:** 
  - Bell icon must be visible on the page
  - Informative unread notifications must be present in notification list
  - Informative message icon must be visible after selecting informative notification

- **Boundary Conditions:** 
  - Test skipped in production environment
  - Test skipped in staging environment
  - Requires authenticated user session
  - Requires at least one informative unread notification present in account

- **Exception Handling:** None (relies on pytest assertion failure handling)

---

#### Method Level: test_04_notifications_panel_opens_on_bell_click_C67874087

- **Scope:** Instance Method

- **Purpose:** Validates that clicking the bell icon successfully opens the notifications sidebar panel and that all expected navigation elements remain visible including device back button, avatar button, bell icon, plus button, and sign-in button.

- **Annotation or Markers:** 
  - `@pytest.mark.regression`
  - `@pytest.mark.skip_in_prod`
  - `@pytest.mark.skip_in_stg`

- **Dependencies:** 
  - `self.fc.sign_in` - FlowContainer authentication method
  - `self.device_card.verify_pc_devices_back_button` - Device back button visibility verification
  - `self.profile.verify_devicepage_avatar_btn` - Avatar button visibility verification
  - `self.devicesMFE.verify_bell_icon_show_up` - Bell icon visibility verification
  - `self.device_card.verify_homepage_plus_button` - Plus button visibility verification
  - `self.profile.verify_navbar_sign_in_button` - Sign-in button visibility verification
  - `self.device_card.click_bell_icon` - Bell icon click interaction
  - `self.bell_icon.verify_notifications_sidebar_ui` - Notifications sidebar UI verification

- **Module Configurations:** None

- **Input Parameters:** 
  - `self` - Test class instance reference

- **Return Parameter:** None (void test method)

- **Functional Flow:** 
  1. Executes user sign-in flow using `self.user_name`, `self.password`, and `self.web_driver`
  2. Asserts PC devices back button is visible with failure message "device back button not found"
  3. Asserts device page avatar button is visible with failure message "avatar button is not found"
  4. Asserts bell icon is visible with failure message "bell icon is not found"
  5. Asserts homepage plus button is visible with failure message "homepage plus button is not found"
  6. Asserts navbar sign-in button is visible with failure message "sign-in button is not found"
  7. Clicks bell icon to trigger notifications panel opening
  8. Verifies notifications sidebar UI is displayed correctly

- **Assertions:** 
  - PC devices back button must be visible
  - Device page avatar button must be visible
  - Bell icon must be visible
  - Homepage plus button must be visible
  - Navbar sign-in button must be visible
  - Notifications sidebar UI must render correctly after bell icon click

- **Boundary Conditions:** 
  - Test skipped in production environment
  - Test skipped in staging environment
  - Requires authenticated user session
  - All navigation elements must be present before bell icon interaction

- **Exception Handling:** None (relies on pytest assertion failure handling)

---

#### Method Level: test_05_no_notifications_when_logged_out_C60336139

- **Scope:** Instance Method

- **Purpose:** Validates that unauthenticated users see a prompt to sign in when accessing the notifications panel, verifying authentication-gated notification access control and correct notifications panel title display.

- **Annotation or Markers:** 
  - `@pytest.mark.regression`
  - `@pytest.mark.skip_in_prod`
  - `@pytest.mark.skip_in_stg`

- **Dependencies:** 
  - `self.css.verify_sign_in_button_show_up` - Sign-in button visibility verification
  - `self.devicesMFE.verify_bell_icon_show_up` - Bell icon visibility verification
  - `self.device_card.click_bell_icon` - Bell icon click interaction
  - `self.bell_icon.verify_sign_in_to_view_msgs` - Sign-in prompt message verification
  - `self.bell_icon.verify_notifications_sidebar_ui` - Notifications sidebar UI verification with title return

- **Module Configurations:** None

- **Input Parameters:** 
  - `self` - Test class instance reference

- **Return Parameter:** None (void test method)

- **Functional Flow:** 
  1. Asserts sign-in button is visible with failure message "sign-in button invisible"
  2. Asserts bell icon is visible with failure message "bell icon invisible"
  3. Clicks bell icon to open notifications panel in logged-out state
  4. Asserts sign-in prompt message is visible with failure message "sign in or create an account to view all of your messages is invisible"
  5. Calls `verify_notifications_sidebar_ui()` and captures returned notifications title name
  6. Asserts returned title name equals "Notifications" with failure message "notifications title name mismatch"

- **Assertions:** 
  - Sign-in button must be visible when logged out
  - Bell icon must be visible when logged out
  - Sign-in prompt message must be displayed in notifications panel
  - Notifications sidebar title must equal "Notifications"

- **Boundary Conditions:** 
  - Test skipped in production environment
  - Test skipped in staging environment
  - User must be in logged-out state (no authentication performed)
  - Notifications panel must be accessible but content-restricted when unauthenticated

- **Exception Handling:** None (relies on pytest assertion failure handling)

---

#### Method Level: test_06_only_account_messages_displayed_C58684361

- **Scope:** Instance Method

- **Purpose:** Validates that the account notification filter correctly displays only account-specific messages by authenticating user, verifying device visibility, opening notifications panel, selecting account category, and verifying account title display.

- **Annotation or Markers:** 
  - `@pytest.mark.regression`
  - `@pytest.mark.skip_in_prod`
  - `@pytest.mark.skip_in_stg`

- **Dependencies:** 
  - `self.fc.sign_in` - FlowContainer authentication method
  - `self.devices_details_pc_mfe.verify_pc_device_name_show_up` - PC device name visibility verification
  - `self.device_card.verify_bell_icon_present` - Bell icon presence verification
  - `self.device_card.click_bell_icon` - Bell icon click interaction
  - `self.bell_icon.click_notification_account` - Account notification filter selection
  - `self.bell_icon.verify_account_category` - Account category title verification

- **Module Configurations:** None

- **Input Parameters:** 
  - `self` - Test class instance reference

- **Return Parameter:** None (void test method)

- **Functional Flow:** 
  1. Executes user sign-in flow using `self.user_name`, `self.password`, and `self.web_driver`
  2. Asserts PC device name is visible on homepage with failure message "PC name on homepage not loaded/visible"
  3. Asserts bell icon is present with failure message "bell icon invisible"
  4. Clicks bell icon to open notifications panel
  5. Clicks notification account filter to display account-specific notifications
  6. Calls `verify_account_category()` and captures returned account title string
  7. Asserts returned account title equals "Account" with failure message "account title name mismatch"

- **Assertions:** 
  - PC device name must be visible on homepage after authentication
  - Bell icon must be present on page
  - Account category title must equal "Account" after filtering

- **Boundary Conditions:** 
  - Test skipped in production environment
  - Test skipped in staging environment
  - Requires authenticated user session
  - Requires at least one PC device associated with account
  - Account notification category must be available in filter options

- **Exception Handling:** None (relies on pytest assertion failure handling)

---

#### Method Level: test_07_sort_order_of_messages_C58684367

- **Scope:** Instance Method

- **Purpose:** Validates that notification messages are correctly sorted and categorized into "Unread" and "Read" sections within the account notifications view, verifying proper message organization and display hierarchy.

- **Annotation or Markers:** 
  - `@pytest.mark.regression`
  - `@pytest.mark.skip_in_prod`
  - `@pytest.mark.skip_in_stg`

- **Dependencies:** 
  - `self.fc.sign_in` - FlowContainer authentication method
  - `self.device_card.click_bell_icon` - Bell icon click interaction
  - `self.bell_icon.click_notification_account` - Account notification filter selection
  - `self.bell_icon.verify_unread_text` - Unread messages category verification
  - `self.bell_icon.verify_read_text` - Read messages category verification

- **Module Configurations:** None

- **Input Parameters:** 
  - `self` - Test class instance reference

- **Return Parameter:** None (void test method)

- **Functional Flow:** 
  1. Executes user sign-in flow using `self.user_name`, `self.password`, and `self.web_driver`
  2. Clicks bell icon to open notifications panel
  3. Clicks notification account filter to display account-specific notifications
  4. Asserts "Unread" text category is visible with failure message "unread messages category not found"
  5. Asserts "Read" text category is visible with failure message "read messages category not found"

- **Assertions:** 
  - "Unread" messages category must be visible in notifications panel
  - "Read" messages category must be visible in notifications panel

- **Boundary Conditions:** 
  - Test skipped in production environment
  - Test skipped in staging environment
  - Requires authenticated user session
  - Requires notification messages to be present (either read or unread)
  - Message sorting must separate unread and read notifications into distinct categories

- **Exception Handling:** None (relies on pytest assertion failure handling)

---

## Missing Artifacts

None

---

# Exhaustive Code Documentation Report

## test_suite_04_bell_notifications.py

### MODULE SUMMARY DETAILS

[MODULE_PURPOSE_START]

This module implements a comprehensive automated test suite for validating bell notification functionality within the HP Experience (HPX) desktop application. It systematically verifies notification panel behavior, user authentication workflows through notification flyouts, notification categorization (urgent, warning, informative), deletion capabilities, and navigation patterns within the notification system across production and staging environment exclusions.

[MODULE_PURPOSE_END]

### 1. File Header (Module-Level Documentation)

- **Primary Responsibility:** Automated regression testing of bell notification icon visibility, notification panel interactions, user sign-in workflows via notification flyouts, notification type verification (urgent/warning/informative), deletion operations for different notification categories, and back-navigation functionality within the HPX Windows desktop application notification system.

- **Dependencies:** 
  - `logging` - Standard Python logging framework for test execution traceability
  - `pytest` - Core testing framework providing test discovery, fixtures, markers, and assertion mechanisms
  - `SAF.misc.saf_misc` - SAF framework utility module for JSON configuration loading
  - `MobileApps.libs.ma_misc.ma_misc` - Mobile Apps library utility for absolute path resolution
  - `MobileApps.resources.const.windows.const.HPX_ACCOUNT` - Constants module containing HPX account configuration paths
  - `MobileApps.libs.flows.windows.hpx_rebranding.flow_container.FlowContainer` - Flow orchestration container managing page object instances and high-level user workflows

- **Module Configuration:** 
  - `pytest.app_info = "DESKTOP"` - Global pytest configuration identifying target application platform as desktop
  - `pytest.set_info = "HPX"` - Global pytest configuration specifying HP Experience application context

### 2. Class Documentation: Test_Suite_04_Bell_Notifications

- **Role:** Pytest test class encapsulating all bell notification feature validation test cases for HPX desktop application, managing shared test fixtures, page object instances, and authentication credentials across test execution lifecycle.

- **Purpose:** Provides structural organization for bell notification test scenarios, establishes class-level setup/teardown mechanisms, maintains shared state for page objects and user credentials, and enforces environment-specific test execution constraints through pytest markers.

#### Fixture: class_setup

- **Scope:** Class

- **Purpose:** Initializes and configures all required test infrastructure components including WebDriver instances, FlowContainer orchestration, page object references, credential management, and HPX process cleanup before test class execution begins.

- **Annotation or Markers:** 
  - `@pytest.fixture(scope="class", autouse=True)` - Declares class-scoped fixture with automatic execution before any test methods run

- **Dependencies:** 
  - `request` - Pytest request object providing access to test context and class attributes
  - `windows_test_setup` - Fixture providing initialized Windows application driver instance
  - `utility_web_session` - Fixture providing web driver session for authentication workflows
  - `FlowContainer` - Flow orchestration class managing page object dictionary and high-level operations
  - `saf_misc.load_json` - JSON configuration file loader
  - `ma_misc.get_abs_path` - Absolute path resolver for configuration files
  - `HPX_ACCOUNT.account_details_path` - Configuration path constant for account credentials

- **Parameter:** 
  - `cls` - Class reference for setting class-level attributes
  - `request` - Pytest request fixture for accessing test class context
  - `windows_test_setup` - Windows application driver fixture
  - `utility_web_session` - Web driver session fixture for browser-based authentication

- **Set-up Action:** 
  1. Assigns class reference from `cls.__class__` for proper class attribute binding
  2. Binds Windows application driver to `request.cls.driver` for test method access
  3. Binds web driver session to `request.cls.web_driver` for authentication operations
  4. Instantiates FlowContainer with driver and assigns to `request.cls.fc`
  5. Executes `kill_hpx_process()` to terminate any existing HPX application instances
  6. Extracts page object references from FlowContainer's `fd` dictionary: `devicesMFE`, `css`, `device_card`, `bell_icon`, `profile`, `devices_details_pc_mfe`, `hpx_settings`
  7. Invokes `web_password_credential_delete()` to clear stored credentials
  8. Loads username from JSON configuration at `HPX_ACCOUNT.account_details_path` under `["hpid"]["username"]` key
  9. Loads password from JSON configuration at `HPX_ACCOUNT.account_details_path` under `["hpid"]["password"]` key

- **State Management:** 
  - `cls.driver` - Windows application driver instance for UI automation
  - `cls.web_driver` - Web driver session for browser-based authentication
  - `cls.fc` - FlowContainer instance managing page objects and workflows
  - `cls.devicesMFE` - Page object for devices micro-frontend interactions
  - `cls.css` - Page object for common sign-in screen operations
  - `cls.device_card` - Page object for device card UI component interactions
  - `cls.bell_icon` - Page object for bell notification icon and panel operations
  - `cls.profile` - Page object for user profile verification operations
  - `cls.devices_details_pc_mfe` - Page object for PC device details page interactions
  - `cls.hpx_settings` - Page object for HPX settings operations
  - `cls.user_name` - HPID username credential loaded from configuration
  - `cls.password` - HPID password credential loaded from configuration

#### Method Level: test_01_verify_bell_notifications_displayed_when_logged_in_C60339087

- **Scope:** Instance Method

- **Purpose:** Validates that the bell notification icon is visible and accessible after successful user authentication, and verifies that clicking the bell icon opens the notification panel with account-specific notifications.

- **Annotation or Markers:** 
  - `@pytest.mark.regression` - Marks test for inclusion in regression test suites
  - `@pytest.mark.skip_in_prod` - Excludes test execution in production environment
  - `@pytest.mark.skip_in_stg` - Excludes test execution in staging environment

- **Dependencies:** 
  - `self.fc.sign_in()` - FlowContainer authentication method
  - `self.devicesMFE.verify_bell_icon_show_up()` - Bell icon visibility verification method
  - `self.device_card.click_bell_icon()` - Bell icon click interaction method
  - `self.bell_icon.click_notification_account()` - Notification account selection method

- **Module Configurations:** None

- **Input Parameters:** 
  - `self` - Test class instance providing access to fixtures and page objects

- **Return Parameter:** None (pytest test method with assertion-based validation)

- **Functional Flow:** 
  1. Invokes `self.fc.sign_in()` with `self.user_name`, `self.password`, and `self.web_driver` to authenticate user
  2. Calls `self.devicesMFE.verify_bell_icon_show_up()` to check bell icon visibility
  3. Asserts bell icon presence with failure message "bell icon is not present"
  4. Executes `self.device_card.click_bell_icon()` to open notification panel
  5. Calls `self.bell_icon.click_notification_account()` to access account notifications

- **Assertions:** 
  - Bell icon must be visible after user sign-in (assertion failure message: "bell icon is not present")

- **Boundary Conditions:** 
  - Test requires successful user authentication before bell icon verification
  - Test skipped in production and staging environments

- **Exception Handling:** No explicit exception handling; relies on pytest assertion framework for failure reporting

#### Method Level: test_02_verify_transition_from_empty_bell_to_notification_bell_on_login_C60339089

- **Scope:** Instance Method

- **Purpose:** Validates the complete user journey from unauthenticated state (empty bell with sign-in prompt) through authentication workflow to authenticated state (bell with categorized notifications), verifying UI state transitions and notification type availability.

- **Annotation or Markers:** 
  - `@pytest.mark.regression` - Marks test for inclusion in regression test suites
  - `@pytest.mark.skip_in_prod` - Excludes test execution in production environment
  - `@pytest.mark.skip_in_stg` - Excludes test execution in staging environment

- **Dependencies:** 
  - `self.devicesMFE.verify_bell_icon_show_up()` - Bell icon visibility verification
  - `self.device_card.click_bell_icon()` - Bell icon interaction
  - `self.bell_icon.verify_notifications_panel_sign_in_btn()` - Sign-in button presence verification
  - `self.bell_icon.click_notifications_panel_close_btn()` - Notification panel close action
  - `self.devices_details_pc_mfe.verify_back_devices_button_on_pc_devices_page_show_up()` - Device details page verification
  - `self.css.verify_sign_in_button_show_up()` - Main sign-in button visibility check
  - `self.css.click_sign_in_button()` - Main sign-in button click action
  - `self.fc.sign_in()` - Authentication workflow execution
  - `self.profile.verify_top_profile_icon_signed_in()` - Post-authentication profile verification
  - `self.bell_icon.click_notification_account()` - Account notification access
  - `self.bell_icon.verify_urgent_unread_notifs()` - Urgent notification verification
  - `self.bell_icon.verify_informative_unread_notifs()` - Informative notification verification
  - `self.bell_icon.verify_warning_unread_notifs()` - Warning notification verification

- **Module Configurations:** None

- **Input Parameters:** 
  - `self` - Test class instance providing access to fixtures and page objects

- **Return Parameter:** None (pytest test method with assertion-based validation)

- **Functional Flow:** 
  1. Asserts bell icon visibility with failure message "bell icon not visible"
  2. Clicks bell icon to open notification panel
  3. Verifies sign-in button presence in notification panel with failure message "sign-in button in notification panel is not present"
  4. Closes notification panel via close button
  5. Verifies device details page loaded with failure message "Device details page not loaded"
  6. Verifies main sign-in button visibility with failure message "sign-in button invisible"
  7. Clicks main sign-in button to initiate authentication
  8. Executes sign-in workflow with `user_icon_click=False` parameter
  9. Verifies user signed-in state via profile icon with failure message "User not signed in/After signing in the 'Sign In' button failed to disappear after 20 seconds"
  10. Clicks bell icon again to open authenticated notification panel
  11. Clicks notification account to view notifications
  12. Verifies urgent notification type equals "urgent notification" with failure message "urgent unread msgs not found"
  13. Verifies informative notification type equals "informative notification" with failure message "informative unread msgs not found"
  14. Verifies warning notification type equals "warning notification" with failure message "warning unread msgs not found"

- **Assertions:** 
  - Bell icon must be visible before interaction
  - Sign-in button must be present in unauthenticated notification panel
  - Device details page must load after closing notification panel
  - Main sign-in button must be visible
  - User profile icon must indicate signed-in state after authentication
  - Urgent notification type must return "urgent notification"
  - Informative notification type must return "informative notification"
  - Warning notification type must return "warning notification"

- **Boundary Conditions:** 
  - Test validates complete state transition from unauthenticated to authenticated
  - Test requires all three notification types (urgent, informative, warning) to be present
  - Test skipped in production and staging environments

- **Exception Handling:** No explicit exception handling; relies on pytest assertion framework for failure reporting

#### Method Level: test_03_verify_login_using_sign_in_option_in_bell_flyout_C60372196

- **Scope:** Instance Method

- **Purpose:** Validates that users can successfully authenticate directly through the sign-in button within the bell notification flyout panel, verifying user initials display after successful login.

- **Annotation or Markers:** 
  - `@pytest.mark.regression` - Marks test for inclusion in regression test suites
  - `@pytest.mark.skip_in_prod` - Excludes test execution in production environment
  - `@pytest.mark.skip_in_stg` - Excludes test execution in staging environment

- **Dependencies:** 
  - `self.devicesMFE.verify_bell_icon_show_up()` - Bell icon visibility verification
  - `self.device_card.click_bell_icon()` - Bell icon interaction
  - `self.bell_icon.verify_notifications_panel_sign_in_btn()` - Sign-in button presence verification
  - `self.bell_icon.click_notifications_panel_sign_in_btn()` - Notification panel sign-in button click
  - `self.fc.sign_in()` - Authentication workflow execution
  - `self.profile.get_user_initials_after_signin()` - User initials retrieval method

- **Module Configurations:** None

- **Input Parameters:** 
  - `self` - Test class instance providing access to fixtures and page objects

- **Return Parameter:** None (pytest test method with assertion-based validation)

- **Functional Flow:** 
  1. Asserts bell icon visibility with failure message "bell icon not visible"
  2. Clicks bell icon to open notification panel
  3. Verifies sign-in button presence in notification panel with failure message "sign-in button in notification panel is not present"
  4. Clicks sign-in button within notification panel
  5. Executes sign-in workflow with `user_icon_click=False` parameter
  6. Retrieves user initials after sign-in completion
  7. Asserts user initials match expected values ("RG" or "RP") with failure message "User not signed in/credentials not matching"

- **Assertions:** 
  - Bell icon must be visible
  - Sign-in button must be present in notification panel
  - User initials must be either "RG" or "RP" after successful authentication

- **Boundary Conditions:** 
  - Test validates authentication specifically through notification panel sign-in button
  - Test expects specific user initials ("RG" or "RP") indicating test account credentials
  - Test skipped in production and staging environments

- **Exception Handling:** No explicit exception handling; relies on pytest assertion framework for failure reporting

#### Method Level: test_04_verify_delete_option_for_urgent_unread_msg_is_disabled_C60336470

- **Scope:** Instance Method

- **Purpose:** Validates that urgent unread notifications have a disabled delete option, enforcing business rule that critical urgent messages cannot be deleted by users.

- **Annotation or Markers:** 
  - `@pytest.mark.regression` - Marks test for inclusion in regression test suites
  - `@pytest.mark.skip_in_prod` - Excludes test execution in production environment
  - `@pytest.mark.skip_in_stg` - Excludes test execution in staging environment

- **Dependencies:** 
  - `self.fc.sign_in()` - Authentication workflow execution
  - `self.devicesMFE.verify_bell_icon_show_up()` - Bell icon visibility verification
  - `self.device_card.click_bell_icon()` - Bell icon interaction
  - `self.bell_icon.click_notification_account()` - Account notification access
  - `self.bell_icon.verify_unread_text()` - Unread messages category verification
  - `self.bell_icon.verify_urgent_unread_notifs()` - Urgent notification presence verification
  - `self.bell_icon.click_urgent_unread_notification_ellipsis()` - Urgent notification options menu interaction
  - `self.bell_icon.verify_delete_disabled_urgent_unread_notifs()` - Delete option disabled state verification

- **Module Configurations:** None

- **Input Parameters:** 
  - `self` - Test class instance providing access to fixtures and page objects

- **Return Parameter:** None (pytest test method with assertion-based validation)

- **Functional Flow:** 
  1. Executes user sign-in workflow
  2. Asserts bell icon visibility with failure message "bell icon not visible"
  3. Clicks bell icon to open notification panel
  4. Clicks notification account to view notifications
  5. Asserts unread messages category presence with failure message "unread messages category not found"
  6. Asserts urgent unread notifications presence with failure message "urgent unread notifications is not present"
  7. Clicks ellipsis menu for urgent unread notification
  8. Verifies delete option is disabled with failure message "delete option is enabled"

- **Assertions:** 
  - Bell icon must be visible after authentication
  - Unread messages category must be present
  - Urgent unread notifications must be present
  - Delete option for urgent notifications must be disabled

- **Boundary Conditions:** 
  - Test requires at least one urgent unread notification to be present
  - Test validates business rule preventing deletion of urgent notifications
  - Test skipped in production and staging environments

- **Exception Handling:** No explicit exception handling; relies on pytest assertion framework for failure reporting

#### Method Level: test_05_verify_delete_option_for_warning_unread_msg_is_enabled_C60336471

- **Scope:** Instance Method

- **Purpose:** Validates that warning unread notifications have an enabled delete option and that deletion operation successfully removes the warning notification from the notification panel.

- **Annotation or Markers:** 
  - `@pytest.mark.regression` - Marks test for inclusion in regression test suites
  - `@pytest.mark.skip_in_prod` - Excludes test execution in production environment
  - `@pytest.mark.skip_in_stg` - Excludes test execution in staging environment

- **Dependencies:** 
  - `self.fc.sign_in()` - Authentication workflow execution
  - `self.devicesMFE.verify_bell_icon_show_up()` - Bell icon visibility verification
  - `self.device_card.click_bell_icon()` - Bell icon interaction
  - `self.bell_icon.click_notification_account()` - Account notification access
  - `self.bell_icon.verify_unread_text()` - Unread messages category verification
  - `self.bell_icon.verify_warning_unread_notifs()` - Warning notification verification and type retrieval
  - `self.bell_icon.verify_unread_warning_notifs_name()` - Warning notification name retrieval
  - `self.bell_icon.click_warning_unread_notifs_ellipsis()` - Warning notification options menu interaction
  - `self.bell_icon.click_delete_warning_unread_notifs()` - Warning notification deletion action
  - `logging.info()` - Logging framework for notification name output

- **Module Configurations:** None

- **Input Parameters:** 
  - `self` - Test class instance providing access to fixtures and page objects

- **Return Parameter:** None (pytest test method with assertion-based validation)

- **Functional Flow:** 
  1. Executes user sign-in workflow
  2. Asserts bell icon visibility with failure message "bell icon not visible"
  3. Clicks bell icon to open notification panel
  4. Clicks notification account to view notifications
  5. Asserts unread messages category presence with failure message "unread messages category not found"
  6. Retrieves notification type from warning unread notifications
  7. Asserts notification type equals "warning notification" with failure message "warning unread msgs not found"
  8. Retrieves warning notification name
  9. Logs notification name using `logging.info()`
  10. Clicks ellipsis menu for warning unread notification
  11. Clicks delete option for warning notification
  12. Asserts warning notification no longer present with failure message "Warning notification still present"

- **Assertions:** 
  - Bell icon must be visible after authentication
  - Unread messages category must be present
  - Warning notification type must return "warning notification"
  - Warning notification must not be present after deletion operation

- **Boundary Conditions:** 
  - Test requires at least one warning unread notification to be present before deletion
  - Test validates complete deletion workflow including UI state update
  - Test skipped in production and staging environments

- **Exception Handling:** No explicit exception handling; relies on pytest assertion framework for failure reporting

#### Method Level: test_06_verify_delete_option_for_informative_unread_msg_is_enabled_C60336472

- **Scope:** Instance Method

- **Purpose:** Validates that informative unread notifications have an enabled delete option and that deletion operation successfully removes the informative notification from the notification panel.

- **Annotation or Markers:** 
  - `@pytest.mark.regression` - Marks test for inclusion in regression test suites
  - `@pytest.mark.skip_in_prod` - Excludes test execution in production environment
  - `@pytest.mark.skip_in_stg` - Excludes test execution in staging environment

- **Dependencies:** 
  - `self.fc.sign_in()` - Authentication workflow execution
  - `self.device_card.click_bell_icon()` - Bell icon interaction
  - `self.bell_icon.click_notification_account()` - Account notification access
  - `self.bell_icon.verify_unread_text()` - Unread messages category verification
  - `self.bell_icon.verify_informative_unread_notifs()` - Informative notification presence verification
  - `self.bell_icon.click_informative_unread_notifs_ellipsis()` - Informative notification options menu interaction
  - `self.bell_icon.click_delete_informative_unread_notifs()` - Informative notification deletion action

- **Module Configurations:** None

- **Input Parameters:** 
  - `self` - Test class instance providing access to fixtures and page objects

- **Return Parameter:** None (pytest test method with assertion-based validation)

- **Functional Flow:** 
  1. Executes user sign-in workflow
  2. Clicks bell icon to open notification panel
  3. Clicks notification account to view notifications
  4. Asserts unread messages category presence with failure message "unread messages category not found"
  5. Asserts informative unread notifications presence with failure message "informative unread notifications is not present"
  6. Clicks ellipsis menu for informative unread notification
  7. Clicks delete option for informative notification
  8. Asserts informative notification no longer present with failure message "informative notification still present"

- **Assertions:** 
  - Unread messages category must be present
  - Informative unread notifications must be present before deletion
  - Informative notification must not be present after deletion operation

- **Boundary Conditions:** 
  - Test requires at least one informative unread notification to be present before deletion
  - Test validates complete deletion workflow including UI state update
  - Test skipped in production and staging environments

- **Exception Handling:** No explicit exception handling; relies on pytest assertion framework for failure reporting

#### Method Level: test_07_verify_user_can_navigate_back_to_navigation_side_panel_C60370254

- **Scope:** Instance Method

- **Purpose:** Validates that users can navigate from a detailed notification view back to the main notification side panel, verifying back button presence, correct text label, and successful navigation to notification list view.

- **Annotation or Markers:** 
  - `@pytest.mark.regression` - Marks test for inclusion in regression test suites
  - `@pytest.mark.skip_in_prod` - Excludes test execution in production environment
  - `@pytest.mark.skip_in_stg` - Excludes test execution in staging environment

- **Dependencies:** 
  - `self.fc.sign_in()` - Authentication workflow execution
  - `self.device_card.click_bell_icon()` - Bell icon interaction
  - `self.bell_icon.click_notification_account()` - Account notification access
  - `self.bell_icon.verify_unread_text()` - Unread messages category verification
  - `self.bell_icon.verify_informative_unread_notifs()` - Informative notification presence verification
  - `self.bell_icon.verify_unread_informative_notifs_name()` - Informative notification name retrieval
  - `self.bell_icon.click_informative_unread_notifs()` - Informative notification detail view navigation
  - `self.bell_icon.verify_detailed_notification_back_btn()` - Back button verification and text retrieval
  - `self.bell_icon.click_detailed_notification_back_btn()` - Back button click action
  - `self.bell_icon.verify_notification_side_panel()` - Notification side panel visibility verification
  - `logging.info()` - Logging framework for notification name output

- **Module Configurations:** None

- **Input Parameters:** 
  - `self` - Test class instance providing access to fixtures and page objects

- **Return Parameter:** None (pytest test method with assertion-based validation)

- **Functional Flow:** 
  1. Executes user sign-in workflow
  2. Clicks bell icon to open notification panel
  3. Clicks notification account to view notifications
  4. Asserts unread messages category presence with failure message "unread messages category not found"
  5. Asserts informative unread notifications presence with failure message "informative unread notifications is not present"
  6. Retrieves informative notification name
  7. Logs notification name using `logging.info()`
  8. Clicks informative notification to open detailed view
  9. Retrieves back button text from detailed notification page
  10. Asserts back button text equals "Account" with failure message "Back button not present OR text incorrect on detailed notification page"
  11. Clicks back button to navigate to notification list
  12. Asserts notification side panel visibility with failure message "notifications side panel invisible"

- **Assertions:** 
  - Unread messages category must be present
  - Informative unread notifications must be present
  - Back button text on detailed notification page must equal "Account"
  - Notification side panel must be visible after back navigation

- **Boundary Conditions:** 
  - Test requires at least one informative unread notification to be present
  - Test validates complete navigation workflow from list to detail and back to list
  - Test verifies specific back button text label "Account"
  - Test skipped in production and staging environments

- **Exception Handling:** No explicit exception handling; relies on pytest assertion framework for failure reporting

---

## Missing Artifacts

None

---

# test_suite_05_bell_notifications.py

## MODULE SUMMARY DETAILS

[MODULE_PURPOSE_START]

This test suite validates the bell notification system functionality within the HP Smart Desktop application (HPX). It verifies notification UI elements, interaction behaviors, read/unread state transitions, notification type categorization (informative, warning, urgent), and detailed notification view components across production and staging environment exclusions.

[MODULE_PURPOSE_END]

### 1. File Header (Module-Level Documentation)

- **Primary Responsibility:** Automated regression testing of bell notification features including notification tile interactions, ellipsis menu functionality, mark-as-read operations across multiple notification severity types, and detailed notification view navigation within the HP Smart Windows desktop application.

- **Dependencies:** 
  - `pytest` - Test framework and fixture management
  - `logging` - Runtime logging for test execution tracking
  - `SAF.misc.saf_misc` - SAF framework utility functions for JSON loading
  - `MobileApps.libs.ma_misc.ma_misc` - Mobile apps utility library for path resolution
  - `MobileApps.resources.const.windows.const.HPX_ACCOUNT` - Account credential configuration constants
  - `MobileApps.libs.flows.windows.hpx_rebranding.flow_container.FlowContainer` - Flow orchestration container for HPX test operations

- **Module Configuration:** 
  - `pytest.app_info = "DESKTOP"` - Defines application platform target as desktop environment
  - `pytest.set_info = "HPX"` - Specifies HPX (HP Smart) application context
  - Class-level fixtures: `class_setup_fixture_ota_regression`, `function_setup_clear_sign_out`

### 2. Class Documentation: Test_Suite_05_Bell_Notifications

- **Role:** Encapsulates all test cases validating bell notification system behaviors, UI element presence, interaction workflows, and state management for notification read/unread transitions within the HPX desktop application.

- **Purpose:** Provides structured test execution context with shared setup fixtures, page object references, and credential management to systematically verify notification panel functionality, dropdown menu interactions, notification type filtering, and detailed view navigation across multiple test scenarios.

#### Fixture: class_setup

- **Scope:** Class

- **Purpose:** Initializes shared test infrastructure including driver instances, page object references, credential loading, and pre-test environment cleanup to establish consistent test execution state across all notification test methods.

- **Annotation or Markers:** `@pytest.fixture(scope="class", autouse=True)`

- **Dependencies:** 
  - `request` - Pytest request fixture for class attribute injection
  - `windows_test_setup` - Windows application driver fixture
  - `utility_web_session` - Web driver session fixture for authentication flows
  - `FlowContainer` - Flow orchestration container
  - `saf_misc.load_json` - JSON credential file loader
  - `ma_misc.get_abs_path` - Absolute path resolver

- **Parameter:** 
  - `cls` - Class reference for attribute assignment
  - `request` - Pytest request object for class attribute injection
  - `windows_test_setup` - Windows application driver instance
  - `utility_web_session` - Web driver session for browser-based authentication

- **Set-up Action:** 
  1. Assigns class reference to `cls` variable
  2. Injects `windows_test_setup` driver into `request.cls.driver`
  3. Injects `utility_web_session` web driver into `request.cls.web_driver`
  4. Instantiates `FlowContainer` with driver and assigns to `request.cls.fc`
  5. Terminates any running HPX processes via `fc.kill_hpx_process()`
  6. Extracts page object references from flow dictionary: `profile`, `css`, `device_card`, `bell_icon`, `hpx_settings`, `devices_details_pc_mfe`
  7. Deletes stored web password credentials via `fc.web_password_credential_delete()`
  8. Loads HPID credentials from JSON configuration file at `HPX_ACCOUNT.account_details_path`
  9. Assigns username and password to class attributes `cls.user_name` and `cls.password`
  10. Minimizes Chrome browser window via `cls.profile.minimize_chrome()`

- **State Management:** 
  - `cls.profile` - Profile page object reference
  - `cls.css` - CSS/sign-in page object reference
  - `cls.device_card` - Device card page object reference
  - `cls.bell_icon` - Bell notification icon page object reference
  - `cls.hpx_settings` - HPX settings page object reference
  - `cls.devices_details_pc_mfe` - PC device details MFE page object reference
  - `cls.user_name` - HPID username credential
  - `cls.password` - HPID password credential

#### Method Level: test_01_verify_notification_tile_ellipsis_clickable_C60339095

- **Scope:** Instance Method

- **Purpose:** Validates that the notification tile ellipsis menu is clickable and reveals a dropdown containing "Mark as Read" and "Delete" options, ensuring notification management controls are accessible and functional.

- **Annotation or Markers:** 
  - `@pytest.mark.regression`
  - `@pytest.mark.skip_in_prod`
  - `@pytest.mark.skip_in_stg`

- **Dependencies:** 
  - `self.profile` - Profile page object for sign-in state verification
  - `self.css` - CSS page object for sign-in button interaction
  - `self.fc` - Flow container for sign-in orchestration
  - `self.device_card` - Device card page object for bell icon interaction
  - `self.bell_icon` - Bell icon page object for notification panel interactions
  - `self.web_driver` - Web driver for authentication flows

- **Module Configurations:** Test execution restricted to non-production and non-staging environments via skip markers.

- **Input Parameters:** 
  - `self` - Test class instance with initialized fixtures and page objects

- **Return Parameter:** None (test method with assertion-based validation)

- **Functional Flow:** 
  1. Check if user is already logged in via `self.profile.verify_top_profile_icon_signed_in()`
  2. If not logged in, click sign-in button via `self.css.click_sign_in_button()`
  3. Execute sign-in flow via `self.fc.sign_in(self.user_name, self.password, self.web_driver)`
  4. Assert profile icon displays user initials after sign-in
  5. Assert bell icon is present on device card
  6. Click bell icon to open notifications panel
  7. Assert notifications title is visible
  8. Click notification account section
  9. Assert notification tile ellipsis is visible
  10. Click notification tile ellipsis
  11. Assert notification dropdown menu is revealed
  12. Assert "Mark as Read" option is present in dropdown
  13. Assert "Delete" option is present in dropdown

- **Assertions:** 
  - Profile icon shows initials after sign-in (failure message: "Profile icon isn't showing initials after sign-in")
  - Bell icon is present (failure message: "bell icon invisible")
  - Notifications title is visible (failure message: "notification title invisible")
  - Notification tile ellipsis is visible (failure message: "notification tile ellipsis invisible")
  - Notification dropdown is revealed (failure message: "notification drop down invisible")
  - "Mark as Read" option is present (failure message: "mark as read option not visible in dropdown")
  - "Delete" option is present (failure message: "delete option not found in dropdown")

- **Boundary Conditions:** Test skipped in production and staging environments; requires pre-existing notifications in the account.

- **Exception Handling:** No explicit exception handling; relies on pytest assertion failure mechanisms.

#### Method Level: test_02_verify_mark_as_read_option_enabled_for_all_notification_types_C60339094

- **Scope:** Instance Method

- **Purpose:** Verifies that the "Mark as Read" functionality operates correctly across all three notification severity types (urgent, informative, warning), ensuring unread notifications transition to read state and maintain name consistency between unread and read views.

- **Annotation or Markers:** 
  - `@pytest.mark.regression`
  - `@pytest.mark.skip_in_prod`
  - `@pytest.mark.skip_in_stg`

- **Dependencies:** 
  - `self.fc` - Flow container for sign-in orchestration
  - `self.profile` - Profile page object for sign-in state verification
  - `self.device_card` - Device card page object for bell icon interaction
  - `self.bell_icon` - Bell icon page object for notification interactions
  - `self.hpx_settings` - HPX settings page object for window management
  - `self.web_driver` - Web driver for authentication flows
  - `logging` - Python logging module for notification name tracking

- **Module Configurations:** Test execution restricted to non-production and non-staging environments.

- **Input Parameters:** 
  - `self` - Test class instance with initialized fixtures and page objects

- **Return Parameter:** None (test method with assertion-based validation)

- **Functional Flow:** 
  1. Execute sign-in flow via `self.fc.sign_in(self.user_name, self.password, self.web_driver)`
  2. Verify profile icon shows signed-in state
  3. Assert bell icon is present
  4. Click bell icon to open notifications panel
  5. Assert notifications title is visible
  6. Click notification account section
  7. **Urgent Notification Processing:**
     - Retrieve urgent unread notification name
     - Log notification name
     - Assert urgent unread notification ellipsis is visible
     - Click urgent unread notification ellipsis
     - Verify and click "Mark as Read" option
     - Swipe to read notifications section
     - Minimize and restore HPX from taskbar
     - Assert urgent notifications are present in read section
     - Retrieve urgent read notification name
     - Log read notification name
     - Assert unread and read notification names match
     - Swipe to top of notifications section
     - Minimize and restore HPX from taskbar
  8. **Informative Notification Processing:**
     - Retrieve informative unread notification name
     - Log notification name
     - Assert informative unread notification ellipsis is visible
     - Click informative unread notification ellipsis
     - Verify and click "Mark as Read" option
     - Swipe to read notifications section
     - Minimize and restore HPX from taskbar
     - Assert informative notifications are present in read section
     - Retrieve informative read notification name
     - Log read notification name
     - Assert unread and read notification names match
     - Swipe to top of notifications section
     - Minimize and restore HPX from taskbar
  9. **Warning Notification Processing:**
     - Retrieve warning unread notification name
     - Log notification name
     - Assert warning unread notification ellipsis is visible
     - Click warning unread notification ellipsis
     - Verify and click "Mark as Read" option
     - Swipe to read notifications section
     - Minimize and restore HPX from taskbar
     - Assert warning notifications are present in read section
     - Retrieve warning read notification name
     - Log read notification name
     - Assert unread and read notification names match

- **Assertions:** 
  - Profile icon shows signed-in state (failure message: "Profile icon isn't showing initials after sign-in")
  - Bell icon is present (failure message: "bell icon invisible")
  - Notifications title is visible (failure message: "notification title invisible")
  - Urgent unread notification ellipsis is visible (failure message: "urgent unread notification ellipsis invisible")
  - Urgent notifications are present in read section (failure message: "urgent notifications not found")
  - Urgent notification name matches between unread and read states (failure message: "urgent msg did not get marked as read after opening the notification")
  - Informative unread notification ellipsis is visible (failure message: "informative unread notification ellipsis invisible")
  - Informative notifications are present in read section (failure message: "informative notifications not found")
  - Informative notification name matches between unread and read states (failure message: "informative msg did not get marked as read after opening the notification")
  - Warning unread notification ellipsis is visible (failure message: "warning unread notification ellipsis not found")
  - Warning notifications are present in read section (failure message: "warning notifications not found")
  - Warning notification name matches between unread and read states (failure message: "warning msg did not get marked as read after opening the notification")

- **Boundary Conditions:** Requires at least one notification of each type (urgent, informative, warning) in unread state; test skipped in production and staging environments.

- **Exception Handling:** No explicit exception handling; relies on pytest assertion failure mechanisms and logging for diagnostic information.

#### Method Level: test_03_verify_unread_read_notifications_C53303701

- **Scope:** Instance Method

- **Purpose:** Validates the presence and categorization of all three notification types (informative, warning, urgent) in both unread and read sections, ensuring proper notification type identification and section organization within the notifications panel.

- **Annotation or Markers:** 
  - `@pytest.mark.regression`
  - `@pytest.mark.skip_in_prod`
  - `@pytest.mark.skip_in_stg`

- **Dependencies:** 
  - `self.fc` - Flow container for sign-in orchestration
  - `self.profile` - Profile page object for sign-in state verification
  - `self.device_card` - Device card page object for bell icon interaction
  - `self.bell_icon` - Bell icon page object for notification type verification
  - `self.driver` - Windows application driver for swipe gestures
  - `self.hpx_settings` - HPX settings page object for window management
  - `self.web_driver` - Web driver for authentication flows

- **Module Configurations:** Test execution restricted to non-production and non-staging environments.

- **Input Parameters:** 
  - `self` - Test class instance with initialized fixtures and page objects

- **Return Parameter:** None (test method with assertion-based validation)

- **Functional Flow:** 
  1. Execute sign-in flow via `self.fc.sign_in(self.user_name, self.password, self.web_driver)`
  2. Assert profile icon shows signed-in state
  3. Assert bell icon is present
  4. Click bell icon to open notifications panel
  5. Assert notifications title is visible
  6. Click notification account section
  7. Assert "Unread" text category is visible
  8. Verify informative unread notifications are present and retrieve notification type
  9. Assert notification type equals "informative notification"
  10. Verify warning unread notifications are present and retrieve notification type
  11. Assert notification type equals "warning notification"
  12. Verify urgent unread notifications are present and retrieve notification type
  13. Assert notification type equals "urgent notification"
  14. Swipe to "read_text" section via driver swipe gesture
  15. Minimize and restore HPX from taskbar
  16. Assert "Read" text category is visible
  17. Assert informative read notifications are visible
  18. Assert warning read notifications are visible
  19. Assert urgent read notifications are visible

- **Assertions:** 
  - Profile icon shows signed-in state (failure message: "Profile icon isn't showing initials after sign-in")
  - Bell icon is present (failure message: "bell icon invisible")
  - Notifications title is visible (failure message: "notification title invisible")
  - "Unread" category is visible (failure message: "unread notifications category invisible")
  - Informative unread notifications type matches (failure message: "informative unread msgs not found")
  - Warning unread notifications type matches (failure message: "warning unread msgs not found")
  - Urgent unread notifications type matches (failure message: "urgent unread msgs not found")
  - "Read" category is visible (failure message: "read notifications category invisible")
  - Informative read notifications are visible (failure message: "informative read notifications invisible")
  - Warning read notifications are visible (failure message: "warning read notifications invisible")
  - Urgent read notifications are visible (failure message: "urgent read notifications invisible")

- **Boundary Conditions:** Requires at least one notification of each type in both unread and read states; test skipped in production and staging environments.

- **Exception Handling:** No explicit exception handling; relies on pytest assertion failure mechanisms.

#### Method Level: test_04_verify_elements_in_notifs_title_C60339091

- **Scope:** Instance Method

- **Purpose:** Validates detailed notification view elements including notification title consistency between list and detail views, message icon visibility, description content, timestamp format validation, back button functionality, and homepage element restoration after navigation.

- **Annotation or Markers:** 
  - `@pytest.mark.regression`
  - `@pytest.mark.skip_in_prod`
  - `@pytest.mark.skip_in_stg`

- **Dependencies:** 
  - `self.profile` - Profile page object for sign-in state verification
  - `self.css` - CSS page object for sign-in button interaction
  - `self.fc` - Flow container for sign-in orchestration
  - `self.device_card` - Device card page object for bell icon and homepage element verification
  - `self.bell_icon` - Bell icon page object for notification detail view interactions
  - `self.driver` - Windows application driver for swipe gestures
  - `self.hpx_settings` - HPX settings page object for window management
  - `self.devices_details_pc_mfe` - PC device details page object for homepage verification
  - `self.web_driver` - Web driver for authentication flows
  - `logging` - Python logging module for notification detail tracking

- **Module Configurations:** Test execution restricted to non-production and non-staging environments.

- **Input Parameters:** 
  - `self` - Test class instance with initialized fixtures and page objects

- **Return Parameter:** None (test method with assertion-based validation)

- **Functional Flow:** 
  1. Check if user is already logged in via `self.profile.verify_top_profile_icon_signed_in()`
  2. If not logged in:
     - Click sign-in button via `self.css.click_sign_in_button()`
     - Execute sign-in flow with `user_icon_click=False` parameter
  3. Assert profile icon shows signed-in state
  4. Assert bell icon is present
  5. Click bell icon to open notifications panel
  6. Assert notifications title is visible
  7. Click notification account section
  8. Assert "Unread" category is visible
  9. Swipe to "read_text" section via driver swipe gesture
  10. Minimize and restore HPX from taskbar
  11. Assert notification tile ellipsis is present
  12. Assert urgent notifications are present in read section
  13. Retrieve urgent read notification name
  14. Log urgent read notification name
  15. Click urgent read notification to open detailed view
  16. Retrieve detailed notification title
  17. Log detailed notification title
  18. Assert list view and detail view notification names match
  19. Assert urgent message icon is visible
  20. Retrieve notification description
  21. Log notification description
  22. Assert timestamp is present
  23. Retrieve timestamp text
  24. Log timestamp
  25. Assert timestamp contains "ago" (case-insensitive)
  26. Assert timestamp contains at least one digit
  27. Verify detailed notification back button and retrieve button text
  28. Assert back button text equals "Account"
  29. Click detailed notification back button
  30. Click notifications back button
  31. Click notifications panel close button
  32. Assert profile icon shows signed-in state
  33. Assert bell icon is present
  34. Assert PC device name is visible on homepage
  35. Assert device back button is present
  36. Assert homepage plus button is present

- **Assertions:** 
  - Profile icon shows signed-in state (failure message: "Profile icon isn't showing initials after sign-in")
  - Bell icon is present (failure message: "bell icon invisible")
  - Notifications title is visible (failure message: "notification title invisible")
  - "Unread" category is visible (failure message: "unread notifications category invisible")
  - Notification tile ellipsis is present (failure message: "notification ellipsis not found")
  - Urgent notifications are present (failure message: "urgent notifications not found")
  - List view and detail view notification names match (failure message: "urgent notif name mismatch between list view and detailed view")
  - Urgent message icon is visible (failure message: "urgent msg icon invisible")
  - Timestamp is present (failure message: "message time stamp not present")
  - Timestamp contains "ago" (failure message: "Timestamp should contain 'ago', got: '{timestamp}'")
  - Timestamp contains a digit (failure message: "Timestamp should contain a number. Got: '{timestamp}'")
  - Back button text equals "Account" (failure message: "detailed notification back btn text mismatch")
  - Profile icon shows signed-in state after navigation (failure message: "Profile icon isn't showing initials after sign-in")
  - Bell icon is present after navigation (failure message: "bell icon invisible")
  - PC device name is visible (failure message: "PC name on homepage not loaded/visible")
  - Device back button is present (failure message: "device back button not found")
  - Homepage plus button is present (failure message: "homepage plus button is not found")

- **Boundary Conditions:** Requires at least one urgent notification in read state; timestamp format must contain "ago" keyword and numeric value; test skipped in production and staging environments.

- **Exception Handling:** No explicit exception handling; relies on pytest assertion failure mechanisms and logging for diagnostic information capture.

---

## PRE-FLIGHT FUNCTION INVENTORY LOG

**Inventory for test_suite_05_bell_notifications.py:** Found 5 total functions:
1. `class_setup` (fixture)
2. `test_01_verify_notification_tile_ellipsis_clickable_C60339095`
3. `test_02_verify_mark_as_read_option_enabled_for_all_notification_types_C60339094`
4. `test_03_verify_unread_read_notifications_C53303701`
5. `test_04_verify_elements_in_notifs_title_C60339091`

---

## Missing Artifacts

None

---

# test_suite_06_bell_notifcations.py

## MODULE SUMMARY DETAILS

[MODULE_PURPOSE_START]

This test suite module validates the bell notification system functionality within the HP Experience (HPX) desktop application, specifically testing notification display, categorization (informative, urgent, warning), read/unread state transitions, and detailed notification view navigation. The module executes automated UI interaction tests using pytest framework with Windows driver integration and page object model architecture.

[MODULE_PURPOSE_END]

### 1. File Header (Module-Level Documentation)

- **Primary Responsibility:** Automated regression testing of bell notification features including notification type verification, read/unread status management, detailed view navigation, and notification description retrieval across multiple notification categories (informative, urgent, warning) within the HPX Windows desktop application.

- **Dependencies:** 
  - `pytest` - Test framework for test execution, fixtures, and markers
  - `logging` - Standard Python logging for test execution tracking
  - `SAF.misc.saf_misc` - SAF framework miscellaneous utilities for JSON loading
  - `MobileApps.libs.ma_misc.ma_misc` - Mobile Apps library miscellaneous utilities for path resolution
  - `MobileApps.resources.const.windows.const.HPX_ACCOUNT` - HPX account configuration constants
  - `MobileApps.libs.flows.windows.hpx_rebranding.flow_container.FlowContainer` - Flow container orchestrating page objects and driver interactions

- **Module Configuration:** 
  - `pytest.app_info = "DESKTOP"` - Global pytest configuration identifying target application platform
  - `pytest.set_info = "HPX"` - Global pytest configuration identifying target application set as HP Experience

---

### 2. Class Documentation: Test_Suite_06_Bell_Notifications

- **Role:** Test suite container class encapsulating all bell notification feature validation test cases, managing shared test fixtures, page object instances, and authentication credentials for HPX desktop application notification testing.

- **Purpose:** Provides structural organization for notification-related test methods, centralizes class-level setup/teardown operations, manages driver lifecycle, initializes page object dependencies, and maintains test isolation through fixture-based configuration and credential management.

---

#### Fixture: class_setup

- **Scope:** Class

- **Purpose:** Initializes and configures all required test infrastructure components, page object instances, driver sessions, and authentication credentials needed across all test methods within the Test_Suite_06_Bell_Notifications class, ensuring consistent test environment setup before any test execution.

- **Annotation or Markers:** 
  - `@pytest.fixture(scope="class", autouse=True)` - Pytest fixture decorator with class-level scope and automatic execution

- **Dependencies:** 
  - `request` - Pytest request object for accessing test context
  - `windows_test_setup` - Fixture providing Windows application driver instance
  - `utility_web_session` - Fixture providing web driver session for credential management
  - `FlowContainer` - Flow orchestration container managing page object dictionary
  - `saf_misc.load_json` - JSON file loader utility
  - `ma_misc.get_abs_path` - Absolute path resolution utility
  - `HPX_ACCOUNT.account_details_path` - Configuration path constant for account credentials

- **Parameter:** 
  - `cls` - Class reference for setting class-level attributes
  - `request` - Pytest request fixture for class attribute injection
  - `windows_test_setup` - Windows driver fixture instance
  - `utility_web_session` - Web driver session fixture instance

- **Set-up Action:** 
  1. Assigns class reference from `cls` parameter to enable class-level attribute modification
  2. Injects `windows_test_setup` driver instance into `request.cls.driver` class attribute
  3. Injects `utility_web_session` web driver into `request.cls.web_driver` class attribute
  4. Instantiates `FlowContainer` with driver and assigns to `request.cls.fc`
  5. Terminates any existing HPX process via `fc.kill_hpx_process()` to ensure clean state
  6. Extracts page object references from flow container dictionary: `devicesMFE`, `css`, `device_card`, `bell_icon`, `profile`
  7. Clears stored web password credentials via `fc.web_password_credential_delete()`
  8. Loads HPX account credentials JSON file from configured path
  9. Extracts and stores username from JSON structure at `["hpid"]["username"]`
  10. Extracts and stores password from JSON structure at `["hpid"]["password"]`

- **State Management:** 
  - `cls.driver` - Windows application driver instance for UI automation
  - `cls.web_driver` - Web driver session for credential operations
  - `cls.fc` - FlowContainer instance managing page object lifecycle
  - `cls.devicesMFE` - Devices MFE page object reference
  - `cls.css` - CSS page object reference
  - `cls.device_card` - Device card page object reference
  - `cls.bell_icon` - Bell icon page object reference for notification interactions
  - `cls.profile` - Profile page object reference
  - `cls.user_name` - HPID username credential string
  - `cls.password` - HPID password credential string

---

## PRE-FLIGHT FUNCTION INVENTORY LOG

**Inventory for test_suite_06_bell_notifcations.py:** Found 5 total functions:
1. class_setup (fixture)
2. test_01_open_detailed_view_from_message_C58684404
3. test_02_mark_message_as_read_by_opening_C58684406
4. test_03_verify_unread_notifs_description_C60336160
5. test_04_verify_read_notifs_description_C60336161

---

#### Method Level: test_01_open_detailed_view_from_message_C58684404

- **Scope:** Instance Method

- **Purpose:** Validates the ability to navigate from the bell notification list to the detailed view of an urgent read notification message, verifying that the detailed description can be retrieved and displayed correctly.

- **Annotation or Markers:** 
  - `@pytest.mark.regression` - Marks test as part of regression test suite
  - `@pytest.mark.skip_in_prod` - Excludes test execution in production environment
  - `@pytest.mark.skip_in_stg` - Excludes test execution in staging environment

- **Dependencies:** 
  - `self.fc.sign_in` - FlowContainer authentication method
  - `self.device_card.click_bell_icon` - Device card page object bell icon interaction
  - `self.bell_icon.click_notification_account` - Bell icon page object account notification navigation
  - `self.driver.swipe` - Driver swipe gesture method
  - `self.bell_icon.verify_urgent_notifications` - Bell icon page object urgent notification verification
  - `self.bell_icon.click_urgent_read_notifs` - Bell icon page object urgent read notification click action
  - `self.bell_icon.get_notif_description` - Bell icon page object notification description retrieval
  - `logging.info` - Standard logging information output

- **Module Configurations:** None explicitly referenced

- **Input Parameters:** 
  - `self` - Instance reference providing access to class-level fixtures and page objects

- **Return Parameter:** None (void test method)

- **Functional Flow:** 
  1. Authenticates user by calling `self.fc.sign_in` with username, password, and web driver credentials
  2. Clicks bell icon on device card via `self.device_card.click_bell_icon()` to open notification panel
  3. Navigates to notification account view via `self.bell_icon.click_notification_account()`
  4. Performs downward swipe gesture on "read_text" element with direction parameter "down"
  5. Asserts urgent notifications section exists using `self.bell_icon.verify_urgent_notifications()` with failure message "urgent notifications not found"
  6. Clicks on urgent read notification item via `self.bell_icon.click_urgent_read_notifs()`
  7. Retrieves notification description text via `self.bell_icon.get_notif_description()` and stores in `description` variable
  8. Logs retrieved description with prefix "Message detailed view: " using `logging.info`

- **Assertions:** 
  - Verifies urgent notifications section is present in notification list with assertion message "urgent notifications not found"

- **Boundary Conditions:** 
  - Requires at least one urgent read notification to exist in the notification list
  - Swipe gesture assumes "read_text" element is present and scrollable
  - Notification description must be retrievable from detailed view

- **Exception Handling:** No explicit try-except blocks; relies on pytest assertion failure handling and page object method exception propagation

---

#### Method Level: test_02_mark_message_as_read_by_opening_C58684406

- **Scope:** Instance Method

- **Purpose:** Validates the automatic read status transition functionality by verifying that an unread informative notification is correctly marked as read after opening its detailed view, confirming the notification name persists across state change.

- **Annotation or Markers:** 
  - `@pytest.mark.regression` - Marks test as part of regression test suite
  - `@pytest.mark.skip_in_prod` - Excludes test execution in production environment
  - `@pytest.mark.skip_in_stg` - Excludes test execution in staging environment

- **Dependencies:** 
  - `self.fc.sign_in` - FlowContainer authentication method
  - `self.device_card.click_bell_icon` - Device card page object bell icon interaction
  - `self.bell_icon.click_notification_account` - Bell icon page object account notification navigation
  - `self.bell_icon.verify_unread_text` - Bell icon page object unread category verification
  - `self.bell_icon.verify_informative_unread_notifs` - Bell icon page object informative unread notification verification
  - `self.bell_icon.verify_unread_informative_notifs_name` - Bell icon page object unread informative notification name retrieval
  - `self.bell_icon.click_informative_unread_notifs` - Bell icon page object informative unread notification click action
  - `self.bell_icon.get_notif_description` - Bell icon page object notification description retrieval
  - `self.bell_icon.click_detailed_notification_back_btn` - Bell icon page object back button navigation
  - `self.bell_icon.verify_informative_notifications` - Bell icon page object informative read notifications verification
  - `self.bell_icon.get_informative_notifications_name` - Bell icon page object read informative notification name retrieval
  - `logging.info` - Standard logging information output

- **Module Configurations:** None explicitly referenced

- **Input Parameters:** 
  - `self` - Instance reference providing access to class-level fixtures and page objects

- **Return Parameter:** None (void test method)

- **Functional Flow:** 
  1. Authenticates user by calling `self.fc.sign_in` with username, password, and web driver credentials
  2. Clicks bell icon on device card via `self.device_card.click_bell_icon()` to open notification panel
  3. Navigates to notification account view via `self.bell_icon.click_notification_account()`
  4. Asserts unread messages category exists using `self.bell_icon.verify_unread_text()` with failure message "unread messages category not found"
  5. Verifies informative unread notifications presence via `self.bell_icon.verify_informative_unread_notifs()` with failure message "info unread msgs not found"
  6. Retrieves unread informative notification name via `self.bell_icon.verify_unread_informative_notifs_name()` and stores in `unread_informative_notifs_name`
  7. Logs unread notification name with prefix "informative unread notifs name: "
  8. Clicks informative unread notification via `self.bell_icon.click_informative_unread_notifs()` to open detailed view
  9. Retrieves notification description via `self.bell_icon.get_notif_description()` and stores in `description`
  10. Logs message description with prefix "msg description: "
  11. Navigates back to notification list via `self.bell_icon.click_detailed_notification_back_btn()`
  12. Asserts informative notifications section (read) exists using `self.bell_icon.verify_informative_notifications()` with failure message "informative notifications not found"
  13. Retrieves read informative notification name via `self.bell_icon.get_informative_notifications_name()` and stores in `read_informative_notifs_name`
  14. Logs read notification name with prefix "read informative notifs name: "
  15. Asserts unread and read notification names match with failure message "informative msg did not get marked as read after opening the notification"

- **Assertions:** 
  - Verifies unread messages category section is present with assertion message "unread messages category not found"
  - Verifies informative unread notifications exist with assertion message "info unread msgs not found"
  - Verifies informative notifications (read) section exists with assertion message "informative notifications not found"
  - Verifies notification name equality between unread and read states with assertion message "informative msg did not get marked as read after opening the notification"

- **Boundary Conditions:** 
  - Requires at least one informative unread notification to exist before test execution
  - Assumes notification name remains consistent across read state transition
  - Requires back navigation to successfully return to notification list view

- **Exception Handling:** No explicit try-except blocks; relies on pytest assertion failure handling and page object method exception propagation

---

#### Method Level: test_03_verify_unread_notifs_description_C60336160

- **Scope:** Instance Method

- **Purpose:** Comprehensively validates the retrieval and display of notification descriptions for all three unread notification types (informative, urgent, warning), verifying that each category's notification name and detailed description can be accessed and logged correctly.

- **Annotation or Markers:** 
  - `@pytest.mark.regression` - Marks test as part of regression test suite
  - `@pytest.mark.skip_in_prod` - Excludes test execution in production environment
  - `@pytest.mark.skip_in_stg` - Excludes test execution in staging environment

- **Dependencies:** 
  - `self.fc.sign_in` - FlowContainer authentication method
  - `self.device_card.click_bell_icon` - Device card page object bell icon interaction
  - `self.bell_icon.click_notification_account` - Bell icon page object account notification navigation
  - `self.bell_icon.verify_unread_text` - Bell icon page object unread category verification
  - `self.bell_icon.verify_unread_informative_notifs_name` - Bell icon page object unread informative notification name retrieval
  - `self.bell_icon.verify_informative_unread_notifs` - Bell icon page object informative unread notification verification
  - `self.bell_icon.click_informative_unread_notifs` - Bell icon page object informative unread notification click action
  - `self.bell_icon.get_notif_description` - Bell icon page object notification description retrieval
  - `self.bell_icon.click_detailed_notification_back_btn` - Bell icon page object back button navigation
  - `self.bell_icon.verify_unread_urgent_notifs_name` - Bell icon page object unread urgent notification name retrieval
  - `self.bell_icon.verify_urgent_unread_notifs` - Bell icon page object urgent unread notification verification
  - `self.bell_icon.click_urgent_unread_notifs` - Bell icon page object urgent unread notification click action
  - `self.bell_icon.verify_warning_unread_notifs` - Bell icon page object warning unread notification verification
  - `self.bell_icon.verify_unread_warning_notifs_name` - Bell icon page object unread warning notification name retrieval
  - `self.bell_icon.click_warning_unread_notifs` - Bell icon page object warning unread notification click action
  - `logging.info` - Standard logging information output

- **Module Configurations:** None explicitly referenced

- **Input Parameters:** 
  - `self` - Instance reference providing access to class-level fixtures and page objects

- **Return Parameter:** None (void test method)

- **Functional Flow:** 
  1. Authenticates user by calling `self.fc.sign_in` with username, password, and web driver credentials
  2. Clicks bell icon on device card via `self.device_card.click_bell_icon()` to open notification panel
  3. Navigates to notification account view via `self.bell_icon.click_notification_account()`
  4. Asserts unread messages category exists using `self.bell_icon.verify_unread_text()` with failure message "unread messages category not found"
  5. Retrieves informative unread notification name via `self.bell_icon.verify_unread_informative_notifs_name()` and stores in `informative_notifs_name`
  6. Logs informative notification name with prefix "Notification Name: "
  7. Asserts informative unread notifications exist using `self.bell_icon.verify_informative_unread_notifs()` with failure message "informative unread notifications is not present"
  8. Clicks informative unread notification via `self.bell_icon.click_informative_unread_notifs()` to open detailed view
  9. Retrieves notification description via `self.bell_icon.get_notif_description()` and stores in `description`
  10. Logs informative unread notification description with prefix "Informative unread notification description: "
  11. Navigates back to notification list via `self.bell_icon.click_detailed_notification_back_btn()`
  12. Retrieves urgent unread notification name via `self.bell_icon.verify_unread_urgent_notifs_name()` and stores in `urgent_notifs_name`
  13. Logs urgent notification name with prefix "Notification Name: "
  14. Asserts urgent unread notifications exist using `self.bell_icon.verify_urgent_unread_notifs()` with failure message "urgent unread msgs not found"
  15. Clicks urgent unread notification via `self.bell_icon.click_urgent_unread_notifs()` to open detailed view
  16. Retrieves notification description via `self.bell_icon.get_notif_description()` and stores in `description`
  17. Logs urgent unread notification description with prefix "Urgent unread notification description: "
  18. Navigates back to notification list via `self.bell_icon.click_detailed_notification_back_btn()`
  19. Asserts warning unread notifications exist using `self.bell_icon.verify_warning_unread_notifs()` with failure message "warning unread notifications is not present"
  20. Retrieves warning unread notification name via `self.bell_icon.verify_unread_warning_notifs_name()` and stores in `warning_notifs_name`
  21. Logs warning notification name with prefix "Notification Name: "
  22. Asserts warning unread notifications exist (duplicate check) using `self.bell_icon.verify_warning_unread_notifs()` with failure message "warning unread msgs not found"
  23. Clicks warning unread notification via `self.bell_icon.click_warning_unread_notifs()` to open detailed view
  24. Retrieves notification description via `self.bell_icon.get_notif_description()` and stores in `description`
  25. Logs warning unread notification description with prefix "Warning unread notification description: "

- **Assertions:** 
  - Verifies unread messages category section is present with assertion message "unread messages category not found"
  - Verifies informative unread notifications exist with assertion message "informative unread notifications is not present"
  - Verifies urgent unread notifications exist with assertion message "urgent unread msgs not found"
  - Verifies warning unread notifications exist (first check) with assertion message "warning unread notifications is not present"
  - Verifies warning unread notifications exist (second check) with assertion message "warning unread msgs not found"

- **Boundary Conditions:** 
  - Requires at least one unread notification in each category (informative, urgent, warning) to exist
  - Assumes back navigation successfully returns to notification list after each detailed view
  - Notification descriptions must be retrievable for all three notification types

- **Exception Handling:** No explicit try-except blocks; relies on pytest assertion failure handling and page object method exception propagation

---

#### Method Level: test_04_verify_read_notifs_description_C60336161

- **Scope:** Instance Method

- **Purpose:** Validates the retrieval and display of notification descriptions for all three read notification types (informative, urgent, warning), verifying that previously read notifications maintain accessible detailed descriptions and can be navigated correctly after application minimization and restoration.

- **Annotation or Markers:** 
  - `@pytest.mark.regression` - Marks test as part of regression test suite
  - `@pytest.mark.skip_in_prod` - Excludes test execution in production environment
  - `@pytest.mark.skip_in_stg` - Excludes test execution in staging environment

- **Dependencies:** 
  - `self.fc.sign_in` - FlowContainer authentication method
  - `self.devicesMFE.verify_bell_icon_show_up` - Devices MFE page object bell icon visibility verification
  - `self.device_card.click_bell_icon` - Device card page object bell icon interaction
  - `self.bell_icon.click_notification_account` - Bell icon page object account notification navigation
  - `self.driver.swipe` - Driver swipe gesture method
  - `self.hpx_settings.minimize_and_click_hp_from_taskbar` - HPX settings page object application minimize and restore action
  - `self.bell_icon.verify_informative_notifications` - Bell icon page object informative read notifications verification
  - `self.bell_icon.click_informative_read_notifs` - Bell icon page object informative read notification click action
  - `self.bell_icon.get_notif_description` - Bell icon page object notification description retrieval
  - `self.bell_icon.click_notifications_back_btn` - Bell icon page object back button navigation
  - `self.bell_icon.verify_urgent_notifications` - Bell icon page object urgent read notifications verification
  - `self.bell_icon.click_urgent_read_notifs` - Bell icon page object urgent read notification click action
  - `self.bell_icon.verify_warning_notifications` - Bell icon page object warning read notifications verification
  - `self.bell_icon.click_warning_read_notifs` - Bell icon page object warning read notification click action
  - `logging.info` - Standard logging information output

- **Module Configurations:** None explicitly referenced

- **Input Parameters:** 
  - `self` - Instance reference providing access to class-level fixtures and page objects

- **Return Parameter:** None (void test method)

- **Functional Flow:** 
  1. Authenticates user by calling `self.fc.sign_in` with username, password, and web driver credentials
  2. Verifies bell icon visibility via `self.devicesMFE.verify_bell_icon_show_up()`
  3. Clicks bell icon on device card via `self.device_card.click_bell_icon()` to open notification panel
  4. Navigates to notification account view via `self.bell_icon.click_notification_account()`
  5. Performs swipe gesture on "read_text" element via `self.driver.swipe("read_text")`
  6. Minimizes application and restores from taskbar via `self.hpx_settings.minimize_and_click_hp_from_taskbar()`
  7. Asserts informative read notifications exist using `self.bell_icon.verify_informative_notifications()` with failure message "informative read msgs not found"
  8. Clicks informative read notification via `self.bell_icon.click_informative_read_notifs()` to open detailed view
  9. Retrieves notification description via `self.bell_icon.get_notif_description()` and stores in `description`
  10. Logs informative read notification description with prefix "Informative read notification description: "
  11. Navigates back to notification list via `self.bell_icon.click_notifications_back_btn()`
  12. Asserts urgent read notifications exist using `self.bell_icon.verify_urgent_notifications()` with failure message "urgent read msgs not found"
  13. Clicks urgent read notification via `self.bell_icon.click_urgent_read_notifs()` to open detailed view
  14. Retrieves notification description via `self.bell_icon.get_notif_description()` and stores in `description`
  15. Logs urgent read notification description with prefix "Urgent read notification description: "
  16. Navigates back to notification list via `self.bell_icon.click_notifications_back_btn()`
  17. Asserts warning read notifications exist using `self.bell_icon.verify_warning_notifications()` with failure message "warning read msgs not found"
  18. Clicks warning read notification via `self.bell_icon.click_warning_read_notifs()` to open detailed view
  19. Retrieves notification description via `self.bell_icon.get_notif_description()` and stores in `description`
  20. Logs warning read notification description with prefix "Warning read notification description: "

- **Assertions:** 
  - Verifies informative read notifications exist with assertion message "informative read msgs not found"
  - Verifies urgent read notifications exist with assertion message "urgent read msgs not found"
  - Verifies warning read notifications exist with assertion message "warning read msgs not found"

- **Boundary Conditions:** 
  - Requires at least one read notification in each category (informative, urgent, warning) to exist
  - Assumes application can be successfully minimized and restored from taskbar
  - Swipe gesture assumes "read_text" element is present and scrollable
  - Back navigation must successfully return to notification list after each detailed view

- **Exception Handling:** No explicit try-except blocks; relies on pytest assertion failure handling and page object method exception propagation

---

## Missing Artifacts

None

---

# test_suite_07_bell_notifcations.py

## MODULE SUMMARY DETAILS

[MODULE_PURPOSE_START]

This test suite validates the bell notification flyout functionality within the HP Experience (HPX) desktop application for Windows. It verifies user interactions with notification categories, message viewing capabilities in read/unread sections, close button functionality, and notification persistence across application relaunches. The module executes regression-level automated UI tests using the pytest framework integrated with Windows automation drivers and page object models.

[MODULE_PURPOSE_END]

### 1. File Header (Module-Level Documentation)

- **Primary Responsibility:** Automated regression testing of bell notification system features in the HPX Windows desktop application, including notification panel UI interactions, message categorization, read/unread state management, and application state persistence validation.

- **Dependencies:** 
  - `pytest` - Test framework for test execution, fixtures, and markers
  - `logging` - Standard Python logging for test execution traceability
  - `SAF.misc.saf_misc` - SAF framework utility functions for JSON configuration loading
  - `MobileApps.libs.ma_misc.ma_misc` - Mobile Apps library utilities for absolute path resolution
  - `MobileApps.resources.const.windows.const.HPX_ACCOUNT` - Windows platform constants for HPX account credential paths
  - `MobileApps.libs.flows.windows.hpx_rebranding.flow_container.FlowContainer` - Flow orchestration container managing page object instances and test workflows

- **Module Configuration:** 
  - `pytest.app_info = "DESKTOP"` - Global pytest configuration identifying the target application platform as desktop
  - `pytest.set_info = "HPX"` - Global pytest configuration specifying the HPX application context

### 2. Class Documentation: Test_Suite_07_Bell_Notifications

- **Role:** Test class container encapsulating all automated test cases for bell notification feature validation in the HPX Windows application

- **Purpose:** Organizes and executes regression test scenarios validating bell icon visibility, notification flyout interactions, message categorization (read/unread), close button functionality, and notification state persistence across application lifecycle events

#### Fixture: class_setup

- **Scope:** Class

- **Purpose:** Initializes the test environment at the class level by setting up Windows automation drivers, web session utilities, flow container orchestration, page object references, credential management, and browser window state preparation before any test method execution

- **Annotation or Markers:** 
  - `@pytest.fixture(scope="class", autouse=True)` - Pytest fixture decorator with class-level scope and automatic execution

- **Dependencies:** 
  - `windows_test_setup` - Pytest fixture providing Windows automation driver instance
  - `utility_web_session` - Pytest fixture providing web driver session for browser-based interactions
  - `FlowContainer` - Flow orchestration class managing page object dictionary and workflow utilities
  - `saf_misc.load_json` - SAF utility for loading JSON configuration files
  - `ma_misc.get_abs_path` - Mobile Apps utility for resolving absolute file paths
  - `HPX_ACCOUNT.account_details_path` - Constant defining the path to HPX account credentials JSON file

- **Parameter:** 
  - `cls` - Class reference for setting class-level attributes
  - `request` - Pytest request object providing access to test context and class instance
  - `windows_test_setup` - Injected fixture providing Windows driver instance
  - `utility_web_session` - Injected fixture providing web driver session

- **Set-up Action:** 
  1. Assigns class reference from `cls` parameter to enable class-level attribute assignment
  2. Assigns Windows automation driver from `windows_test_setup` fixture to `request.cls.driver`
  3. Assigns web driver session from `utility_web_session` fixture to `request.cls.web_driver`
  4. Instantiates `FlowContainer` with Windows driver and assigns to `request.cls.fc`
  5. Invokes `kill_hpx_process()` to terminate any existing HPX application processes
  6. Extracts page object references from flow container's `fd` dictionary: `profile`, `device_card`, `bell_icon`, `devicesMFE`, `devices_details_pc_mfe`
  7. Invokes `web_password_credential_delete()` to clear stored web credentials
  8. Loads HPX account credentials from JSON file using `saf_misc.load_json` and `ma_misc.get_abs_path`
  9. Extracts username and password from `hpid` key in credentials dictionary
  10. Assigns username to `cls.user_name` and password to `cls.password`
  11. Invokes `cls.profile.minimize_chrome()` to minimize browser window

- **State Management:** 
  - `cls.driver` - Windows automation driver instance for desktop application control
  - `cls.web_driver` - Web driver session for browser-based interactions
  - `cls.fc` - FlowContainer instance managing page objects and workflows
  - `cls.profile` - Page object for user profile interactions
  - `cls.device_card` - Page object for device card UI interactions
  - `cls.bell_icon` - Page object for bell notification icon and flyout interactions
  - `cls.devicesMFE` - Page object for devices micro-frontend interactions
  - `cls.devices_details_pc_mfe` - Page object for PC device details micro-frontend interactions
  - `cls.user_name` - HPID username credential loaded from configuration
  - `cls.password` - HPID password credential loaded from configuration

#### Method Level: test_01_verify_close_button_functionality_in_bell_notification_flyout_C60339090

- **Scope:** Instance Method

- **Purpose:** Validates that the close button is visible within the bell notification flyout panel and successfully closes the flyout when clicked, ensuring proper UI control functionality for dismissing notifications

- **Annotation or Markers:** 
  - `@pytest.mark.regression` - Marks test as part of regression test suite

- **Dependencies:** 
  - `self.devices_details_pc_mfe` - Page object for PC device details verification
  - `self.devicesMFE` - Page object for home navigation
  - `self.fc` - FlowContainer for sign-in workflow orchestration
  - `self.profile` - Page object for user authentication state verification
  - `self.device_card` - Page object for bell icon interaction
  - `self.bell_icon` - Page object for notification flyout verification and close button interaction

- **Module Configurations:** None

- **Input Parameters:** 
  - `self` - Instance reference to test class providing access to class-level fixtures and page objects

- **Return Parameter:** None (pytest test method with assertion-based validation)

- **Functional Flow:** 
  1. Asserts PC device name visibility on device details page using `verify_pc_device_name_show_up()`
  2. Navigates to home screen for logged-in users via `click_home_loggedin()`
  3. Executes sign-in workflow using `fc.sign_in()` with username, password, web driver, and `user_icon_click=False` parameter
  4. Verifies user signed-in state by checking top profile icon using `verify_top_profile_icon_signed_in()`
  5. Asserts bell icon visibility using `verify_bell_icon_show_up()`
  6. Clicks bell icon to open notification flyout using `click_bell_icon()`
  7. Asserts account category visibility in notification flyout using `verify_account_category()`
  8. Verifies shortcuts category presence using `verify_shortcuts_category()`
  9. Asserts close button visibility in notification panel using `verify_notifications_panel_close_btn()`
  10. Clicks close button to dismiss notification flyout using `click_notifications_panel_close_btn()`

- **Assertions:** 
  - PC device name must be present on device details page
  - User must be successfully signed in with profile icon visible within 20 seconds
  - Bell icon must be visible in the UI
  - Account category must be visible in bell notification flyout
  - Close button must be visible in bell notification flyout

- **Boundary Conditions:** 
  - 20-second timeout for sign-in verification
  - UI element visibility dependent on application state and rendering timing

- **Exception Handling:** None explicitly defined; pytest assertion failures will raise AssertionError with custom failure messages

#### Method Level: test_02_verify_users_can_view_unread_messages_C60339083

- **Scope:** Instance Method

- **Purpose:** Validates that users can successfully view unread messages in the bell notification flyout by navigating to the account notification section, verifying unread notification presence, accessing read notifications, and retrieving notification descriptions

- **Annotation or Markers:** 
  - `@pytest.mark.regression` - Marks test as part of regression test suite

- **Dependencies:** 
  - `self.devices_details_pc_mfe` - Page object for PC device details verification
  - `self.devicesMFE` - Page object for home navigation
  - `self.fc` - FlowContainer for sign-in workflow orchestration
  - `self.profile` - Page object for user authentication state verification
  - `self.device_card` - Page object for bell icon interaction
  - `self.bell_icon` - Page object for notification interactions and verification
  - `logging` - Standard logging module for test execution traceability

- **Module Configurations:** None

- **Input Parameters:** 
  - `self` - Instance reference to test class providing access to class-level fixtures and page objects

- **Return Parameter:** None (pytest test method with assertion-based validation)

- **Functional Flow:** 
  1. Asserts PC device name visibility on device details page using `verify_pc_device_name_show_up()`
  2. Navigates to home screen for logged-in users via `click_home_loggedin()`
  3. Executes sign-in workflow using `fc.sign_in()` with username, password, web driver, and `user_icon_click=False` parameter
  4. Verifies user signed-in state by checking top profile icon using `verify_top_profile_icon_signed_in()`
  5. Asserts bell icon visibility using `verify_bell_icon_show_up()`
  6. Clicks bell icon to open notification flyout using `click_bell_icon()`
  7. Clicks notification account section using `click_notification_account()`
  8. Asserts informative unread notifications presence using `verify_informative_unread_notifs()`
  9. Clicks informative read notifications using `click_informative_read_notifs()`
  10. Retrieves notification description using `get_notif_description()`
  11. Logs notification description with info-level logging

- **Assertions:** 
  - PC device name must be present on device details page
  - User must be successfully signed in with profile icon visible within 20 seconds
  - Bell icon must be visible in the UI
  - Informative unread notifications must be present in the notification flyout

- **Boundary Conditions:** 
  - 20-second timeout for sign-in verification
  - Notification content availability dependent on backend notification service state

- **Exception Handling:** None explicitly defined; pytest assertion failures will raise AssertionError with custom failure messages

#### Method Level: test_03_verify_users_can_view_messages_under_read_section_C60339084

- **Scope:** Instance Method

- **Purpose:** Validates that users can view messages under the read section of bell notifications by navigating through notification categories, scrolling to read notifications, verifying both informative and unread notification presence, and retrieving detailed message descriptions

- **Annotation or Markers:** 
  - `@pytest.mark.regression` - Marks test as part of regression test suite

- **Dependencies:** 
  - `self.devices_details_pc_mfe` - Page object for PC device details verification
  - `self.devicesMFE` - Page object for home navigation
  - `self.fc` - FlowContainer for sign-in workflow orchestration
  - `self.profile` - Page object for user authentication state verification
  - `self.device_card` - Page object for bell icon interaction
  - `self.bell_icon` - Page object for notification interactions and verification
  - `self.driver` - Windows automation driver for swipe/scroll actions
  - `logging` - Standard logging module for test execution traceability

- **Module Configurations:** None

- **Input Parameters:** 
  - `self` - Instance reference to test class providing access to class-level fixtures and page objects

- **Return Parameter:** None (pytest test method with assertion-based validation)

- **Functional Flow:** 
  1. Asserts PC device name visibility on device details page using `verify_pc_device_name_show_up()`
  2. Navigates to home screen for logged-in users via `click_home_loggedin()`
  3. Executes sign-in workflow using `fc.sign_in()` with username, password, web driver, and `user_icon_click=False` parameter
  4. Verifies user signed-in state by checking top profile icon using `verify_top_profile_icon_signed_in()`
  5. Asserts bell icon visibility using `verify_bell_icon_show_up()`
  6. Clicks bell icon to open notification flyout using `click_bell_icon()`
  7. Asserts account category visibility in notification flyout using `verify_account_category()`
  8. Verifies shortcuts category presence using `verify_shortcuts_category()`
  9. Clicks notification account section using `click_notification_account()`
  10. Performs downward swipe on "read_text" element using `driver.swipe()` with `direction="down"`
  11. Asserts informative notifications presence using `verify_informative_notifications()`
  12. Asserts informative unread notifications presence using `verify_informative_unread_notifs()`
  13. Clicks informative read notifications using `click_informative_read_notifs()`
  14. Retrieves notification description using `get_notif_description()`
  15. Logs notification description with info-level logging

- **Assertions:** 
  - PC device name must be present on device details page
  - User must be successfully signed in with profile icon visible within 20 seconds
  - Bell icon must be visible in the UI
  - Account category must be visible in bell notification flyout
  - Informative notifications must be found in the notification list
  - Informative unread notifications must be present

- **Boundary Conditions:** 
  - 20-second timeout for sign-in verification
  - Scroll/swipe action requires "read_text" element to be present and scrollable
  - Notification content availability dependent on backend notification service state

- **Exception Handling:** None explicitly defined; pytest assertion failures will raise AssertionError with custom failure messages

#### Method Level: test_04_verify_notifications_after_relaunching_app_C66254937

- **Scope:** Instance Method

- **Purpose:** Validates notification persistence and state management by verifying that both unread and read informative notifications remain accessible after the HPX application is restarted, ensuring proper data persistence across application lifecycle events

- **Annotation or Markers:** 
  - `@pytest.mark.regression` - Marks test as part of regression test suite

- **Dependencies:** 
  - `self.profile` - Page object for user authentication state verification
  - `self.devicesMFE` - Page object for bell icon visibility verification
  - `self.device_card` - Page object for bell icon interaction
  - `self.bell_icon` - Page object for notification interactions and verification
  - `self.fc` - FlowContainer for application restart workflow

- **Module Configurations:** None

- **Input Parameters:** 
  - `self` - Instance reference to test class providing access to class-level fixtures and page objects

- **Return Parameter:** None (pytest test method with assertion-based validation)

- **Functional Flow:** 
  1. Verifies user signed-in state by checking top profile icon using `verify_top_profile_icon_signed_in()`
  2. Asserts bell icon visibility using `verify_bell_icon_show_up()`
  3. Clicks bell icon to open notification flyout using `click_bell_icon()`
  4. Asserts account category visibility in notification flyout using `verify_account_category()`
  5. Verifies shortcuts category presence using `verify_shortcuts_category()`
  6. Clicks notification account section using `click_notification_account()`
  7. Asserts informative unread notifications presence using `verify_informative_unread_notifs()`
  8. Asserts informative read notifications presence using `verify_informative_notifications()`
  9. Restarts myHP application using `fc.restart_myHP()`
  10. Asserts bell icon visibility after relaunch using `verify_bell_icon_show_up()`
  11. Clicks bell icon to reopen notification flyout using `click_bell_icon()`
  12. Clicks notification account section using `click_notification_account()`
  13. Asserts informative unread notifications presence after relaunch using `verify_informative_unread_notifs()`
  14. Asserts informative read notifications presence after relaunch using `verify_informative_notifications()`

- **Assertions:** 
  - User must be successfully signed in with profile icon visible within 20 seconds
  - Bell icon must be visible before application restart
  - Account category must be visible in bell notification flyout before restart
  - Informative unread notifications must be present before restart
  - Informative read notifications must be found before restart
  - Bell icon must be visible after relaunching application
  - Informative unread notifications must be present after relaunching application
  - Informative read notifications must be found after relaunching application

- **Boundary Conditions:** 
  - 20-second timeout for sign-in verification
  - Application restart timing dependent on system performance and application initialization
  - Notification state persistence dependent on backend service and local cache management

- **Exception Handling:** None explicitly defined; pytest assertion failures will raise AssertionError with custom failure messages

---

## PRE-FLIGHT FUNCTION INVENTORY LOG

**Inventory for test_suite_07_bell_notifcations.py:** Found 5 total functions/methods:
1. `class_setup` (fixture)
2. `test_01_verify_close_button_functionality_in_bell_notification_flyout_C60339090`
3. `test_02_verify_users_can_view_unread_messages_C60339083`
4. `test_03_verify_users_can_view_messages_under_read_section_C60339084`
5. `test_04_verify_notifications_after_relaunching_app_C66254937`

---

## Missing Artifacts

None

---

# PRE-FLIGHT FUNCTION INVENTORY LOG

**Inventory for test_suite_08_bell_notifcations.py:** Found 6 total functions:
1. class_setup (fixture)
2. test_01_verify_bell_notifications_device_details_screen_blur_displayed_C60336359
3. test_02_verify_support_on_urgent_info_warning_unread_notifications_C60369962
4. test_03_verify_support_on_urgent_unread_notifications_C60370064
5. test_04_verify_support_on_important_unread_notifications_C60370065
6. test_05_verify_bell_good_to_know_notifications_C60370067

---

# test_suite_08_bell_notifcations.py

## MODULE SUMMARY DETAILS

[MODULE_PURPOSE_START]

This test suite module implements automated regression testing for the bell notification system within the HPX Desktop application. It validates notification UI behaviors including visibility, categorization, interaction patterns, and visual effects across urgent, informative, and warning notification types. The module leverages pytest framework with class-scoped fixtures to orchestrate Windows desktop automation and web session management for comprehensive notification feature verification.

[MODULE_PURPOSE_END]

## 1. File Header (Module-Level Documentation)

- **Primary Responsibility:** Automated regression testing of bell notification functionality in HPX Desktop application, validating notification display, categorization, user interaction workflows, and UI state management across multiple notification severity levels.

- **Dependencies:** 
  - `pytest` - Test framework and fixture management
  - `logging` - Runtime logging infrastructure
  - `SAF.misc.saf_misc` - SAF framework utility functions for JSON operations
  - `MobileApps.libs.ma_misc.ma_misc` - Mobile apps utility library for path resolution
  - `MobileApps.resources.const.windows.const.HPX_ACCOUNT` - Account configuration constants
  - `MobileApps.libs.flows.windows.hpx_rebranding.flow_container.FlowContainer` - Flow orchestration container for page object access

- **Module Configuration:** 
  - `pytest.app_info = "DESKTOP"` - Application platform identifier
  - `pytest.set_info = "HPX"` - Product identifier for HPX application
  - Class-level fixtures: `class_setup_fixture_ota_regression`, `function_setup_clear_sign_out`

## 2. Class Documentation: Test_Suite_08_Bell_Notifications

- **Role:** Test suite container class organizing bell notification regression test cases with shared fixture initialization and page object access patterns.

- **Purpose:** Encapsulates test execution context for bell notification feature validation, managing test lifecycle through pytest fixtures, providing centralized access to page objects (devicesMFE, bell_icon, device_card), and coordinating authentication state across test methods.

### Fixture: class_setup

- **Scope:** Class

- **Purpose:** Initializes test environment dependencies including Windows driver, web session, flow container, page objects, and loads HPID account credentials from configuration files for authentication workflows.

- **Annotation or Markers:** 
  - `@pytest.fixture(scope="class", autouse=True)`

- **Dependencies:** 
  - `windows_test_setup` - Windows desktop automation driver fixture
  - `utility_web_session` - Web browser session fixture
  - `FlowContainer` - Flow orchestration container
  - `saf_misc.load_json` - JSON configuration loader
  - `ma_misc.get_abs_path` - Absolute path resolver
  - `HPX_ACCOUNT.account_details_path` - Account credentials file path constant

- **Parameter:** 
  - `cls` - Class reference for setting class-level attributes
  - `request` - Pytest request object for accessing test context and class instance
  - `windows_test_setup` - Injected Windows automation driver instance
  - `utility_web_session` - Injected web browser session instance

- **Set-up Action:** 
  1. Assigns class reference to `cls` variable
  2. Binds `windows_test_setup` driver to `request.cls.driver`
  3. Binds `utility_web_session` to `request.cls.web_driver`
  4. Instantiates `FlowContainer` with driver and assigns to `request.cls.fc`
  5. Terminates any running HPX processes via `fc.kill_hpx_process()`
  6. Extracts page objects from flow dictionary: `devicesMFE`, `css`, `device_card`, `bell_icon`, `profile`
  7. Clears stored web password credentials via `fc.web_password_credential_delete()`
  8. Loads HPID username from JSON configuration file
  9. Loads HPID password from JSON configuration file

- **State Management:** 
  - `cls.driver` - Windows automation driver instance
  - `cls.web_driver` - Web browser session instance
  - `cls.fc` - FlowContainer orchestration object
  - `cls.devicesMFE` - Devices MFE page object
  - `cls.css` - CSS page object
  - `cls.device_card` - Device card page object
  - `cls.bell_icon` - Bell icon page object
  - `cls.profile` - Profile page object
  - `cls.user_name` - HPID username credential
  - `cls.password` - HPID password credential

### Method Level: test_01_verify_bell_notifications_device_details_screen_blur_displayed_C60336359

- **Scope:** Instance Method

- **Purpose:** Validates that opening the bell notification panel applies a background blur effect to the device details screen, ensuring proper visual layering and focus management in the notification UI.

- **Annotation or Markers:** 
  - `@pytest.mark.regression`

- **Dependencies:** 
  - `self.fc.sign_in` - Authentication flow method
  - `self.devicesMFE.verify_bell_icon_show_up` - Bell icon visibility verification
  - `self.device_card.click_bell_icon` - Bell icon interaction
  - `self.bell_icon.click_notification_account` - Account notification category selection
  - `self.bell_icon.verify_background_blur` - Background blur effect verification

- **Module Configurations:** None

- **Input Parameters:** 
  - `self` - Test class instance providing access to fixtures and page objects

- **Return Parameter:** None (pytest test method)

- **Functional Flow:** 
  1. Authenticates user via `sign_in` with username, password, and web driver
  2. Asserts bell icon visibility on device MFE screen with failure message "bell icon is not present"
  3. Clicks bell icon to open notification panel
  4. Clicks notification account category to navigate to account notifications
  5. Asserts background blur effect is applied with failure message "background blur is not displayed on device details screen"

- **Assertions:** 
  - Bell icon must be visible on the device MFE screen
  - Background blur effect must be displayed when notification panel is opened

- **Boundary Conditions:** 
  - Requires successful user authentication
  - Depends on bell icon being rendered in UI
  - Assumes notification panel opens successfully

- **Exception Handling:** None explicitly implemented; pytest assertion failures will raise AssertionError with custom messages

### Method Level: test_02_verify_support_on_urgent_info_warning_unread_notifications_C60369962

- **Scope:** Instance Method

- **Purpose:** Validates the presence and correct display of all three notification severity types (urgent, informative, warning) in unread state within the account notification category, ensuring comprehensive notification type support.

- **Annotation or Markers:** 
  - `@pytest.mark.regression`

- **Dependencies:** 
  - `self.fc.sign_in` - Authentication flow method
  - `self.devicesMFE.verify_bell_icon_show_up` - Bell icon visibility verification
  - `self.device_card.click_bell_icon` - Bell icon interaction
  - `self.bell_icon.verify_account_category` - Account category verification
  - `self.bell_icon.verify_shortcuts_category` - Shortcuts category verification
  - `self.bell_icon.click_notification_account` - Account notification category selection
  - `self.bell_icon.verify_urgent_unread_notifs` - Urgent notification verification
  - `self.bell_icon.verify_informative_unread_notifs` - Informative notification verification
  - `self.bell_icon.verify_warning_unread_notifs` - Warning notification verification

- **Module Configurations:** None

- **Input Parameters:** 
  - `self` - Test class instance providing access to fixtures and page objects

- **Return Parameter:** None (pytest test method)

- **Functional Flow:** 
  1. Authenticates user via `sign_in` with username, password, and web driver
  2. Asserts bell icon visibility with failure message "bell icon is not present"
  3. Clicks bell icon to open notification panel
  4. Verifies account category is displayed
  5. Verifies shortcuts category is displayed
  6. Clicks notification account category to filter account notifications
  7. Asserts urgent unread notifications are present with failure message "urgent unread msgs not found"
  8. Asserts informative unread notifications are present with failure message "informative unread msgs not found"
  9. Asserts warning unread notifications are present with failure message "warning unread msgs not found"

- **Assertions:** 
  - Bell icon must be visible
  - Urgent unread notifications must be displayed
  - Informative unread notifications must be displayed
  - Warning unread notifications must be displayed

- **Boundary Conditions:** 
  - Requires successful authentication
  - Assumes test account has unread notifications of all three severity types
  - Depends on notification panel rendering correctly

- **Exception Handling:** None explicitly implemented; pytest assertion failures will raise AssertionError with custom messages

### Method Level: test_03_verify_support_on_urgent_unread_notifications_C60370064

- **Scope:** Instance Method

- **Purpose:** Validates urgent notification interaction behavior including ellipsis menu access, delete option disabled state for urgent notifications, and mark-as-read functionality, ensuring critical notifications cannot be accidentally deleted.

- **Annotation or Markers:** 
  - `@pytest.mark.regression`

- **Dependencies:** 
  - `self.fc.sign_in` - Authentication flow method
  - `self.devicesMFE.verify_bell_icon_show_up` - Bell icon visibility verification
  - `self.device_card.click_bell_icon` - Bell icon interaction
  - `self.bell_icon.verify_account_category` - Account category verification
  - `self.bell_icon.click_notification_account` - Account notification category selection
  - `self.bell_icon.verify_urgent_unread_notification_ellipsis` - Urgent notification ellipsis verification
  - `self.bell_icon.click_urgent_unread_notification_ellipsis` - Urgent notification ellipsis interaction
  - `self.bell_icon.verify_delete_disabled_urgent_unread_notifs` - Delete disabled state verification
  - `self.bell_icon.verify_notifs_and_mark_as_read` - Mark as read functionality verification

- **Module Configurations:** None

- **Input Parameters:** 
  - `self` - Test class instance providing access to fixtures and page objects

- **Return Parameter:** None (pytest test method)

- **Functional Flow:** 
  1. Authenticates user via `sign_in` with username, password, and web driver
  2. Asserts bell icon visibility with failure message "bell icon is not present"
  3. Clicks bell icon to open notification panel
  4. Verifies account category is displayed
  5. Clicks notification account category to filter account notifications
  6. Asserts urgent unread notification ellipsis menu is present with failure message "urgent unread notification ellipsis not found"
  7. Clicks urgent unread notification ellipsis to reveal dropdown menu
  8. Asserts delete option is disabled for urgent notifications with failure message "delete disabled urgent unread notifs not found"
  9. Verifies mark-as-read functionality for notifications

- **Assertions:** 
  - Bell icon must be visible
  - Urgent unread notification ellipsis menu must be present
  - Delete option must be disabled for urgent unread notifications

- **Boundary Conditions:** 
  - Requires successful authentication
  - Assumes test account has urgent unread notifications
  - Urgent notifications must have special delete-disabled behavior

- **Exception Handling:** None explicitly implemented; pytest assertion failures will raise AssertionError with custom messages

### Method Level: test_04_verify_support_on_important_unread_notifications_C60370065

- **Scope:** Instance Method

- **Purpose:** Validates informative notification interaction workflow including ellipsis menu access, dropdown reveal behavior, and availability of both mark-as-read and delete options for non-urgent notifications.

- **Annotation or Markers:** 
  - `@pytest.mark.regression`

- **Dependencies:** 
  - `self.fc.sign_in` - Authentication flow method
  - `self.devicesMFE.verify_bell_icon_show_up` - Bell icon visibility verification
  - `self.device_card.click_bell_icon` - Bell icon interaction
  - `self.bell_icon.verify_account_category` - Account category verification
  - `self.bell_icon.click_notification_account` - Account notification category selection
  - `self.bell_icon.verify_informative_unread_notification_ellipsis` - Informative notification ellipsis verification
  - `self.bell_icon.click_informative_unread_notification_ellipsis` - Informative notification ellipsis interaction
  - `self.bell_icon.verify_notification_dropdown_revealed` - Dropdown visibility verification
  - `self.bell_icon.verify_dropdown_mark_as_read_option_present` - Mark as read option verification
  - `self.bell_icon.verify_dropdown_delete_option_present` - Delete option verification

- **Module Configurations:** None

- **Input Parameters:** 
  - `self` - Test class instance providing access to fixtures and page objects

- **Return Parameter:** None (pytest test method)

- **Functional Flow:** 
  1. Authenticates user via `sign_in` with username, password, and web driver
  2. Asserts bell icon visibility with failure message "bell icon is not present"
  3. Clicks bell icon to open notification panel
  4. Verifies account category is displayed
  5. Clicks notification account category to filter account notifications
  6. Asserts informative unread notification ellipsis menu is present with failure message "informative unread notification ellipsis not found"
  7. Clicks informative unread notification ellipsis to reveal dropdown menu
  8. Asserts notification dropdown is revealed with failure message "notification drop down invisible"
  9. Asserts mark-as-read option is present in dropdown with failure message "mark as read option not visible in dropdown"
  10. Asserts delete option is present in dropdown with failure message "delete option not visible in dropdown"

- **Assertions:** 
  - Bell icon must be visible
  - Informative unread notification ellipsis menu must be present
  - Notification dropdown must be revealed after clicking ellipsis
  - Mark-as-read option must be visible in dropdown
  - Delete option must be visible in dropdown

- **Boundary Conditions:** 
  - Requires successful authentication
  - Assumes test account has informative unread notifications
  - Informative notifications must allow both mark-as-read and delete actions

- **Exception Handling:** None explicitly implemented; pytest assertion failures will raise AssertionError with custom messages

### Method Level: test_05_verify_bell_good_to_know_notifications_C60370067

- **Scope:** Instance Method

- **Purpose:** Validates warning notification interaction workflow including ellipsis menu access, dropdown reveal behavior, and availability of both mark-as-read and delete options for good-to-know warning notifications.

- **Annotation or Markers:** 
  - `@pytest.mark.regression`

- **Dependencies:** 
  - `self.fc.sign_in` - Authentication flow method
  - `self.devicesMFE.verify_bell_icon_show_up` - Bell icon visibility verification
  - `self.device_card.click_bell_icon` - Bell icon interaction
  - `self.bell_icon.verify_account_category` - Account category verification
  - `self.bell_icon.click_notification_account` - Account notification category selection
  - `self.bell_icon.verify_warning_unread_notification_ellipsis` - Warning notification ellipsis verification
  - `self.bell_icon.click_warning_unread_notification_ellipsis` - Warning notification ellipsis interaction
  - `self.bell_icon.verify_notification_dropdown_revealed` - Dropdown visibility verification
  - `self.bell_icon.verify_dropdown_mark_as_read_option_present` - Mark as read option verification
  - `self.bell_icon.verify_dropdown_delete_option_present` - Delete option verification

- **Module Configurations:** None

- **Input Parameters:** 
  - `self` - Test class instance providing access to fixtures and page objects

- **Return Parameter:** None (pytest test method)

- **Functional Flow:** 
  1. Authenticates user via `sign_in` with username, password, and web driver
  2. Asserts bell icon visibility with failure message "bell icon is not present"
  3. Clicks bell icon to open notification panel
  4. Verifies account category is displayed
  5. Clicks notification account category to filter account notifications
  6. Asserts warning unread notification ellipsis menu is present with failure message "warning unread notification ellipsis not found"
  7. Clicks warning unread notification ellipsis to reveal dropdown menu
  8. Asserts notification dropdown is revealed with failure message "notification drop down invisible"
  9. Asserts mark-as-read option is present in dropdown with failure message "mark as read option not visible in dropdown"
  10. Asserts delete option is present in dropdown with failure message "delete option not visible in dropdown"

- **Assertions:** 
  - Bell icon must be visible
  - Warning unread notification ellipsis menu must be present
  - Notification dropdown must be revealed after clicking ellipsis
  - Mark-as-read option must be visible in dropdown
  - Delete option must be visible in dropdown

- **Boundary Conditions:** 
  - Requires successful authentication
  - Assumes test account has warning unread notifications
  - Warning notifications must allow both mark-as-read and delete actions

- **Exception Handling:** None explicitly implemented; pytest assertion failures will raise AssertionError with custom messages

---

## Missing Artifacts

None