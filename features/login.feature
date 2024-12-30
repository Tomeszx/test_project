Feature: Login to service
  """ This feature will check if user will be able to login to service with different credentials. """

  Scenario: Login to service with correct credentials
    Given the website "https://practicetestautomation.com/practice-test-login/" has been opened
      And the login page is fully loaded
    When i fill username field with 'student'
      And i fill password field with 'Password123'
      And i click to login button
     Then the url ends with '/logged-in-successfully/'
      And the logout button is clickable
      And the header title is 'Logged In Successfully'


  Scenario Outline: Login to service with incorrect login only
    """
    Currently there is a bug, so the test will fail. Someone can check which logins are in database.
    Each time the wrong username will be typed it would say that it's wrong.
    """
    Given the website "https://practicetestautomation.com/practice-test-login/" has been opened
      And the login page is fully loaded
     When i fill username field with '<username>'
      And i click to login button
     Then the login error message is displayed with 'Your password is invalid!'

    Examples:
      | username             |
      | student              |
      | not_existing_student |

  Scenario: Login to service with only password
    Given the website "https://practicetestautomation.com/practice-test-login/" has been opened
      And the login page is fully loaded
     When i fill password field with 'some_password'
      And i click to login button
     Then the login error message is displayed with 'Your username is invalid!'

  Scenario Outline: Login to service with invalid credentials
    Given the website "https://practicetestautomation.com/practice-test-login/" has been opened
      And the login page is fully loaded
     When i fill username field with '<username_value>'
      And i fill password field with '<password_value>'
      And i click to login button
     Then the user is still on login page
      And the login error message is displayed with 'Your username is invalid!'

    Examples:
      | username_value | password_value |
      | admin          | admin          |
      | 123            | 123            |
      | \\\            | \\\            |
      | &\.\           | ...            |
