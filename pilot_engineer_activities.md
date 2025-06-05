# Defined Lower-Level Activities for Pilot Engineers (First 6 Months)

## Engineer 1: Central UAT Test Case Identification & Migration

**Overall Goal:** Transform manual UAT by identifying critical business scenarios, migrating them to BDD (ReqNRoll/Playwright), and establishing an automation-first UAT strategy.
**Total Estimated Duration:** 6 Months (Pilot Phase)

---

**Phase 1: Discovery, Analysis & Planning (Est. Months 1-2)**

1.  **Deep Dive into Existing UAT Processes & Test Assets**
    *   **Activities:**
        *   Liaise with business teams, UAT coordinators, and product owners to collect all existing UAT documentation.
        *   Shadow current UAT execution sessions to understand manual effort, common challenges, and business context.
    *   **Timeline/Effort:** Weeks 1-3 (~10-12 person-days)
    *   **Dependencies/Requirements:**
        *   Availability of UAT stakeholders (business teams, coordinators, POs).
        *   Access to existing UAT documentation (test plans, cases, acceptance criteria).
        *   Opportunity to observe UAT sessions (if applicable and ongoing).
    *   **Deliverables:**
        *   Comprehensive inventory of current UAT assets.
        *   Documented map of existing UAT processes, including pain points & challenges.

2.  **Identify & Prioritize UAT Scenarios for Automation**
    *   **Activities:**
        *   Analyze collected UAT test cases and historical defect data to identify high-value, repetitive, business-critical E2E scenarios.
        *   Collaborate with stakeholders to select a pilot set of UAT scenarios (including candidates to replace current manual BVT). Prioritize based on business criticality, frequency, stability, and ROI for automation.
    *   **Timeline/Effort:** Weeks 3-6 (~12-15 person-days, overlapping with activity 1 & 3)
    *   **Dependencies/Requirements:**
        *   Completed initial UAT asset inventory (from Activity 1).
        *   Access to historical defect data (Jira, test management tools).
        *   Availability of stakeholders for prioritization workshops.
        *   Clear understanding of business-critical functionalities from roadmap/POs.
    *   **Deliverables:**
        *   A prioritized backlog of UAT scenarios selected for automation in the pilot.
        *   Justification and expected benefits for each selected scenario.

3.  **Master BDD Tooling & Methodology**
    *   **Activities:**
        *   Undertake training and self-learning on BDD principles, Gherkin syntax, ReqNRoll, and Playwright.
        *   Practice writing sample BDD scenarios and simple Playwright scripts in a sandbox/dev environment.
    *   **Timeline/Effort:** Weeks 2-5 (Can be concurrent; dedicated learning ~5-7 person-days)
    *   **Dependencies/Requirements:**
        *   Access to training resources/materials for ReqNRoll, Playwright, BDD.
        *   Access to a sandbox/development environment for practice.
        *   Guidance/documentation on chosen tools from Sirius Roadmap (pages 5-6).
    *   **Deliverables:**
        *   Demonstrated proficiency in BDD tools and methodology (e.g., sample scenarios/scripts).
        *   Personal learning notes/summary.

---

**Phase 2: Migration, Automation Development & Initial Integration (Est. Months 3-4)**

4.  **Convert Selected UAT Scenarios to BDD (Gherkin)**
    *   **Activities:**
        *   For the prioritized UAT scenarios, rewrite them as clear, concise, and unambiguous Gherkin (.feature) files.
        *   Conduct workshops (Three Amigos: BA/PO, Dev, Test) to validate these BDD scenarios.
    *   **Timeline/Effort:** Weeks 7-10 (~15-18 person-days)
    *   **Dependencies/Requirements:**
        *   Prioritized backlog of UAT scenarios (from Activity 2).
        *   Proficiency in BDD/Gherkin (from Activity 3).
        *   Availability of BAs, POs, and pilot squad developers for validation workshops.
        *   Access to a version control system for feature files.
    *   **Deliverables:**
        *   A set of reviewed and approved Gherkin feature files for the pilot UAT scenarios, stored in version control.

