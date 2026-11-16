from django.test import SimpleTestCase
from django.urls import reverse

from vagas.dados import VAGAS


class VagasViewsTests(SimpleTestCase):
    def test_home_page_renders(self):
        response = self.client.get(reverse("home"))

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "DevElas")
        self.assertContains(response, "Ver vagas")

    def test_mural_page_lists_all_vagas(self):
        response = self.client.get(reverse("mural"))

        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.context["vagas"]), len(VAGAS))
        self.assertContains(response, "Mural de vagas")

    def test_mural_filter_by_modalidade(self):
        response = self.client.get(reverse("mural"), {"modalidade": "Remoto"})

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context["total"], 2)
        self.assertTrue(all(vaga["modalidade"] == "Remoto" for vaga in response.context["vagas"]))
        self.assertContains(response, "na modalidade Remoto")

    def test_detail_page_renders_for_existing_vaga(self):
        response = self.client.get(reverse("detalhe", args=[1]))

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Desenvolvedora Python Júnior")

    def test_detail_page_raises_404_for_invalid_vaga(self):
        response = self.client.get(reverse("detalhe", args=[999]))

        self.assertEqual(response.status_code, 404)
