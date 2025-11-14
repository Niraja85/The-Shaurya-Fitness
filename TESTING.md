# The shaurya Fitness Testing
[Return to the README](README.md)

## Table of Contents

- [The Shaurya Fitness Testing](#the-shaurya-fitness-testing)
  - [Table of Contents](#table-of-contents)
- [Performance](#performance)
  - [Google's Lighthouse Performance](#googles-lighthouse-performance)
- [Accessibility](#accessibility)
  - [Accessibility Validation](#accessibility-validation)
- [Code Validation](#code-validation)
  - [HTML Validation](#html-validation)
  - [CSS Validation](#css-validation)
  - [JS Validation](#js-validation)
  - [PEP8 Validation](#pep8-validation)
- [Testing](#testing)
  - [Manual Testing (BDD)](#manual-testing-bdd)
  - [Automated Testing (TDD)](#automated-testing-tdd)
- [Bugs](#bugs)

# Performance

## Google's Lighthouse Performance

[Google Lighthouse](https://developers.google.com/web/tools/lighthouse) was used to test the performance of the website. There are a couple of issues due to Bootstrap, Stripe and general Heroku slowness.

<details><summary>Home</summary>
<img src="docs/testing/lighthouse/Home-LH.png" >
</details>
<details><summary>Register</summary>
<img src="docs/testing/lighthouse/Register-LH.png">
</details>
<details><summary>Products</summary>
<img src="docs/testing/lighthouse/Products-LH.png">
</details>
<details><summary>Product-Detail</summary>
<img src="docs/testing/lighthouse/Product-detail-LH.png">
</details>
<details><summary>FAQ</summary>
<img src="docs/testing/lighthouse/FAQ-LH.png">
</details>
<details><summary>Contact</summary>
<img src="docs/testing/lighthouse/Contact-LH.png">
</details>
<details><summary>Profile</summary>
<img>
</details>
<details><summary>Checkout</summary>
<img>
</details>
<details><summary>Order Confirmation</summary>
<img>
</details>
<details><summary>Privacy Policy</summary>
<img src="docs/testing/lighthouse/Privacy-policy-LH.png">
</details>

*Go back to the [top](#table-of-contents)*

---

# Accessibility

## Accessibility Validation

The [WAVE WebAIM web accessibility evaluation tool](https://wave.webaim.org/) was used to ensure the website met high accessibility standards. The 2 errors seen are beacuse of not using labels for form-control which is for all pages and a contrast error for signin on register page which is a default in allauth account.

<details><summary>Home-Wave</summary>
<img src="docs/testing/wave/home-wave.png">
</details>
<details><summary>Register</summary>
<img src="docs/testing/wave/register-wave.png">
</details>
<details><summary>Products</summary>
<img src="docs/testing/wave/Products-wave.png">
</details>
<details><summary>Product Details</summary>
<img src="docs/testing/wave/Product-dd.png">
</details>
<details><summary>Faq</summary>
<img src="docs/testing/wave/FAQ-wave.png">
</details>
<details><summary>Contact</summary>
<img src="docs/testing/wave/Contact-wave.png">
</details>
<details><summary>Profile</summary>
<img src="">
</details>
<details><summary>Checkout</summary>
<img src="">
</details>
<details><summary>Order Confirmation</summary>
<img src="">
</details>
<details><summary>Privacy policy</summary>
<img src="docs/testing/wave/Privacy-policy-wave.png">
</details>

*Go back to the [top](#table-of-contents)*

## HTML Validation

The [W3C Markup Validation Service](https://validator.w3.org/) was used to validate the HTML of the website.

<details><summary>Home</summary>
<img src="">
</details>

## CSS Validation

The [W3C Jigsaw CSS Validation Service](https://jigsaw.w3.org/css-validator/) was used to validate the CSS of the website. The CSS passes with 0 errors.

![CSS validation](docs/testing/validation/CSS-validator.png)

*Go back to the [top](#table-of-contents)*













