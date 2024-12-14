from odoo.tests import common, new_test_user
from odoo.exceptions import ValidationError

class TestHospitalModule(common.TransactionCase):
    def test_duplicate_name(self):
        user = new_test_user(self.env, "test base user", groups = "base.group_user")
        
        patient = self.env["hospital.patient"].create({
            "name": "John Doe",
            "age": 45,
        })

        with self.assertRaises(ValidationError) as e:
            self.env["hospital.patient"].create({
                "name": "John Doe",
                "age": 20,
            })
        
        self.assertIn(
            "Name John Doe Already Exists",
            str(e.exception),
            "Validation error message does not match expected output"
        )