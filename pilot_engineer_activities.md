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
        *   Set up local development environment for ReqNRoll and Playwright.
    *   **Timeline/Effort:** Weeks 2-5 (Can be concurrent; dedicated learning ~5-7 person-days)
    *   **Dependencies/Requirements:**
        *   Access to training resources/materials for ReqNRoll, Playwright, BDD.
        *   Access to a sandbox/development environment for practice.
        *   Guidance/documentation on chosen tools from Sirius Roadmap (pages 5-6).
    *   **Deliverables:**
        *   Demonstrated proficiency in BDD tools and methodology (e.g., sample scenarios/scripts).
        *   Personal learning notes/summary.
        *   Functional local setup for BDD/Playwright development.

---

**Phase 2: Migration, Automation Development & Initial Integration (Est. Months 3-4)**

4.  **Convert Selected UAT Scenarios to BDD (Gherkin)**
    *   **Activities:**
        *   For the prioritized UAT scenarios, rewrite them as clear, concise, and unambiguous Gherkin (.feature) files.
        *   Conduct workshops (Three Amigos: BA/PO, Dev, Test) to validate these BDD scenarios.
        *   Establish conventions for Gherkin syntax and feature file organization.
    *   **Timeline/Effort:** Weeks 7-10 (~15-18 person-days)
    *   **Dependencies/Requirements:**
        *   Prioritized backlog of UAT scenarios (from Activity 2).
        *   Proficiency in BDD/Gherkin (from Activity 3).
        *   Availability of BAs, POs, and pilot squad developers for validation workshops.
        *   Access to a version control system for feature files.
    *   **Deliverables:**
        *   A set of reviewed and approved Gherkin feature files for the pilot UAT scenarios, stored in version control.
        *   Documented Gherkin writing conventions.

5.  **Develop Automated Test Scripts using Playwright**
    *   **Activities:**
        *   Implement the step definitions for the Gherkin scenarios using Playwright within the ReqNRoll framework.
        *   Define and implement robust Playwright locator strategies (e.g., data-testid, CSS, role-based locators).
        *   Structure test code using Page Object Model (POM) or similar design patterns for maintainability and reusability.
        *   Implement test data parameterization strategies (e.g., using external data files, dynamic data generation) to support varied test scenarios.
        *   Incorporate best practices for explicit waits and assertions to ensure test stability.
        *   Collaborate with the Eng. Practices Eng. to understand and utilize mocking strategies (Mockito/MockFlow, roadmap page 8) for isolating tests from backend dependencies.
    *   **Timeline/Effort:** Weeks 9-16 (~25-30 person-days, significant overlap with activity 4 initially, then focused development)
    *   **Dependencies/Requirements:**
        *   Approved Gherkin feature files (from Activity 4).
        *   Established Playwright/ReqNRoll development environment.
        *   Access to application under test (or its components) for script development.
        *   Collaboration with Eng. Practices Eng. for mocking strategy and CI/CD integration points.
        *   Test data sources/creation strategy.
    *   **Deliverables:**
        *   Functional, version-controlled Playwright automated test scripts and step definition libraries for the pilot BDD scenarios.
        *   Documented locator strategies and POM structure.
        *   Reusable test utility functions.

6.  **Setup & Test Execution in DT2 Environment**
    *   **Activities:**
        *   Collaborate with the Eng. Practices Eng. to ensure the automated UAT scripts (ReqNRoll/Playwright) can be configured and executed in the dedicated DT2 environment (roadmap page 11).
        *   Develop GitHub Actions workflows to trigger the automated UAT suite (e.g., on a schedule, on deployment to DT2, or manually triggered for UAT phase).
        *   Configure test execution to parse and publish test results (e.g., JUnit XML, HTML reports) for CI/CD visibility and stakeholder review within GitHub Actions.
        *   Perform initial test runs in DT2, troubleshoot environmental/script issues, and ensure stability.
    *   **Timeline/Effort:** Weeks 15-18 (~8-10 person-days, concurrent with later stages of Activity 5)
    *   **Dependencies/Requirements:**
        *   DT2 environment provisioned and accessible as per roadmap.
        *   Initial set of automated scripts ready for execution (from Activity 5).
        *   Deployment mechanisms for application and test scripts to DT2.
        *   GitHub Actions runner configured for DT2 or able to trigger tests there.
        *   Support from Eng. Practices Eng. and potentially platform/ops teams for DT2 setup and GitHub Actions integration.
    *   **Deliverables:**
        *   Successfully executed pilot automated UAT suite in DT2, triggered via GitHub Actions.
        *   Documented setup/configuration for running UAT suite in DT2, including GitHub Actions workflow files.
        *   Automated test reports available via GitHub Actions artifacts or linked dashboards.
        *   Initial list of any identified environment or script stability issues.

