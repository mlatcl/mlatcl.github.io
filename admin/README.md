# Decap CMS Admin

This is the Decap CMS administration area for the ML@CL site (formerly Netlify CMS).

Use it to edit people, projects, publications, available student projects, and related content without a pull request. Git-fluent editors can still work in the repository directly.

## Login URL

Open **https://mlatcl.netlify.app/admin/** and sign in with GitHub.

Do **not** use `https://mlatcl.github.io/admin/` for login. Decap’s GitHub backend uses Netlify’s OAuth proxy, which only works when the admin UI is served from the Netlify site hostname.

## Proposing an available student project

In the CMS, open **Projects for MPhil/PrtIII/PrtII** and create or edit an entry:

1. Set **Status** to `Available` (or `Hidden` / `Completed` as appropriate).
2. Choose **Categories** (`prtii`, `prtiii`, `MPhil`, `PhD`).
3. Add **Supervisors** (primary contact first).
4. Fill **Prerequisites** when the brief expects specific preparation (for example IEI / L172).
5. Link **Related Projects** to group programmes such as Information Topography, Interfaces, or AI Adoption.
6. Complete the overview and FAQ fields (`student_learn`, `project_objective`, `project_bigger_picture`).

## Configuring GitHub OAuth on Netlify

These files configure Decap CMS. The site must be connected in [Netlify](https://app.netlify.com) from the GitHub repo `mlatcl/mlatcl.github.io`.

Access is via the GitHub backend (org members with push access), not Netlify Identity. Netlify still hosts the OAuth proxy:

1. In GitHub (organisation) go to **Developer Settings** → **OAuth Apps** and create an application. Authorization callback URL should be `https://api.netlify.com/auth/done`.
2. Create a client ID / secret pair.
3. In Netlify go to **Access control** → **OAuth** → **Install provider**, choose GitHub, and paste the client ID and secret.

See also: <https://docs.netlify.com/visitor-access/oauth-provider-tokens/>

![](oauth-settings.png)

## Local editing

`admin/config.yml` sets `local_backend: true`. Maintainers can run a local Decap proxy against a checkout to test schema changes before publishing.
