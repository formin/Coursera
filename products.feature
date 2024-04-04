# features/products.feature
Feature: Product management

  Scenario: List all products
    Given I have product data
    When I request all products
    Then I should receive all products

  Scenario: Search product by name
    Given I have product data
    When I search for a product by name
    Then I should receive products matching the name
