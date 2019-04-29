# Contributing to hl7-at-fhir-profiles

The following is a set of guidelines for contributing to the hl7-at-fhir-profiles project and its packages,
which are hosted in the HL7-Austria organization on GitHub. These are mostly guidelines, not rules. Use your best judgment,
and feel free to propose changes to this document in a pull request.

<!-- TOC -->

- [Contributing to hl7-at-fhir-profiles](#contributing-to-hl7-at-fhir-profiles)
    - [Code of Conduct](#code-of-conduct)
    - [How Can I Contribute?](#how-can-i-contribute)
        - [Reporting Bugs](#reporting-bugs)
            - [Before Submitting A Bug Report](#before-submitting-a-bug-report)
            - [How Do I Submit A (Good) Bug Report?](#how-do-i-submit-a-good-bug-report)
        - [Request New Profiles/Extensions](#request-new-profilesextensions)
            - [How Do I Submit a (Good) Enhancement](#how-do-i-submit-a-good-enhancement)
    - [Issue and Pull Request Labels](#issue-and-pull-request-labels)
    - [Style guides](#styleguides)
        - [Git Commit Messages](#git-commit-messages)
        - [Naming Conventions](#naming-conventions)
    - [Additional Information](#additional-information)
    - [Support](#support)

<!-- /TOC -->

## Code of Conduct

This project and everyone participating in it is governed by HL7 Austria FHIR Technical Committee. By participating, you are expected to uphold this code. Please report unacceptable behavior to tcfhir@hl7.at.

## How Can I Contribute?

- TBD (depends on results from issue #14)

### Reporting Bugs

- TBD

#### Before Submitting A Bug Report

- TBD

#### How Do I Submit A (Good) Bug Report?

- TBD

### Request New Profiles/Extensions
In order to request a new Profile or an Extension either create an issue with the label `enhancement` or email [tc-fhir](mailto:tcfhir@hl7.at)
Use the issue to describe the intended use case and if applicable state some examples.

#### How Do I Submit a (Good) Enhancement

- TBD


## Issue and Pull Request Labels

| Label name | Description |
| --- | --- |
| `discussion` | needs to be discussed in a meeting of the technical committee FHIR in HL7 Austria |
| `review` | a solution to an open issue is provided, however the solution has to be reviewed before closing respective issue |
| `bug` | marks a bug in the implementation |
| `enhancement` | propose a new feature or a change in an existing profile/extension |
| `blocked` | issues marked with `blocked` are dependent on other issue still in progress |
| `hot` | marks issues with high priority, these are only assigned by the HL7 Austria TC-FHIR, any invalid use on issues will be removed without discussion |


## Style guides

### Git Commit Messages
A commit message must start with the corresponding ticket number in GitHub (#TICKETNUMBER) each commit message must have a description which should be in present tense and use imperative voice

### Naming Conventions

In general the HL7 [FHIR naming conventions](http://wiki.hl7.org/index.php?title=FHIR_Guide_to_Designing_Resources#Naming_Rules_.26_Guidelines) apply. Essentially these conventions ask for **consistency** and **precision** (i.e. minimizing ambiguity, while ensuring the meaning is easily understood) when naming fields, resources or operations.

Most of these guidelines are suggestions, except the following rules that *must* be followed:
-  be lowerCamelCase for elements, UpperCamelCase for resources, be lowercase for operations
-  be U.S. English (spelled correctly!)
-  be expressed as a noun, with a preceding adjective where necessary to clarify the semantics and to make unique
-  not make use of trade-marked terms

#### Profile Naming conventions

A profile follows a prefix pattern, meaning that a name from left to right goes from specific to generic. It uses UpperCamelCase.

**ProfileName** = [*Realm*-] *Use* , *ParentProfile*
**Realm** = Is this profile supposed to be used in a realm? Then use the **countryCode**[^ISO3166-3]
**Use** = What is this profile used for? **UpperCamelCase**
**ParentProfile** =  Which profile does this profile extend from? **UpperCamelCase**

[^ISO3166-3]: country codes are [ISO 3166-3](https://www.iso.org/iso-3166-country-codes.html) in the Alpha-2 code format, all lowercase.

Example: Patient used in Austria, for ELGA.
```
Realm = Austria -> at- (country code)
Use = ELGA -> Elga
ParentProfile = Patient -> Patient
at-ElgaPatient
```

Example: Patient minimal information for Patient Summary in any Realm
```
Realm = any -> no prefix
Use = Patient Summary -> PatientSummary
ParentProfile = Patient -> Patient
PatientSummaryPatient
```

#### Extension Naming conventions

An extension follows a suffix pattern, meaning that a name from left to right goes from generic to specific. It uses lowerCamelCase.

**ExtensionName** = [*ProfileItIsFor*], {*FieldWithChildrenItIsIn*}, *FieldItAdds*
**ProfileItIsFor** = Either Base Profile or **Profile** previously defined (optional if extension can occur anywhere -> Ex. NullFlavor), without the Realm.
**FieldWithChildrenItIsIn** = Optional and Repeating, represents the **hierarchy** where the extension is to be used (optionally if it can occur anywhere).
**FieldItAdds** = **unique naming** for field

Example: Extra patient field for "Sozialversicherungsnummer"
```
Profile = at-Patient -> patient
FieldWithChildrenitIsIn = identifier -> Identifier
FieldItAdds = Sozialversicherungsnummer -> Ssnr (or SocialSecurityNumber)
patientIdentifierSsnr
```

Example: Extra field strength in Composition, for Allergies of a PatientSummary
```
Profile = PatientSummaryComposition -> patientSummaryComposition
FieldWithChildrenitIsIn = Section Patient - Section Allergies  -> SectionPatientSubsectionAllergies (here we clarify which section, instead of writing SectionSection)
FieldItAdds = Strength -> Strength
patientSummaryCompositionSectionPatientSectionAllergiesStrength
```

Example: Field nullFlavor that can be added anywhere
```
Profile = none -> ""
FieldWithChildrenitIsIn = any -> ""
FieldItAdds = nullFlavor -> nullFlavor
nullFlavor
```

## Additional Information

- TBD (add mail addresses and contact information)

## Support
We actively monitor the issues coming in through the GitHub repository at https://github.com/HL7Austria/hl7-at-fhir-profiles/issues. You are welcome to register your bugs and feature suggestions there. For questions and broader discussions, we use the TC-Austria channel on [Zulip](https://chat.fhir.org).
