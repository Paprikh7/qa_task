Feature: As a user,  i want to be able to log in and access the account page

  Scenario: Given a user, when i fill login form with valid credentials,
  i can access account page when i submit the form
    Given the login page is open
    When i fill "username" on Login page
    And i click "next" button on the login page
    And i fill "password" on Login page
    And i click "submit" button on the login page
    And i click "stay signed no" button on the login page
    And navigate to mailbox
    And i click on button "new mail" on the mail page
    And i click on button "address book" on the mail page
    And i click on button "my contacts" on the mail page
    And i click on button "add person" on the mail page
    And i click on button "save added person" on the mail page
    And i click on button "add attachment" on the mail page
    And upload a attachment
    And i fill "subject" on mail page with "test"
    And i click on button "send mail" on the mail page
    Then i open first mail
    And i check if attachment is visible in the mail
    And User logout