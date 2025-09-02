# 🔄 Icon Replacement Reference

## 📝 **Markdown Icon Usage**

Replace emojis with custom icons using this format:

```markdown
<!-- Instead of: 📝 -->
<img src="assets/icons/file-text.svg" alt="Documentation" width="20" height="20" style="vertical-align: middle;">

<!-- Instead of: 🚀 -->
<img src="assets/icons/rocket.svg" alt="Quick Start" width="20" height="20" style="vertical-align: middle;">
```

## 🎯 **Complete Replacement Map**

### **Headers and Sections**
```markdown
# Make Gist List <img src="assets/icons/file-text.svg" alt="Documentation" width="20" height="20" style="vertical-align: middle;">

## <img src="assets/icons/rocket.svg" alt="Quick Start" width="20" height="20" style="vertical-align: middle;"> Quick Start

## <img src="assets/icons/target.svg" alt="Goals" width="20" height="20" style="vertical-align: middle;"> What You Get

## <img src="assets/icons/wrench.svg" alt="Configuration" width="20" height="20" style="vertical-align: middle;"> Configuration
```

### **Feature Lists**
```markdown
- <img src="assets/icons/arrows-clockwise.svg" alt="Updates" width="20" height="20" style="vertical-align: middle;"> **Automatic Updates**: Runs daily via GitHub Actions
- <img src="assets/icons/chart-bar.svg" alt="Data" width="20" height="20" style="vertical-align: middle;"> **Rich Information**: Title, file count, language, public status, update date, and links
- <img src="assets/icons/target.svg" alt="Integration" width="20" height="20" style="vertical-align: middle;"> **Gist Integration**: Optionally updates a target gist with the generated list
- <img src="assets/icons/rocket.svg" alt="Setup" width="20" height="20" style="vertical-align: middle;"> **Easy Setup**: Fork, configure secrets, and you're done!
- <img src="assets/icons/palette.svg" alt="Customization" width="20" height="20" style="vertical-align: middle;"> **Customizable**: Easy to modify output format and add new fields
- <img src="assets/icons/lock.svg" alt="Security" width="20" height="20" style="vertical-align: middle;"> **Secure**: Uses minimal GitHub token permissions (gist scope only)
```

### **Status Indicators**
```markdown
| Variable | Required | Description |
|----------|----------|-------------|
| `GITHUB_USERNAME` | <img src="assets/icons/check.svg" alt="Required" width="16" height="16" style="vertical-align: middle;"> | Your GitHub username |
| `LIST_GIST_ID` | <img src="assets/icons/x.svg" alt="Optional" width="16" height="16" style="vertical-align: middle;"> | ID of the gist to update (optional) |
```

### **Tips and Warnings**
```markdown
> <img src="assets/icons/lightbulb.svg" alt="Tip" width="16" height="16" style="vertical-align: middle;"> **Tip**: After forking, you'll be redirected to your own copy of the repository.

> <img src="assets/icons/warning.svg" alt="Important" width="16" height="16" style="vertical-align: middle;"> **Important**: The token only needs "gist" scope.
```

### **Success Indicators**
```markdown
> <img src="assets/icons/target.svg" alt="Success" width="16" height="16" style="vertical-align: middle;"> **Success Indicators**: 
> - The gist contains a markdown table with your gists
> - The table shows titles, file counts, languages, and links
> - The "Last updated" timestamp is recent
```

## 🎨 **CSS Styling Options**

### **Option 1: Inline Styles (Recommended for GitHub)**
```markdown
<img src="assets/icons/rocket.svg" alt="Quick Start" width="20" height="20" style="vertical-align: middle;">
```

### **Option 2: Custom CSS Classes (If using GitHub Pages)**
```css
.icon {
  width: 20px;
  height: 20px;
  vertical-align: middle;
  display: inline-block;
}

.icon-large {
  width: 24px;
  height: 24px;
}

.icon-small {
  width: 16px;
  height: 16px;
}
```

Then use:
```markdown
<img src="assets/icons/rocket.svg" alt="Quick Start" class="icon">
```

## 📱 **Responsive Considerations**

- **Desktop**: 20x20 or 24x24 pixels
- **Mobile**: 16x16 pixels (use CSS media queries)
- **High DPI**: SVG scales automatically
- **Accessibility**: Always include meaningful `alt` text

## 🔄 **Replacement Process**

1. **Download icons** from [Phosphor Icons](https://phosphoricons.com/)
2. **Save in `assets/icons/`** folder
3. **Replace emojis** using the patterns above
4. **Test appearance** in GitHub
5. **Adjust sizing** if needed

## 💡 **Pro Tips**

- **Consistent sizing**: Use the same dimensions throughout
- **Alt text**: Make it descriptive and meaningful
- **Vertical alignment**: Use `vertical-align: middle` for inline text
- **Test thoroughly**: Check on different devices and screen sizes