5.  **Develop Automated Test Scripts using Playwright**
    *   **Activities:**
        *   Implement the step definitions for the Gherkin scenarios using Playwright, ensuring scripts are modular, maintainable, and use appropriate selectors.
        *   Incorporate best practices for test data management. Collaborate with the Eng. Practices Eng. to understand and utilize mocking strategies (Mockito/MockFlow, roadmap page 8) for isolating tests.
    *   **Timeline/Effort:** Weeks 9-16 (~25-30 person-days, significant overlap with activity 4 initially, then focused development)
    *   **Dependencies/Requirements:**
        *   Approved Gherkin feature files (from Activity 4).
        *   Established Playwright development environment.
        *   Access to application under test (or its components) for script development.
        *   Collaboration with Eng. Practices Eng. for mocking strategy and CI/CD integration points.
        *   Test data sources/creation strategy.
    *   **Deliverables:**
        *   Functional, version-controlled Playwright automated test scripts for the pilot BDD scenarios.
        *   Documented step definitions and any helper libraries created.

6.  **Setup & Test Execution in DT2 Environment**
    *   **Activities:**
        *   Collaborate with the Eng. Practices Eng. to ensure the automated UAT scripts can be configured and executed in the dedicated DT2 environment (roadmap page 11).
        *   Perform initial test runs in DT2, troubleshoot environmental/script issues, and ensure stability.
    *   **Timeline/Effort:** Weeks 15-18 (~8-10 person-days, concurrent with later stages of Activity 5)
    *   **Dependencies/Requirements:**
        *   DT2 environment provisioned and accessible as per roadmap.
        *   Initial set of automated scripts ready for execution (from Activity 5).
        *   Deployment mechanisms for application and test scripts to DT2.
        *   Support from Eng. Practices Eng. and potentially platform/ops teams for DT2 setup.
    *   **Deliverables:**
        *   Successfully executed pilot automated UAT suite in DT2.
        *   Documentation of setup/configuration for running UAT suite in DT2.
        *   Initial list of any identified environment or script stability issues.

---

**Phase 3: Refinement, Reporting & Knowledge Transfer Preparation (Est. Months 5-6)**

7.  **Iterate and Refine Automated UAT Suite**
    *   **Activities:**
        *   Based on execution results and feedback, continuously refine and stabilize the automated UAT test scripts. Address flakiness.
        *   Expand coverage by automating more UAT scenarios from the prioritized backlog as time permits.
    *   **Timeline/Effort:** Weeks 17-24 (~15-20 person-days, ongoing)
    *   **Dependencies/Requirements:**
        *   Running UAT suite in DT2 (from Activity 6).
        *   Feedback mechanisms from pilot executions.
        *   Stable application builds for testing against.
    *   **Deliverables:**
        *   An increasingly robust, reliable, and comprehensive automated UAT test suite.
        *   Updated scripts in version control.

8.  **Establish Automated UAT Reporting**
    *   **Activities:**
        *   Work towards generating automated test execution reports (as per roadmap page 12) that provide clear evidence of test coverage, pass/fail status, and defects found.
        *   Define the process for sharing these reports with business users *before* their focused exploratory UAT.
    *   **Timeline/Effort:** Weeks 19-22 (~7-10 person-days)
    *   **Dependencies/Requirements:**
        *   Automated UAT suite executing reliably.
        *   Chosen reporting tools/libraries compatible with Playwright/ReqNRoll.
        *   Requirements from business users on report content.
    *   **Deliverables:**
        *   Standardized automated test report template and generation process integrated into the test execution pipeline.
        *   Example reports shared with stakeholders.

9.  **Document Best Practices & Create Migration Playbook**
    *   **Activities:**
        *   Document the end-to-end process for identifying, prioritizing, converting, and automating UAT test cases.
        *   Capture lessons learned, challenges, solutions, and best practices for BDD/Playwright implementation specifically for UAT.
    *   **Timeline/Effort:** Weeks 20-24 (~8-10 person-days, ongoing documentation build-up)
    *   **Dependencies/Requirements:**
        *   Experience and learnings from all previous activities.
        *   Templates for playbook documentation.
    *   **Deliverables:**
        *   A draft "UAT Automation Migration Playbook" for pilot teams and future scaling.

10. **Prepare for Knowledge Sharing & Team Onboarding**
    *   **Activities:**
        *   Prepare materials (presentations, guides, examples) and a plan for training/onboarding other teams on the new UAT automation approach.
        *   Identify reusable components or templates from the pilot work.
    *   **Timeline/Effort:** Weeks 22-24 (~5-7 person-days)
    *   **Dependencies/Requirements:**
        *   Draft UAT Automation Migration Playbook (from Activity 9).
        *   Understanding of common skill levels in target teams.
    *   **Deliverables:**
        *   Initial set of training materials for UAT automation.
        *   Plan for supporting the onboarding of future teams.

---

## Engineer 2: Embedding New Ways of Working & Engineering Practices

