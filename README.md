# Aire Labs Email Automation System

An automated email generation system for creating consistent, professional newsletters using MJML templates and JSON configurations.

## 🚀 Quick Start

### 1. Install Dependencies

```bash
# Install Python dependencies
pip install -r requirements.txt

# Install Node.js dependencies (for MJML compilation)
npm install
```

### 2. Generate Your First Email

```bash
# Create a new email configuration
python email_generator.py new-config --name "december-update"

# Edit the configuration file
# config/december-update.json

# Generate the email
python email_generator.py generate --config december-update

# Compile MJML to HTML
npm run compile
```

## 📁 Project Structure

```
├── templates/              # MJML email templates
│   └── newsletter-template.mjml
├── config/                 # Email configurations  
│   ├── email-config-example.json
│   └── [your-configs].json
├── output/                 # Generated emails
│   ├── *.mjml             # Generated MJML files
│   └── html/              # Compiled HTML files
├── img/                   # Email assets
├── email_generator.py     # Main automation script
└── README.md
```

## ⚡ Automation Features

### Template System
- **Reusable MJML template** with variable placeholders
- **Consistent brand styling** across all emails
- **Modular sections** (hero, features, reading list, CTAs)
- **Conditional content** (show/hide sections)

### Configuration-Driven
- **JSON-based content** management
- **Easy text/image updates** without touching code
- **Multiple email variants** from one template
- **Version control friendly**

### Command Line Interface
```bash
# List available commands
python email_generator.py --help

# Create new configuration
python email_generator.py new-config --name "january-newsletter"

# Generate email from config
python email_generator.py generate --config "january-newsletter"

# List all configurations
python email_generator.py list-configs

# List all templates
python email_generator.py list-templates
```

## 📝 Creating New Emails

### Method 1: Configuration File (Recommended)

1. **Create new config:**
   ```bash
   python email_generator.py new-config --name "my-newsletter"
   ```

2. **Edit the JSON file:**
   ```json
   {
     "email_title": "Your Email Title",
     "hero_title": "Main Headline",
     "hero_intro_text": "Opening paragraph...",
     "primary_cta_text": "Get Started",
     "primary_cta_url": "https://your-link.com",
     "features": [
       {
         "feature_title": "New Feature",
         "feature_text_blocks": [
           {"text": "Feature description..."}
         ]
       }
     ]
   }
   ```

3. **Generate email:**
   ```bash
   python email_generator.py generate --config my-newsletter
   ```

4. **Compile to HTML:**
   ```bash
   npm run compile
   ```

### Method 2: Direct Template Editing

For one-off customizations, edit the template directly:
- `templates/newsletter-template.mjml`

## 🎨 Customization Options

### Content Sections
- **Hero section** with title, text, image, CTA
- **Platform updates** with multiple features
- **Reading recommendations** 
- **Secondary CTAs**
- **Company footer**

### Visual Elements
- Colors and fonts (defined in template)
- Images and screenshots
- Button styles and CTAs
- Section spacing and layout

### Conditional Content
Use boolean flags to show/hide sections:
```json
{
  "show_platform_updates": true,
  "show_reading_section": false,
  "show_secondary_cta": true
}
```

## 🔧 Advanced Usage

### Multiple Templates
Create specialized templates for different email types:
```bash
# Use custom template
python email_generator.py generate --config my-config --template custom-template.mjml
```

### Batch Generation
Generate multiple emails with different configurations:
```bash
for config in config/*.json; do
  python email_generator.py generate --config $(basename $config .json)
done
```

### Integration with Email Services
The generated HTML files can be imported into:
- **Mailchimp** - Copy HTML content
- **ConvertKit** - Import HTML template  
- **SendGrid** - Use as HTML template
- **Loops** - Import as custom template

## 📊 Best Practices

### Content Strategy
- **Lead with value** in hero section
- **Single clear CTA** per email
- **Consistent brand voice** (avoid "Ready to build faster" type language)
- **Mobile-first design** considerations

### Technical
- **Version control** all configurations
- **Test emails** before sending
- **Optimize images** for email
- **Preview** in multiple clients

### Organization
- **Descriptive config names** (e.g., `2024-12-product-update`)
- **Archive old emails** in dated folders
- **Document** configuration changes
- **Backup** generated files

## 🚦 Next Steps

### Level 1: Basic Automation ✅
- ✅ Template + variables system
- ✅ CLI for email generation
- ✅ JSON configuration management

### Level 2: Enhanced Workflow
- [ ] Web interface for non-technical users
- [ ] Email preview server
- [ ] A/B testing configurations
- [ ] Integration with email platforms

### Level 3: Full Pipeline
- [ ] Automated image optimization
- [ ] Content management system
- [ ] Scheduled email generation
- [ ] Analytics integration

## 💡 Tips for Success

1. **Start small** - Use the example configuration as a base
2. **Test frequently** - Generate and preview emails often
3. **Keep configurations simple** - Avoid overly complex JSON structures
4. **Document your process** - Note what works for your team
5. **Version everything** - Track changes to templates and configurations

---

This system transforms your manual email creation process into a scalable, maintainable workflow that maintains brand consistency while enabling rapid iteration.

