echo git add --all;
echo git commit -m $1
token_id="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"
username="brendajfa"
repo="KaggleExercices"
echo git push https://$token_id@github.com/$username/$repo.git
