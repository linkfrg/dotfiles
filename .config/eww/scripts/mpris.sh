#!/bin/bash
playerctl -F metadata --format '{"name": "{{playerName}}", "title": "{{title}}", "artist": "{{artist}}", "status": "{{status}}", "art": "{{mpris:artUrl}}"}'
