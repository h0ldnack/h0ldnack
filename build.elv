#! /usr/bin/env elvish
#pkgs.pandoc pkgs.python39Packages.weasyprint pkgs.entr

fn gen-index {
  fd --type file --extension html '.' > sitemap.txt
}

fn build-txt {
  pandoc resume.html -f html -t plain -o resume.txt
}


fn build-pdf {
  pandoc resume.html -f html -t pdf --pdf-engine=weasyprint --css=pdf.css -s -o resume.pdf
}

fn sync {
  var DATE = (date --iso-8601=hours)
  var MSG = (echo "Automatically added on" $DATE)
  try {
	git pull
	git add *
	git commit -m $MSG
	git push -u origin main
  } catch e {
	dunstify "Remote commit failed for holdnack.net | because $e"
  }
}

fn main {
  gen-index
  build-txt
  build-pdf
  sync
}

main
