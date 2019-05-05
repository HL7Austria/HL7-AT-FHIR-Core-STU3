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
There are multiple ways of how one can contribute to the efforts of the TC FHIR from HL7 Austria:
- Active participation on the HL7 Austria TC FHIR conference calls 
- Creating feature requests or bug reports on github
- For questions and broader discussions, use the TC-Austria channel on [Zulip](https://chat.fhir.org)

### Reporting Bugs

- For reporting bugs the TC FHIR created an issue template for github, it can be found [here] (https://github.com/HL7Austria/hl7-at-fhir-profiles/blob/master/.github/ISSUE_TEMPLATE/hl7-at--bug-report.md) and is available automatically if a new issue is created.

#### Before Submitting A Bug Report

- Please make sure if there isn't already an open or closed github issue in the HL7 Austria repository for the problem that you are facing. If the problem isn't directly related to HL7 Austria FHIR profiles or extensions but is more general, please also make sure that it hasn't be dealt with on the official [FHIR Chat] (https://chat.fhir.org).

#### How Do I Submit A (Good) Bug Report?

- In order to create a good bug report you will be asked to fill out a couple of questions concerning your bug, which are necessary for the TC FHIR in order to address the stated problem most effectively.  

| Bug Criteria | Description |
| --- | --- |
| Real Submitter | Who ist the real submitter, in case the creation of the issue was done by proxy. |
| Resource(s)/Profiles incl. Version | Which resources or profiles are affected by this bug report? |
| Priority | Priority of this bug report (Blocker, Critical, Major, Minor, Trivial). |
| Describe the bug | A clear and concise description of what the bug is. |
| To Reproduce | Steps to reproduce the behavior. |
| Expected behavior | A clear and concise description of what you expected to happen. |

### Request New Profiles/Extensions
- For requesting new Profiles or Extensions or features in general the TC FHIR created a feature request template for github, it can be found [here] (https://github.com/HL7Austria/hl7-at-fhir-profiles/blob/master/.github/ISSUE_TEMPLATE/hl7-at--feature-request.md) and is available automatically if a new issue is created.
- Alternatively a new Profile or an Extension can be requested by sending an email to [tc-fhir](mailto:office@hl7.at)
- Use the issue to describe the intended use case and if applicable state some examples.

#### How Do I Submit a (Good) Enhancement

- In order to create a good feature request you will be asked to fill out a couple of questions concerning your request, which are necessary for the TC FHIR in order to address the desired feature most effectively.

| Request Criteria | Description |
| --- | --- |
| Real Submitter | Who ist the real submitter, in case the creation of the issue was done by proxy. |
| Resource(s)/Profiles incl. Version | Which resources or profiles are affected by this bug report? |
| Priority | Priority of this request (Blocker, Critical, Major, Minor, Trivial). |
| Is your feature request related to a problem? Please describe. | A clear and concise description of what the problem is. |
| Describe the solution you'd like | A clear and concise description of what you want to happen. |
| Describe alternatives you've considered | A clear and concise description of any alternative solutions or features you've considered. |

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

### Documentation of decisions on issues
HL7 International is documenting the decision it makes on issues in it's ticket tracker tool gforge. For HL7 Austria we've decided to use their way of documenting decisions for our github issues as well. Since github issues don't provide any forms to fill out certain attributes for an issue it was decided to document the decision criteria as a comment for each issue with the following attributes:
- **Motion:** Exact wording of the motion which will be moved.
- **Change Type:** describes the severity of the proposed change -> HL7 International categories (Any, None, Non-substantive, Compatible-substantive, Non-compatible)
- **(Ballot) Resolution:** final resolution -> HL7 International (ballot) categories (Persuasive, Persuasive with Mod, ...)
- **Mover/Seconder: For-Against-Abstain:**

### Information if an issue is derived from a Ballot
Since github issues cannot be created automatically out of HL7 Austria Ballot results, it was decided to document the Ballot information as a comment for each relevant issue with the following attributes:
- **Ballot Info:** from which ballot it came from

- **Ballot Weight:** categories (and codes) from HL7 Austria ballots for a comment
	- NEG-S (negative, serious), NEG-G (negative, minor), Z-V (approval with proposal), Z-T (approval - typo), Z-F (approval with question), Z-K (approval with comment)

## Support
We actively monitor the issues coming in through the GitHub repository at https://github.com/HL7Austria/hl7-at-fhir-profiles/issues. You are welcome to register your bugs and feature suggestions there. For questions and broader discussions, we use the TC-Austria channel on [Zulip](https://chat.fhir.org).