---

**Phase 3: Refinement, Reporting & Knowledge Transfer Preparation (Est. Months 5-6)**

7.  **Iterate and Refine Automated UAT Suite**
    *   **Activities:**
        *   Based on execution results and feedback, continuously refine and stabilize the automated UAT test scripts. Address flakiness.
        *   Investigate and implement Playwright's test concurrency features (sharding, parallel workers) within GitHub Actions to optimize UAT suite execution time.
        *   Implement intelligent retry mechanisms for inherently flaky tests, with clear reporting on retries. Ensure this doesn't hide persistent issues.
        *   Expand coverage by automating more UAT scenarios from the prioritized backlog as time permits.
    *   **Timeline/Effort:** Weeks 17-24 (~15-20 person-days, ongoing)
    *   **Dependencies/Requirements:**
        *   Running UAT suite in DT2 via GitHub Actions (from Activity 6).
        *   Feedback mechanisms from pilot executions and UAT stakeholders.
        *   Stable application builds for testing against.
        *   Resources (e.g., CI runners) available for parallel execution.
    *   **Deliverables:**
        *   An increasingly robust, reliable, and comprehensive automated UAT test suite with optimized execution times.
        *   Updated scripts and GitHub Actions workflows in version control.
        *   Report on flakiness reduction and concurrency improvements.

8.  **Establish Automated UAT Reporting**
    *   **Activities:**
        *   Work towards generating comprehensive automated test execution reports (as per roadmap page 12 via ReqNRoll/Playwright capabilities and GitHub Actions artifacts) providing clear evidence of test coverage, pass/fail status, screenshots/videos on failure, and defects found.
        *   Define the process for sharing these reports with business users *before* their focused exploratory UAT.
        *   Integrate test reporting with existing test management or defect tracking tools (e.g., Jira) if feasible.
    *   **Timeline/Effort:** Weeks 19-22 (~7-10 person-days)
    *   **Dependencies/Requirements:**
        *   Automated UAT suite executing reliably via GitHub Actions.
        *   Chosen reporting tools/libraries compatible with Playwright/ReqNRoll and publishable via GitHub Actions.
        *   Requirements from business users on report content and accessibility.
    *   **Deliverables:**
        *   Standardized automated test report template and generation process integrated into the GitHub Actions pipeline.
        *   Example reports shared with stakeholders, demonstrating key metrics and failure analysis capabilities.
        *   Documented procedure for accessing and interpreting UAT automation reports.

9.  **Document Best Practices & Create Migration Playbook**
    *   **Activities:**
        *   Document the end-to-end process for identifying, prioritizing, converting, and automating UAT test cases using ReqNRoll/Playwright and integrating with GitHub Actions.
        *   Capture lessons learned, challenges, solutions, and best practices for BDD/Playwright implementation, concurrency, reporting, and CI/CD integration specifically for UAT.
    *   **Timeline/Effort:** Weeks 20-24 (~8-10 person-days, ongoing documentation build-up)
    *   **Dependencies/Requirements:**
        *   Experience and learnings from all previous activities.
        *   Templates for playbook documentation.
    *   **Deliverables:**
        *   A draft "UAT Automation Migration Playbook" for pilot teams and future scaling, including technical setup guides for tools and CI.

10. **Prepare for Knowledge Sharing & Team Onboarding**
    *   **Activities:**
        *   Prepare materials (presentations, hands-on labs, code examples) and a plan for training/onboarding other teams on the new UAT automation approach, including technical aspects of tool usage and GitHub Actions integration.
        *   Identify reusable components, Playwright utility libraries, or GitHub Actions workflow templates from the pilot work.
    *   **Timeline/Effort:** Weeks 22-24 (~5-7 person-days)
    *   **Dependencies/Requirements:**
        *   Draft UAT Automation Migration Playbook (from Activity 9).
        *   Understanding of common skill levels in target teams.
    *   **Deliverables:**
        *   Initial set of technical training materials for UAT automation, ReqNRoll/Playwright, and CI integration.
        *   Plan for supporting the onboarding of future teams, including sandbox environment setup for training.

---

## Engineer 2: Embedding New Ways of Working & Engineering Practices

**Overall Goal:** Champion and implement modern engineering and testing practices within pilot squads, focusing on CI/CD integration (GitHub Actions), shift-left principles, automation culture, effective tooling adoption (mocking, BDD, PEGA testing), and establishing stable, efficient development pipelines as per the Sirius Roadmap.
**Total Estimated Duration:** 6 Months (Pilot Phase)

---

