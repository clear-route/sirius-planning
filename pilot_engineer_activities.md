# Defined Lower-Level Activities for Pilot Engineers (First 6 Months)

## Engineer 1: Central UAT Test Case Identification & Migration

**Goal:** Transform manual UAT by identifying critical business scenarios, migrating them to BDD (ReqNRoll/Playwright), and establishing an automation-first UAT strategy.

**Key Activities (Phased: Discovery & Planning; Migration & Automation; Refinement & Reporting):**

1.  **Deep Dive into Existing UAT Processes & Test Assets:**
    *   Liaise with business teams, UAT coordinators, and product owners to collect all existing UAT documentation.
    *   Shadow current UAT execution sessions to understand manual effort and business context.
2.  **Identify & Prioritize UAT Scenarios for Automation:**
    *   Analyze UAT test cases and historical defect data to identify high-value, repetitive, business-critical scenarios.
    *   Collaborate with stakeholders to select a pilot set of UAT scenarios (including BVT candidates).
3.  **Master BDD Tooling & Methodology:**
    *   Undertake training and self-learning on BDD principles, Gherkin, ReqNRoll, and Playwright.
4.  **Convert Selected UAT Scenarios to BDD (Gherkin):**
    *   Rewrite prioritized UAT scenarios as clear Gherkin (.feature) files.
    *   Conduct workshops (Three Amigos) to validate BDD scenarios.
5.  **Develop Automated Test Scripts using Playwright:**
    *   Implement step definitions for Gherkin scenarios using Playwright.
    *   Incorporate best practices for test data management and mocking (with Eng. Practices Eng.).
6.  **Setup & Test Execution in DT2 Environment:**
    *   Collaborate ensure automated UAT scripts can be executed in the DT2 environment.
    *   Perform initial test runs in DT2 and stabilize.
7.  **Iterate and Refine Automated UAT Suite:**
    *   Continuously refine and stabilize automated UAT test scripts based on results and feedback.
    *   Expand coverage by automating more scenarios.
8.  **Establish Automated UAT Reporting:**
    *   Work towards generating automated test execution reports providing clear evidence for UAT.
    *   Define process for sharing reports with business users pre-exploratory UAT.
9.  **Document Best Practices & Create Migration Playbook:**
    *   Document the end-to-end process for UAT automation.
    *   Capture lessons learned, challenges, and best practices in a "UAT Automation Migration Playbook."
10. **Prepare for Knowledge Sharing & Team Onboarding:**
    *   Prepare materials for training/onboarding other teams on the new UAT automation approach.

## Engineer 2: Embedding New Ways of Working & Engineering Practices

**Goal:** Champion and implement modern engineering/testing practices within pilot squads, focusing on CI/CD integration, shift-left, automation culture, tooling (mocking, BDD, PEGA testing), and stable development pipelines.

**Key Activities (Phased: Assessment & Strategy; Implementation & Coaching; Optimization & Standardization):**

1.  **Baseline Current Engineering Practices & CI/CD Maturity:**
    *   Map pilot squads' existing development lifecycle, branching, build, testing, and CI/CD.
    *   Identify pain points and gaps against the Sirius Roadmap.
2.  **Develop & Communicate Pilot Engineering Practices Adoption Strategy:**
    *   Define a strategy for introducing unit testing, BDD, mocking, CI/CD integration, and developer ownership in pilot squads.
    *   Socialize this strategy and roadmap benefits.
3.  **Tooling Onboarding & Environment Preparation:**
    *   Train pilot squads on ReqNRoll/Playwright, Mockito/MockFlow, PEGA unit testing, and DT2 usage.
4.  **Drive Adoption of Unit Testing & Developer-Led Testing:**
    *   Coach developers in pilot squads on writing effective unit tests (including PEGA unit tests).
    *   Integrate unit tests into early CI stages; promote "squads own test automation" and "automation as part of DoD."
5.  **Integrate Automated Tests into CI/CD Pipelines:**
    *   Hands-on support for configuring CI/CD pipelines to automatically execute unit, squad functionality, and Sirius functionality tests at appropriate stages with quality gates.
6.  **Establish & Champion Mocking Practices:**
    *   Guide pilot squads in identifying dependencies and using Mockito/MockFlow for mocks in Dev/DT2.
7.  **Refine CI/CD Pipelines and Test Execution Efficiency:**
    *   Monitor and optimize CI/CD pipeline performance and test execution times.
    *   Refine quality gate rules.
8.  **Develop & Document Standardized Engineering Playbooks:**
    *   Document best practices for CI/CD, PEGA unit testing, mocking, BDD integration, and branching.
9.  **Facilitate Performance Profiling Setup:**
    *   Guide pilot squads in integrating performance profiling tests (against mocked endpoints) in DT2.
10. **Prepare for Scaling & Knowledge Transfer:**
    *   Develop training modules and plan for champion identification and rotation support.