#! /usr/bin/env nix-shell
#! nix-shell -i fish -p pkgs.pandoc pkgs.python39Packages.weasyprint

function build-markdown
	pandoc index.html -f html -t markdown -s -o readme.md
end

function build-pdf
	pandoc index.html -f html -t pdf --pdf-engine=weasyprint -s -o resume.pdf
end

function sync
	set DATE (date --iso-8601=hours)
	set MSG "Automatically added on <$DATE>"
	git add *
	git commit -m "$MSG"
	git push -u origin main
end

function main
	build-markdown
	build-pdf
	sync
end

main $argv
