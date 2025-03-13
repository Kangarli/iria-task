Feature: Dynamic Controls

  Scenario: Check and uncheck checkbox
    Given Navigate to "https://practice.expandtesting.com/dynamic-controls"
    When Check the checkbox
    When Uncheck the checkbox
    When Remove checkbox button
    Then Should see the checkbox removed

  Scenario: Enable and disable input field
    Given Navigate to "https://practice.expandtesting.com/dynamic-controls"
    When Enable the input field
    Then Should see the input field enabled
    When Disable the input field
    Then Should see the input field disabled