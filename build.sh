#! /usr/bin/env nix-shell
#! nix-shell -i fish -p pkgs.pandoc pkgs.python39Packages.weasyprint pkgs.entr


function build-pdf
	pandoc resume.html -f html -t pdf --pdf-engine=weasyprint --css=pdf.css -s -o resume.pdf
end

function sync
	set DATE (date --iso-8601=hours)
	set MSG "Automatically added on <$DATE>"
	git pull
	git add *
	git commit -m "$MSG"
	git push -u origin main
end

function main
	build-pdf
	sync
end

main $argv
