import random

from django.contrib.auth.models import User
from django.core.management.base import BaseCommand
from faker import Faker

from notes.models import Note


class Command(BaseCommand):
    help = "Generate fake users and notes"

    def add_arguments(self, parser):
        parser.add_argument(
            "--users",
            type=int,
            default=5,  # Default number of users to create if none exist
            help="Number of fake users to create",
        )

        parser.add_argument(
            "--notes",
            type=int,
            default=50,  # Default number of notes to create
            help="Number of fake notes to create",
        )

    def handle(self, *args, **kwargs):
        fake = Faker()
        num_users = kwargs["users"]
        num_notes = kwargs["notes"]

        # Generate fake users if none exist
        users = User.objects.all()

        if not users.exists():
            self.stdout.write(self.style.WARNING(f"No users found. Creating {num_users} fake users."))
            for _ in range(num_users):
                first_name = fake.first_name()
                last_name = fake.last_name()
                username = fake.user_name()
                email = fake.email()
                password = "password123"  # Default password for all fake users  # noqa: S105

                user = User.objects.create_user(
                    username=username,
                    first_name=first_name,
                    last_name=last_name,
                    email=email,
                    password=password,
                )
                self.stdout.write(self.style.SUCCESS(f"User '{username}' created."))

            users = User.objects.all()

        # Generate fake notes
        self.stdout.write(self.style.SUCCESS(f"Generating {num_notes} fake notes."))
        for _ in range(num_notes):
            user = random.choice(users)  # noqa: S311
            title = fake.sentence(nb_words=6)
            body = fake.paragraph(nb_sentences=10)

            note = Note.objects.create(  # noqa: F841
                owner=user,
                title=title,
                body=body,
            )

            self.stdout.write(self.style.SUCCESS(f"Note '{title}' created for user '{user.username}'"))

        self.stdout.write(self.style.SUCCESS(f"{num_notes} fake notes created successfully!"))
