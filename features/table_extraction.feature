Feature: Form Submission Validation

    Scenario: Extract and validate column values
        Given Navigate to "https://practice.expandtesting.com/tables"
        When Extract values from the "Last Name" column
        Then Validate the extracted values are ["Smith", "Bach", "Doe", "Conway"]

    Scenario: Verify row count before and after an action
        Given Navigate to "https://practice.expandtesting.com/tables"
        When Count the rows in the table
        And Perform a "Delete" action on the first row
        Then Verify the row count is reduced by 1 after delete

    Scenario: Ensure correct sorting order (ascending/descending)
        Given Navigate to "https://practice.expandtesting.com/tables"
        When Click the "Last Name" column header to sort in ascending order
        Then Verify the rows are sorted in ascending order by "Last Name"
        When Click the "Last Name" column header again to sort in descending order
        Then Verify the rows are sorted in descending order by "Last Name"