**Overall Goal:** Champion and implement modern engineering and testing practices within pilot squads, focusing on CI/CD integration, shift-left principles, automation culture, effective tooling adoption (mocking, BDD, PEGA testing), and establishing stable, efficient development pipelines as per the Sirius Roadmap.
**Total Estimated Duration:** 6 Months (Pilot Phase)

---

**Phase 1: Assessment, Strategy Definition & Foundational Setup (Est. Months 1-2)**

1.  **Baseline Current Engineering Practices & CI/CD Maturity**
    *   **Activities:**
        *   Conduct workshops and interviews with pilot squad members to map their existing development lifecycle, branching, build processes, testing, and CI/CD.
        *   Identify key pain points, inefficiencies, and gaps against roadmap goals (e.g., lack of unit tests, manual regression, unstable environments – roadmap pages 3, 4, 13).
    *   **Timeline/Effort:** Weeks 1-3 (~10-12 person-days)
    *   **Dependencies/Requirements:**
        *   Availability of pilot squad members (devs, testers, leads).
        *   Access to existing documentation on development processes and CI/CD setups.
        *   Understanding of the Sirius Roadmap's target engineering state.
    *   **Deliverables:**
        *   A baseline assessment report for each pilot squad, detailing current practices, CI/CD maturity, and identified gaps.

2.  **Develop & Communicate Pilot Engineering Practices Adoption Strategy**
    *   **Activities:**
        *   Based on the roadmap (esp. pages 10, 11, 13, 14) and baseline assessment, define a tailored strategy for introducing new practices in pilot squads (unit testing, BDD, mocking, CI/CD test integration, developer ownership).
        *   Socialize this strategy, benefits, and the Sirius Roadmap vision with pilot squads.
    *   **Timeline/Effort:** Weeks 2-4 (~7-8 person-days)
    *   **Dependencies/Requirements:**
        *   Baseline assessment reports (from Activity 1).
        *   Clear understanding of available tools (ReqNRoll, Playwright, Mockito, MockFlow, PEGA testing tools).
        *   Buy-in from squad leadership.
    *   **Deliverables:**
        *   Documented adoption strategy for new engineering practices for pilot teams.
        *   Communication plan and materials.

3.  **Tooling Onboarding & Environment Preparation**
    *   **Activities:**
        *   Organize/deliver initial training/awareness for pilot squads on ReqNRoll/Playwright (for BDD understanding), Mockito/MockFlow (page 8), and PEGA unit testing (page 6).
        *   Collaborate with platform teams to ensure pilot squads understand DT2 usage (page 11) for automated tests, including deployment of code/mocks.
    *   **Timeline/Effort:** Weeks 3-6 (Can be concurrent; dedicated effort ~8-10 person-days)
    *   **Dependencies/Requirements:**
        *   Availability of training materials or resources for specified tools.
        *   Access to DT2 environment and deployment mechanisms.
        *   Coordination with platform/infrastructure teams.
    *   **Deliverables:**
        *   Pilot squads onboarded onto new tools with basic understanding.
        *   DT2 environment access and usage guidelines clarified for pilot teams.
        *   Record of training sessions delivered.

---

**Phase 2: Implementation, Coaching & CI/CD Integration (Est. Months 3-4)**

4.  **Drive Adoption of Unit Testing & Developer-Led Testing**
    *   **Activities:**
        *   Actively coach/mentor developers in pilot squads on writing effective unit tests (including PEGA unit tests with mocking, page 6).
        *   Help squads integrate unit tests into their development workflow (execution on dev branch push - page 10).
        *   Champion "squads own test automation" and "test automation as part of Definition of Done (DoD)" (page 10).
    *   **Timeline/Effort:** Weeks 7-16 (~20-25 person-days, ongoing coaching and support)
    *   **Dependencies/Requirements:**
        *   Developers in pilot squads allocated time for learning and writing unit tests.
        *   Established unit testing frameworks (e.g., JUnit, NUnit, PEGA testing tools).
        *   CI infrastructure capable of running unit tests.
    *   **Deliverables:**
        *   Demonstrable increase in unit test creation and coverage within pilot squads.
        *   Unit tests integrated into early CI stages for pilot squads.
        *   DoD updated in pilot squads to include unit testing.

