#!/usr/bin/env node
// file: scripts/replace-contribution-icons.js

/**
 * Replace Contribution Icons Script
 * 
 * This script automatically replaces All Contributors emojis with custom Phosphor icons
 * in the README.md file. It's designed to work with the All Contributors bot workflow
 * to maintain visual consistency across the project.
 * 
 * Usage:
 *   node scripts/replace-contribution-icons.js
 * 
 * The script:
 * 1. Reads the README.md file
 * 2. Replaces all standard All Contributors emojis with custom SVG icons
 * 3. Writes the updated content back to README.md
 * 
 * Icons are sourced from the assets/icons/ directory and use the official
 * All Contributors emoji key from https://allcontributors.org/docs/en/emoji-key
 */

const fs = require('fs');
const path = require('path');

// Read the README.md file from the project root
const readmePath = path.join(__dirname, '..', 'README.md');
let readmeContent = fs.readFileSync(readmePath, 'utf8');

/**
 * Emoji to Icon Mapping
 * 
 * Maps all standard All Contributors emojis to custom Phosphor SVG icons.
 * Based on the official All Contributors emoji key from:
 * https://allcontributors.org/docs/en/emoji-key
 * 
 * Each mapping includes:
 * - Official emoji from All Contributors specification
 * - Custom SVG icon with proper alt text and styling
 * - Consistent 16x16 size with vertical alignment
 */
const emojiToIconMap = {
    '🔊': '<img src="assets/icons/megaphone.svg" alt="Audio" width="16" height="16" style="vertical-align: middle;">',
    '♿️': '<img src="assets/icons/shield-check.svg" alt="Accessibility" width="16" height="16" style="vertical-align: middle;">',
    '🐛': '<img src="assets/icons/bug.svg" alt="Bug" width="16" height="16" style="vertical-align: middle;">',
    '📝': '<img src="assets/icons/file-text.svg" alt="Blog" width="16" height="16" style="vertical-align: middle;">',
    '💼': '<img src="assets/icons/handshake.svg" alt="Business" width="16" height="16" style="vertical-align: middle;">',
    '💻': '<img src="assets/icons/terminal.svg" alt="Code" width="16" height="16" style="vertical-align: middle;">',
    '🖋': '<img src="assets/icons/clipboard-text.svg" alt="Content" width="16" height="16" style="vertical-align: middle;">',
    '🔣': '<img src="assets/icons/chart-bar.svg" alt="Data" width="16" height="16" style="vertical-align: middle;">',
    '📖': '<img src="assets/icons/books.svg" alt="Documentation" width="16" height="16" style="vertical-align: middle;">',
    '🎨': '<img src="assets/icons/palette.svg" alt="Design" width="16" height="16" style="vertical-align: middle;">',
    '💡': '<img src="assets/icons/lightbulb.svg" alt="Examples" width="16" height="16" style="vertical-align: middle;">',
    '📋': '<img src="assets/icons/calendar.svg" alt="Event Organizing" width="16" height="16" style="vertical-align: middle;">',
    '💵': '<img src="assets/icons/currency-dollar.svg" alt="Financial" width="16" height="16" style="vertical-align: middle;">',
    '🔍': '<img src="assets/icons/magnifying-glass.svg" alt="Funding/Research" width="16" height="16" style="vertical-align: middle;">',
    '🤔': '<img src="assets/icons/lightbulb.svg" alt="Ideas" width="16" height="16" style="vertical-align: middle;">',
    '🚇': '<img src="assets/icons/server.svg" alt="Infrastructure" width="16" height="16" style="vertical-align: middle;">',
    '🚧': '<img src="assets/icons/wrench.svg" alt="Maintenance" width="16" height="16" style="vertical-align: middle;">',
    '🧑‍🏫': '<img src="assets/icons/handshake.svg" alt="Mentoring" width="16" height="16" style="vertical-align: middle;">',
    '📦': '<img src="assets/icons/package.svg" alt="Platform" width="16" height="16" style="vertical-align: middle;">',
    '🔌': '<img src="assets/icons/plug.svg" alt="Plugin" width="16" height="16" style="vertical-align: middle;">',
    '📆': '<img src="assets/icons/calendar.svg" alt="Project Management" width="16" height="16" style="vertical-align: middle;">',
    '📣': '<img src="assets/icons/megaphone.svg" alt="Promotion" width="16" height="16" style="vertical-align: middle;">',
    '💬': '<img src="assets/icons/question.svg" alt="Questions" width="16" height="16" style="vertical-align: middle;">',
    '🔬': '<img src="assets/icons/magnifying-glass.svg" alt="Research" width="16" height="16" style="vertical-align: middle;">',
    '👀': '<img src="assets/icons/eyes.svg" alt="Review" width="16" height="16" style="vertical-align: middle;">',
    '🛡️': '<img src="assets/icons/shield-check.svg" alt="Security" width="16" height="16" style="vertical-align: middle;">',
    '🔧': '<img src="assets/icons/wrench.svg" alt="Tools" width="16" height="16" style="vertical-align: middle;">',
    '🌍': '<img src="assets/icons/globe.svg" alt="Translation" width="16" height="16" style="vertical-align: middle;">',
    '⚠️': '<img src="assets/icons/test-tube.svg" alt="Tests" width="16" height="16" style="vertical-align: middle;">',
    '✅': '<img src="assets/icons/check.svg" alt="Tutorials" width="16" height="16" style="vertical-align: middle;">',
    '📢': '<img src="assets/icons/megaphone.svg" alt="Talks" width="16" height="16" style="vertical-align: middle;">',
    '📓': '<img src="assets/icons/test-tube.svg" alt="User Testing" width="16" height="16" style="vertical-align: middle;">',
    '📹': '<img src="assets/icons/video-camera.svg" alt="Videos" width="16" height="16" style="vertical-align: middle;">'
};

/**
 * Replace Emojis with Custom Icons
 * 
 * Iterates through all emoji mappings and replaces each emoji occurrence
 * in the README.md content with the corresponding custom SVG icon.
 * Uses global regex replacement to catch all instances of each emoji.
 */
Object.entries(emojiToIconMap).forEach(([emoji, icon]) => {
    const regex = new RegExp(emoji, 'g');
    readmeContent = readmeContent.replace(regex, icon);
});

/**
 * Write Updated Content
 * 
 * Saves the modified README.md content back to the file system.
 * The file now contains custom icons instead of standard emojis.
 */
fs.writeFileSync(readmePath, readmeContent, 'utf8');

// Success message
console.log('✅ Successfully replaced emojis with custom icons in README.md');