**Phase 1: Assessment, Strategy Definition & Foundational Setup (Est. Months 1-2)**

1.  **Baseline Current Engineering Practices & CI/CD Maturity**
    *   **Activities:**
        *   Conduct workshops and interviews with pilot squad members to map their existing development lifecycle, branching, build processes, testing, and CI/CD.
        *   Identify key pain points, inefficiencies, and gaps against roadmap goals (e.g., lack of unit tests, manual regression, unstable environments – roadmap pages 3, 4, 13).
    *   **Timeline/Effort:** Weeks 1-3 (~10-12 person-days)
    *   **Dependencies/Requirements:** (As previously defined)
    *   **Deliverables:** (As previously defined)

2.  **Develop & Communicate Pilot Engineering Practices Adoption Strategy**
    *   **Activities:**
        *   Based on the roadmap (esp. pages 10, 11, 13, 14) and baseline assessment, define a tailored strategy for introducing new practices in pilot squads (unit testing, BDD, mocking, CI/CD test integration, developer ownership).
        *   Socialize this strategy, benefits, and the Sirius Roadmap vision with pilot squads.
    *   **Timeline/Effort:** Weeks 2-4 (~7-8 person-days)
    *   **Dependencies/Requirements:** (As previously defined)
    *   **Deliverables:** (As previously defined)

3.  **Tooling Onboarding & Environment Preparation**
    *   **Activities:**
        *   Organize/deliver initial training/awareness for pilot squads on ReqNRoll/Playwright, Mockito/MockFlow (page 8), and PEGA unit testing (page 6).
        *   Provide technical setup guides/scripts for local development environments for these tools.
        *   Collaborate with platform teams to ensure pilot squads understand DT2 usage (page 11) and how to configure GitHub Actions runners (if self-hosted) or utilize GitHub-hosted runners effectively for DT2 interactions.
    *   **Timeline/Effort:** Weeks 3-6 (Can be concurrent; dedicated effort ~8-10 person-days)
    *   **Dependencies/Requirements:** (As previously defined) + GitHub Actions access and understanding of runner configurations.
    *   **Deliverables:** (As previously defined) + Basic setup guides for local tooling.

---

**Phase 2: Implementation, Coaching & CI/CD Integration (Est. Months 3-4)**

4.  **Drive Adoption of Unit Testing & Developer-Led Testing**
    *   **Activities:**
        *   Actively coach/mentor developers in pilot squads on writing effective unit tests.
        *   Guide squads in setting up PEGA unit test cases using PegaUnit or relevant tools within the PEGA platform, including configuring test rulesets and data transforms.
        *   Coach on mocking data pages, activities, and connectors effectively within PEGA unit tests to isolate units of work.
        *   Help squads integrate unit tests into their development workflow (execution on dev branch push via GitHub Actions - page 10).
        *   Champion "squads own test automation" and "test automation as part of Definition of Done (DoD)" (page 10).
    *   **Timeline/Effort:** Weeks 7-16 (~20-25 person-days, ongoing coaching and support)
    *   **Dependencies/Requirements:** (As previously defined) + Access to PEGA Dev Studio, PegaUnit documentation.
    *   **Deliverables:** (As previously defined) + Example PEGA unit tests with mocks. GitHub Actions workflow snippets for PEGA unit test execution (if PEGA build/test can be CLI driven).

5.  **Integrate Automated Tests into CI/CD Pipelines (GitHub Actions Focus)**
    *   **Activities:**
        *   Work hands-on with pilot squads to design and configure GitHub Actions YAML workflows for a comprehensive CI/CD pipeline.
        *   Define GitHub Actions workflow triggers (e.g., `on: [push]` to feature branches, `on: pull_request` to main/squad branches, `workflow_dispatch` for manual runs).
        *   Implement distinct jobs/stages within GitHub Actions for: build, static analysis (e.g., SonarLint/SonarQube integration), unit tests (Java, JS, PEGA), API/integration tests, and BDD UI tests (coordinated with UAT Eng).
        *   Configure quality gates in GitHub Actions (e.g., fail build on test failure, check code coverage thresholds from tools like JaCoCo/Istanbul and fail if below target, integrate SonarQube quality gates).
        *   Ensure test results (JUnit XML, etc.) are published as artifacts in GitHub Actions and provide fast feedback to developers (e.g., via PR comments or status checks).
        *   Automate deployment to DT2 from GitHub Actions upon successful completion of quality gates on squad/main branches.
    *   **Timeline/Effort:** Weeks 9-16 (~20-25 person-days, heavy collaboration with squads)
    *   **Dependencies/Requirements:** (As previously defined) + GitHub Actions expertise, access to configure repository secrets/variables, SonarQube/other quality tool integration points.
    *   **Deliverables:**
        *   Fully documented GitHub Actions workflow files (`.github/workflows/*.yml`) for pilot squads, covering build, multiple test stages, quality gates, and deployment to DT2.
        *   CI/CD pipelines for pilot squads enhanced with automated test execution stages and quality gates, all managed via GitHub Actions.

