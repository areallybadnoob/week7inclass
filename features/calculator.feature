Feature: Scientific Calculator
  As a user
  I want to perform basic and scientific calculations
  So that I can get accurate results for mathematical operations

  Scenario: Perform addition of two numbers
    Given the calculator is open
    When I add 5 and 3
    Then the result should be 6

  Scenario: Perform subtraction of two numbers
    Given the calculator is open
    When I subtract 10 from 7
    Then the result should be -3

  Scenario: Perform multiplication of two numbers
    Given the calculator is open
    When I multiply 4 and 6
    Then the result should be 24

  Scenario: Perform division of two numbers
    Given the calculator is open
    When I divide 15 by 3
    Then the result should be 5

  Scenario: Division by zero
    Given the calculator is open
    When I divide 10 by 0
    Then I should see an error message "Division by zero is not allowed."

  Scenario: Calculate the cosine of a number
    Given the calculator is open
    When I calculate the cosine of 0
    Then the result should be 1

  Scenario: Calculate the sine of a number
    Given the calculator is open
    When I calculate the sine of 0
    Then the result should be 0

  Scenario: Calculate the tangent of a number
    Given the calculator is open
    When I calculate the tangent of 0
    Then the result should be 0

  Scenario: Undefined tangent value
    Given the calculator is open
    When I calculate the tangent of 90 degrees (π/2 radians)
    Then I should see an error message "Tangent is undefined for this input."