5.  **Integrate Automated Tests into CI/CD Pipelines**
    *   **Activities:**
        *   Work hands-on with pilot squads to configure CI/CD pipelines for automated execution of squad functionality tests (on dev branch merge) and Sirius functionality tests (on squad branch merge to main), pre-DT2 promotion (roadmap page 14).
        *   Ensure test results provide fast feedback and build statuses act as quality gates.
    *   **Timeline/Effort:** Weeks 9-16 (~20-25 person-days, heavy collaboration with squads)
    *   **Dependencies/Requirements:**
        *   Mature CI/CD infrastructure (e.g., Jenkins, GitLab CI, GitHub Actions).
        *   Availability of squad-level and Sirius-level automated tests (some developed by UAT Eng., some by squads).
        *   Clear definitions of quality gates.
        *   Collaboration with UAT Engineer for integrating BDD/E2E tests.
    *   **Deliverables:**
        *   CI/CD pipelines for pilot squads enhanced with automated test execution stages (unit, integration, squad functional, Sirius functional) and quality gates.
        *   Documented pipeline configurations.

6.  **Establish & Champion Mocking Practices**
    *   **Activities:**
        *   Guide pilot squads in identifying external dependencies causing test flakiness/slowness.
        *   Coach them on using Mockito and MockFlow to create/deploy mocks in Dev/DT2 (roadmap page 8).
    *   **Timeline/Effort:** Weeks 10-15 (~10-12 person-days, concurrent with other activities)
    *   **Dependencies/Requirements:**
        *   Understanding of application architecture and dependencies within pilot squads.
        *   Mockito/MockFlow tools set up and accessible.
        *   Developers trained in using these mocking tools.
    *   **Deliverables:**
        *   Pilot squads actively using mocking techniques for their automated tests.
        *   Reusable mock configurations/templates developed (if applicable).
        *   Reduction in test flakiness attributed to external dependencies for pilot tests.

---

**Phase 3: Optimization, Standardization & Knowledge Dissemination (Est. Months 5-6)**

7.  **Refine CI/CD Pipelines and Test Execution Efficiency**
    *   **Activities:**
        *   Monitor CI/CD pipeline performance and test execution times (aiming for <30 min for DT2 full suite, page 11). Work with squads to optimize (parallelization, targeted runs).
        *   Refine quality gate rules based on pilot experience ("green build" definitions - page 10).
    *   **Timeline/Effort:** Weeks 17-24 (~10-15 person-days, ongoing)
    *   **Dependencies/Requirements:**
        *   Established CI/CD pipelines with integrated tests (from Activity 5).
        *   Monitoring tools for pipeline performance.
        *   Squad collaboration for optimization efforts.
    *   **Deliverables:**
        *   Optimized CI/CD pipelines for pilot squads with improved efficiency and feedback times.
        *   Documented refined quality gate definitions.

8.  **Develop & Document Standardized Engineering Playbooks**
    *   **Activities:**
        *   Based on pilot experiences, document standardized approaches, best practices, code examples, and "how-to" guides for: CI/CD integration, PEGA unit testing, mocking, BDD test implementation, branching strategies supporting early testing.
    *   **Timeline/Effort:** Weeks 18-24 (~15-18 person-days, ongoing documentation build-up)
    *   **Dependencies/Requirements:**
        *   Learnings and best practices from all previous pilot activities.
        *   Collaboration with UAT Engineer for BDD-related content.
        *   Templates for playbooks.
    *   **Deliverables:**
        *   A set of "Engineering Practice Playbooks" for the Sirius program, covering key modernization areas.

9.  **Facilitate Performance Profiling Setup**
    *   **Activities:**
        *   Guide pilot squads in integrating performance profiling tests (against mocked endpoints) into their release pipeline in DT2 to catch regressions early (roadmap page 11).
    *   **Timeline/Effort:** Weeks 20-23 (~5-7 person-days)
    *   **Dependencies/Requirements:**
        *   Performance testing tools identified and available.
        *   DT2 environment stable and mocks in place.
        *   Squads able to define performance baselines/thresholds.
    *   **Deliverables:**
        *   Initial performance profiling tests integrated into CI/CD for pilot applications in DT2.
        *   Process for analyzing performance reports established.

10. **Prepare for Scaling & Knowledge Transfer**
    *   **Activities:**
        *   Develop training modules and workshop materials based on the playbooks.
        *   Identify "champions" within pilot squads who can help onboard other teams.
        *   Plan initial rotation/support strategy for these pilot squads assisting other teams.
    *   **Timeline/Effort:** Weeks 22-24 (~7-10 person-days)
    *   **Dependencies/Requirements:**
        *   Draft Engineering Practice Playbooks (from Activity 8).
        *   Agreement on the scaling strategy (as previously defined).
    *   **Deliverables:**
        *   Training materials for new engineering practices.
        *   A list of identified champions from pilot squads.
        *   A draft plan for supporting the scaling of these practices to other teams.

---