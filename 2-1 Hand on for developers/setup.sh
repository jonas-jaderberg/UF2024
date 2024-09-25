#!/bin/bash

cat << \EOF >> ~/.bash_profile
# Add .NET Core SDK tools
export PATH="$PATH:/home/vscode/.dotnet/tools"
EOF

