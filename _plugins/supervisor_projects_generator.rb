# frozen_string_literal: true
#
# Generates one page per supervisor listed in any _availableprojects/*.md
# document, at /people/<slug>/projects.html, using the shared
# `supervisor-projects` layout (defined in the mlatcl/jekyll-theme remote
# theme).
#
# This replaces the old scripts/generate_supervisor_pages.py workaround,
# which had to pre-commit one stub file per supervisor into a
# `_supervisorprojects/` collection because GitHub Pages' "legacy" build
# does not run custom generator plugins. Now that the site builds via a
# GitHub Actions workflow (.github/workflows/pages.yml), this generator
# runs for real at build time, so the stub files/collection/script are no
# longer needed.
module MlAtCl
  class SupervisorProjectsGenerator < Jekyll::Generator
    safe true
    priority :low

    def generate(site)
      supervisor_slugs(site).each do |slug|
        person = person_by_slug(site)[slug]
        next unless person # skip slugs with no matching _people/*.md file

        site.pages << build_page(site, slug, display_name(person))
      end
    end

    private

    # Unique, sorted list of supervisor slugs referenced across
    # _availableprojects/*.md. Guards against the one legacy entry that
    # uses an old mapping-style `supervisors:` list (hashes, not slugs)
    # instead of the modern slug-list schema.
    def supervisor_slugs(site)
      projects = site.collections["availableprojects"]&.docs || []
      projects
        .flat_map { |doc| Array(doc.data["supervisors"]).select { |s| s.is_a?(String) } }
        .uniq
        .sort
    end

    def person_by_slug(site)
      @person_by_slug ||= (site.collections["people"]&.docs || [])
        .each_with_object({}) { |doc, hash| hash[doc.data["slug"]] = doc }
    end

    def display_name(person)
      first = person.data["preferred"]
      first = person.data["given"] if first.nil? || first.to_s.strip.empty?
      [first, person.data["family"]].compact.join(" ")
    end

    def build_page(site, slug, name)
      page = Jekyll::PageWithoutAFile.new(site, site.source, "", "#{slug}-projects.html")
      page.content = ""
      page.data.merge!(
        "layout" => "supervisor-projects",
        "title" => "#{name} \u2014 Projects to Supervise",
        "person_slug" => slug,
        "permalink" => "/people/#{slug}/projects.html"
      )
      page
    end
  end
end
