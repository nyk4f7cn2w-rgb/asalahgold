#!/bin/sh
# Bump the build id in index.html and version.json together (run before every publish).
# Visitors holding an old cached copy will auto-refresh once to the new build.
set -e
B="$(date -u +%Y.%m.%d-%H%M)"
sed -i "s|<meta name=\"asalah-build\" content=\"[^\"]*\">|<meta name=\"asalah-build\" content=\"$B\">|" index.html
printf '{"build":"%s"}\n' "$B" > version.json
echo "build $B"
