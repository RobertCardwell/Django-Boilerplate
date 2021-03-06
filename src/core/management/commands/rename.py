# A tool to rename this project at all the points where the name occurs.
# Usage to rename the project to "myproject":
# python manage.py rename myproject
# You will need to manually rename the outermost folder.

from django.core.management.base import BaseCommand
import os


class Command(BaseCommand):
    help = 'Renames a Django Project'
    
    def add_arguments(self, parser):
        parser.add_argument(    
            'new_project_name', 
            type=str,
            help='The new Django project name'
            )
        
    def handle(self, *args, **kwargs):
        new_project_name = kwargs['new_project_name']
        
        # logic to rename the project:
        
        files_to_rename = [
            'boilerplate/settings/base.py',
            'boilerplate/wsgi.py',
            'manage.py',
            'core/management/commands/rename.py'
        ]
        
        folder_to_rename = 'boilerplate'

        for f in files_to_rename:
            with open(f, 'r') as file:
                filedata = file.read()
            
            filedata = filedata.replace('boilerplate', new_project_name)
            
            with open(f, 'w') as file:
                file.write(filedata)
        
        os.rename(folder_to_rename, new_project_name)
        
        self.stdout.write(self.style.SUCCESS('Project has been renamed to %s' % new_project_name))
        