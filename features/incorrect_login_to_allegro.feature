Feature: Login to allegro
  """ This feature will check if user will be able to login to Allegro service with incorrect credentials. """

  Scenario: Login to allegro with only login
    Given the website "https://allegro.pl/logowanie" has been opened
      And the cookie consents modal has been accepted
     When i fill username field with "<username_value>"
      And i click to login button
     Then the empty password field appears

  Scenario: Login to allegro with only password
    Given the website "https://allegro.pl/logowanie" has been opened
      And the cookie consents modal has been accepted
     When i fill password field with "<password_value>"
      And i click to login button
     Then the empty username field appears

  Scenario Outline: Login to allegro with invalid credentials
    Given the website "https://allegro.pl/logowanie" has been opened
      And the cookie consents modal has been accepted
     When i fill username field with "<username_value>"
      And i fill password field with "<password_value>"
     Then the user is still on login page

    Examples:
      | username_value | password_value |
      | admin          | admin          |
      | 123            | 123            |
      | \\\            | \\\            |
      | &\.\           | ...            |
