#!/usr/bin/env python3
"""
Email Generator for Aire Labs Newsletter
Automates MJML email generation using templates and configuration files
"""

import json
import os
import sys
import argparse
from pathlib import Path
from datetime import datetime
import pystache

class EmailGenerator:
    def __init__(self, base_dir=None):
        self.base_dir = Path(base_dir) if base_dir else Path(__file__).parent
        self.templates_dir = self.base_dir / "templates"
        self.config_dir = self.base_dir / "config"
        self.output_dir = self.base_dir / "output"
        
        # Ensure output directory exists
        self.output_dir.mkdir(exist_ok=True)
    
    def load_config(self, config_file):
        """Load email configuration from JSON file"""
        config_path = self.config_dir / config_file
        if not config_path.exists():
            raise FileNotFoundError(f"Config file not found: {config_path}")
        
        with open(config_path, 'r') as f:
            return json.load(f)
    
    def load_template(self, template_file):
        """Load MJML template file"""
        template_path = self.templates_dir / template_file
        if not template_path.exists():
            raise FileNotFoundError(f"Template file not found: {template_path}")
        
        with open(template_path, 'r') as f:
            return f.read()
    
    def generate_email(self, config_file, template_file="newsletter-template.mjml", output_name=None):
        """Generate email from template and config"""
        print(f"Loading configuration: {config_file}")
        config = self.load_config(config_file)
        
        print(f"Loading template: {template_file}")
        template = self.load_template(template_file)
        
        print("Rendering email with configuration...")
        renderer = pystache.Renderer()
        rendered_email = renderer.render(template, config)
        
        # Generate output filename
        if not output_name:
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            output_name = f"newsletter_{timestamp}.mjml"
        
        output_path = self.output_dir / output_name
        
        print(f"Writing generated email to: {output_path}")
        with open(output_path, 'w') as f:
            f.write(rendered_email)
        
        print(f"✅ Email successfully generated: {output_path}")
        return output_path
    
    def create_new_config(self, config_name, based_on="email-config-example.json"):
        """Create a new configuration file based on existing template"""
        base_config = self.load_config(based_on)
        new_config_path = self.config_dir / f"{config_name}.json"
        
        with open(new_config_path, 'w') as f:
            json.dump(base_config, f, indent=2)
        
        print(f"✅ New config created: {new_config_path}")
        print("Edit this file to customize your email content.")
        return new_config_path
    
    def list_configs(self):
        """List available configuration files"""
        configs = list(self.config_dir.glob("*.json"))
        if configs:
            print("Available configurations:")
            for config in configs:
                print(f"  - {config.stem}")
        else:
            print("No configuration files found.")
        return configs
    
    def list_templates(self):
        """List available template files"""
        templates = list(self.templates_dir.glob("*.mjml"))
        if templates:
            print("Available templates:")
            for template in templates:
                print(f"  - {template.name}")
        else:
            print("No template files found.")
        return templates

def main():
    parser = argparse.ArgumentParser(description="Generate Aire Labs newsletter emails")
    parser.add_argument("action", choices=["generate", "new-config", "list-configs", "list-templates"], 
                       help="Action to perform")
    parser.add_argument("--config", "-c", help="Configuration file name (without .json extension)")
    parser.add_argument("--template", "-t", default="newsletter-template.mjml", 
                       help="Template file name")
    parser.add_argument("--output", "-o", help="Output file name")
    parser.add_argument("--name", "-n", help="Name for new configuration")
    
    args = parser.parse_args()
    
    generator = EmailGenerator()
    
    try:
        if args.action == "generate":
            if not args.config:
                print("Error: --config is required for generate action")
                sys.exit(1)
            
            config_file = f"{args.config}.json" if not args.config.endswith('.json') else args.config
            generator.generate_email(config_file, args.template, args.output)
        
        elif args.action == "new-config":
            if not args.name:
                print("Error: --name is required for new-config action")
                sys.exit(1)
            
            generator.create_new_config(args.name)
        
        elif args.action == "list-configs":
            generator.list_configs()
        
        elif args.action == "list-templates":
            generator.list_templates()
    
    except Exception as e:
        print(f"Error: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
