# App support and privacy

Public documents for **Gallery Search AI** and **platelog**, hosted together on [GitHub Pages](https://lpaiu-cs.github.io/platelog-site/). The repository name stays `platelog-site` so previously published Platelog links keep working.

## Edit a document

1. Open the relevant HTML file on GitHub and click the pencil. Edit the text and effective date, then propose a change on a branch.
2. Review the rendered page locally and run `python3 check_site.py`. No installation, framework, build step or GitHub Actions is needed.
3. Obtain the owner's final approval before merging. GitHub Pages publishes `main` from `/` using the repository's existing Pages configuration.
4. After Pages publishes, open the live URL before updating any App Store / Google Play setting. Never point a store at a pending branch or inaccessible page.

For local preview:

```sh
python3 check_site.py
python3 -m http.server 8773 --bind 127.0.0.1
```

Open `http://127.0.0.1:8773/`. The checker verifies local links, document metadata and the absence of remote page assets or scripts. It does not certify legal compliance or availability of external services.

## Files and stable URLs

| Purpose | File / URL suffix |
|---|---|
| Shared app hub | `index.html` |
| Website and voluntary email support privacy | `site-privacy.html` |
| Gallery Search AI introduction | `gallery-search-ai/index.html` |
| Gallery Search AI policy | `gallery-search-ai/privacy.html` |
| Gallery Search AI help | `gallery-search-ai/support.html` |
| Gallery Search AI free use, license and consumer rights | `gallery-search-ai/purchase.html` |
| Platelog Korean introduction | `platelog.html` |
| Platelog existing Korean store links | `privacy.html`, `support.html`, `terms.html`, `delete.html` |
| Platelog English and Japanese documents | Same file names under `en/` and `ja/` |

`delete.html` and its translations remain the account-deletion URLs used by existing Platelog apps and Google Play. Do not delete or rename these files. No Platelog app update is needed for this URL-preserving migration.

The old `gallery-search-ai-support` repository will retain only compatibility redirects after the shared pages are live. Maintain the full documents here, not in both repositories.

## Keep the notices true

These apps have different processing: Gallery Search AI performs photo search locally; Platelog uploads content for invited crews. Keep their policies separate. Shared hosting and email practices belong in `site-privacy.html`.

When Gallery Search AI privacy/help changes, update the offline snapshots `ios/FindImage/Privacy.txt` and `Support.txt` in its private app repository in the same release. Use that repository's release-bundle check to verify the contact and current public URL. Record any temporary version mismatch; users must still be able to read help without internet access.

When Platelog behavior changes, update Korean, English and Japanese notices together. Preserve mandatory local rights even when a translation names Korean as the governing language. State the actual active providers, countries, data, retention and deletion behavior. Do not assert fixed backup days, guaranteed erasure of others' copies, unseen contracts or worldwide compliance.

Review the data flow before adding an SDK, analytics, AI service, login provider, purchase type or new market. Store privacy labels describe app collection; visiting this website and voluntarily emailing support have their own disclosure.

There are no third-party fonts, scripts, embedded media, analytics, forms or developer cookies. GitHub's own IP logging is disclosed. Adding a cookie banner for tracking that does not exist would not fix a processing issue.

## Release boundary

Gallery Search AI's initial release scope is the United States, United Kingdom, Canada, Australia and New Zealand. EU distribution is deferred. This does not expand Platelog's existing store distribution. Publishing English documents alone does not satisfy all obligations for expanding a cloud sharing service: verify international transfers, children's privacy, account deletion and operational rights handling before doing so.

Do not commit credentials, private addresses, telephone numbers, support emails from users, app telemetry or personal photographs. Public contact: `lpaiu.cs@gmail.com`. Operator: JUNEYOUNG KIM, South Korea; developer name: lpaiu.
