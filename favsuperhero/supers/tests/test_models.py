from django.db.models import CharField, ForeignKey, SET_NULL
from django.test import TestCase
from django_extensions.db.fields import AutoSlugField
from supers.models import Superhero, User


class SuperheroModelTest(TestCase):

    def test_fields(self):
        expected_fields = {
            'name': CharField,
            'slug': AutoSlugField,
            'player': ForeignKey
        }

        for field in expected_fields:
            self.assertTrue(hasattr(Superhero, field))
            self.assertTrue(isinstance(
                    Superhero._meta.get_field(field), expected_fields[field]
            ))

        self.assertEqual(Superhero._meta.get_field('name').max_length, 60)
        self.assertEqual(Superhero._meta.get_field('name').unique, True)

        self.assertEqual(
            Superhero._meta.get_field('slug')._populate_from, 'name'
        )

        self.assertEqual(
            Superhero._meta.get_field('player').related_model, User
        )
        self.assertEqual(Superhero._meta.get_field('player').null, True)
        self.assertEqual(
            Superhero._meta.get_field('player').remote_field.on_delete,
            SET_NULL
        )
