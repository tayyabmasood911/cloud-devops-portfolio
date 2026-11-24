import os
import unittest

class TestComponentIntegrity(unittest.TestCase):
    def test_readme_exists(self):
        self.assertTrue(os.path.exists("README.md"), "README.md must be present")

    def test_makefile_exists(self):
        self.assertTrue(os.path.exists("Makefile"), "Makefile must be present")

    def test_ci_workflow_exists(self):
        self.assertTrue(os.path.exists(".github/workflows/ci.yml"), "CI workflow must be present")

    def test_healthcheck_script_exists(self):
        self.assertTrue(os.path.exists("scripts/healthcheck.sh"), "Healthcheck script must be present")

    def test_environment_template_exists(self):
        self.assertTrue(os.path.exists("config/production.env.example"), "Env template must be present")

    def test_gitattributes_exists(self):
        self.assertTrue(os.path.exists(".gitattributes"), ".gitattributes must be present")

    def test_security_policy_exists(self):
        self.assertTrue(os.path.exists("SECURITY.md"), "SECURITY.md must be present")

    def test_architecture_svg_exists(self):
        self.assertTrue(os.path.exists("docs/architecture.svg"), "docs/architecture.svg must be present")
        with open("docs/architecture.svg", "r", encoding="utf-8") as f:
            content = f.read()
            self.assertIn("#ffffff", content, "Architecture SVG must have strict white background")
            self.assertIn("<svg", content, "Valid SVG root element required")

    def test_portfolio_showcase_content(self):
        with open("README.md", "r", encoding="utf-8") as f:
            content = f.read()
            self.assertIn("tayyabmasood911", content, "Portfolio must reference active user profile")
            self.assertIn("opentofu-aws-multi-region-transit-gateway", content)
            self.assertIn("pulumi-typescript-aws-ecs-fargate", content)
            self.assertIn("terraform-azure-aks-zero-trust", content)
            self.assertIn("terraform-gcp-gke-enterprise", content)
            self.assertIn("crossplane-aws-composable-infrastructure", content)
            self.assertIn("helm-charts-microservices-suite", content)
            self.assertIn("cloud-infrastructure-cost-estimation-infracost", content)

if __name__ == "__main__":
    unittest.main()
