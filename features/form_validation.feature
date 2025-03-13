Feature: Form Submission Validation

  Scenario: Submit the form with valid data
    Given Navigate to "https://practice.expandtesting.com/form-validation"
    When Fill the form with valid data
    And Submit the form
    Then Should see a succes mesage

  Scenario: Submit the form with invalid data
    Given Navigate to "https://practice.expandtesting.com/form-validation"
    When Fill the form with invalid data
    And Submit the form
    Then Should see appropriate error messages