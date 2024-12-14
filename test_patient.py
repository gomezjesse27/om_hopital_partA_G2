from odoo.tests import common, new_test_user

class TestHospitalModule(common.TransactionCase):
    def test_create_patient(self):
        user = new_test_user(self.env, "test base user", groups = "base.group_user")

        patient = self.env["hospital.patient"].create({
            "name": "John Doe",
            "age": 45,
        })

        self.assertEqual(patient.age, 45, "Patient creation has bug, age should be 45")
        self.assertEqual(patient.name, "John Doe", "Patient creation has bug, name should be John Doe")