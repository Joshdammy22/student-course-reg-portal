from django.core.management.base import BaseCommand
from courses.models import Course

class Command(BaseCommand):
    help = 'Delete all courses from the database'

    def handle(self, *args, **kwargs):
        # Get the number of courses before deleting
        course_count = Course.objects.count()

        if course_count == 0:
            self.stdout.write(self.style.WARNING('No courses found to delete.'))
            return

        # Delete all courses
        Course.objects.all().delete()

        # Output success message
        self.stdout.write(self.style.SUCCESS(f'Successfully deleted {course_count} courses.'))
