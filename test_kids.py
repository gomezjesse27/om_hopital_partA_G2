from odoo.tests import common
from odoo.tools.safe_eval import safe_eval

class TestKidsActionDomain(common.TransactionCase):
    def setUp(self):
        super(TestKidsActionDomain, self).setUp()
        self.Patient = self.env['hospital.patient']

    def test_kids_action_domain(self):
        kid_young = self.Patient.create({
            'name': 'Kid Young',
            'age': 10,
            'gender': 'male',
        })
        kid_edge = self.Patient.create({
            'name': 'Kid Edge',
            'age': 18,
            'gender': 'female',
        })
        adult = self.Patient.create({
            'name': 'Adult Person',
            'age': 19,
            'gender': 'male',
        })

        kids_action = self.env.ref('om_hospital.action_hospital_kids')
        # Convert the domain from string to Python list using safe_eval
        kids_domain = safe_eval(kids_action.domain or '[]')

        kids_results = self.Patient.search(kids_domain)

        self.assertIn(kid_young, kids_results, "A 10-year-old should appear in kids domain.")
        self.assertIn(kid_edge, kids_results, "An 18-year-old should appear in kids domain.")
        self.assertNotIn(adult, kids_results, "A 19-year-old should not appear in kids domain.")

        print("PASSED: test_kids_action_domain")