6.  **Establish & Champion Mocking Practices (Mockito/MockFlow)**
    *   **Activities:**
        *   Guide pilot squads in identifying external dependencies for mocking.
        *   Assist squads in setting up Mockito for Java-based service mocking or configuring WireMock/MockServer instances for broader API mocking, potentially run as Docker containers managed via CI/CD.
        *   Develop MockFlow configurations (as per roadmap page 8) to package and deploy these mocks (e.g., mock server configurations, Docker images) to Dev and DT2 environments via GitHub Actions.
        *   Coach on using mocking tools and ensure test scripts are configured to point to mocked service endpoints during CI test runs.
    *   **Timeline/Effort:** Weeks 10-15 (~10-12 person-days, concurrent with other activities)
    *   **Dependencies/Requirements:** (As previously defined) + Docker knowledge (if using containerized mocks), MockFlow tool/library access and documentation.
    *   **Deliverables:** (As previously defined) + Example MockFlow configurations, GitHub Actions steps for deploying/managing mocks.

---

**Phase 3: Optimization, Standardization & Knowledge Dissemination (Est. Months 5-6)**

7.  **Refine CI/CD Pipelines (GitHub Actions) and Test Execution Efficiency**
    *   **Activities:**
        *   Monitor CI/CD pipeline (GitHub Actions) performance and test execution times (aiming for <30 min for DT2 full suite, page 11).
        *   Work with squads to optimize by: implementing GitHub Actions best practices like reusable workflows (`workflow_call`), matrix builds for parallel testing across configurations (e.g., different browsers/Java versions), advanced dependency caching strategies.
        *   Analyze GitHub Actions execution logs and timing charts to identify bottlenecks in build and test stages.
        *   Refine quality gate rules and thresholds based on pilot experience.
        *   Implement strategies for NFRs such as using test concurrency to optimise test execution time for end-to-end journeys (Playwright).
    *   **Timeline/Effort:** Weeks 17-24 (~10-15 person-days, ongoing)
    *   **Dependencies/Requirements:** (As previously defined) + Advanced GitHub Actions knowledge.
    *   **Deliverables:** (As previously defined) + Optimized GitHub Actions workflows, documented pipeline optimization techniques.

8.  **Develop & Document Standardized Engineering Playbooks**
    *   **Activities:**
        *   Based on pilot experiences, document standardized approaches, including detailed technical guides for setting up and configuring GitHub Actions workflows for various testing types, PEGA unit testing with PegaUnit, Mockito/MockFlow usage, BDD test implementation with ReqNRoll/Playwright, and branching strategies that integrate seamlessly with GitHub Actions.
    *   **Timeline/Effort:** Weeks 18-24 (~15-18 person-days, ongoing documentation build-up)
    *   **Dependencies/Requirements:** (As previously defined)
    *   **Deliverables:** (As previously defined) + Specific technical sections in playbooks on GitHub Actions, an example being implementing test concurrecny to optimise test execution.

9.  **Facilitate Performance Profiling Setup**
    *   **Activities:**
        *   Guide pilot squads in scripting performance tests using tools like k6, JMeter (if existing expertise), or Playwright's performance API, targeting mocked endpoints.
        *   Integrate performance test execution into GitHub Actions (e.g., as a separate workflow or a job in the main pipeline), establishing performance baselines and alerts/reports for regressions.
        *   Coach on analyzing performance test results (response times, throughput, error rates).
    *   **Timeline/Effort:** Weeks 20-23 (~5-7 person-days)
    *   **Dependencies/Requirements:** (As previously defined) + Chosen performance testing tool setup, GitHub Actions integration capability for the tool.
    *   **Deliverables:** (As previously defined) + GitHub Actions workflow for performance testing, example performance test scripts.

10. **Prepare for Scaling & Knowledge Transfer**
    *   **Activities:**
        *   Develop training modules and workshop materials based on the playbooks, including hands-on labs for GitHub Actions pipeline creation, PEGA unit testing, mocking, and BDD automation setup.
        *   (No major new technical sub-tasks here, focuses on material preparation)
    *   **Timeline/Effort:** Weeks 22-24 (~7-10 person-days)
    *   **Dependencies/Requirements:** (As previously defined)
    *   **Deliverables:** (As previously defined) + Hands-on lab exercises for technical training.

---