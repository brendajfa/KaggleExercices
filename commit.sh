echo git add --all;
echo git commit -m $1
token_id="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"
username="brendajfa"
repo="KaggleExercices"
echo git push https://$token_id@github.com/$username/$repo.git
