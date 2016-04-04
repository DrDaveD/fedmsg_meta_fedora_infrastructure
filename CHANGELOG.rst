
0.17.3
------

Commits

- fc4f25c50 Disable this test in koji.
  https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/fc4f25c50

0.17.2
------

Pull Requests

- (@AdamWill)       #370, add openQA processor
  https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/pull/370
- (@Devyani-Divs)   #371, Fixed unicode encode error
  https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/pull/371
- (@ralphbean)      #372, Handle new compat issues with copr messages.
  https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/pull/372
- (@msimacek)       #373, Add collection field to koschei processor
  https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/pull/373
- (@ralphbean)      #374, Add a PDC processor with tests.
  https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/pull/374

Commits

- 47a9d9a1a add openQA processor
  https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/47a9d9a1a
- 6117913ad Fixed unicode encode error
  https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/6117913ad
- 387d4f4df Handle new compat issues with copr messages.
  https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/387d4f4df
- 2794c59dd Handle new compat issues with copr messages.
  https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/2794c59dd
- 98e288cb5 Add collection attributes to koschei processor
  https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/98e288cb5
- 284c6a7fd Add a PDC processor with tests.
  https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/284c6a7fd
- ad9a7d974 Bury those links.
  https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/ad9a7d974

0.17.1
------

Pull Requests

- (@ralphbean)      #368, Long form for planet.
  https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/pull/368
- (@ralphbean)      #369, Conglomerate pagure events.
  https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/pull/369

Commits

- c0afe605f Long form for planet.
  https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/c0afe605f
- 82dea450f First stab at some pagure conglomerators.
  https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/82dea450f
- 9256efaea Merge pagure events by old style commits.
  https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/9256efaea
- decaa16e3 Handle conglomerating new-style pagure commits.
  https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/decaa16e3
- 7a287bf74 Newlines!
  https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/7a287bf74
- 4e08755c9 Limit this only to pagure messages.
  https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/4e08755c9

0.17.0
------

Pull Requests

- (@ralphbean)      #367, Start adding some lexers.
  https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/pull/367
- (@ralphbean)      #366, Pad against a race condition with koji.
  https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/pull/366

Commits

- 4015cc361 Pad against a race condition with koji.
  https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/4015cc361
- ff9b042a7 Start adding some lexers.
  https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/ff9b042a7

0.15.11
-------

Pull Requests

- (@ralphbean)      #361, Conglomerate irc meeting events (for fedora-hubs).
  https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/pull/361
- (@pypingou)       #362, Adjust the pagure processor for the new format of the fedmsg message sent
  https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/pull/362
- (@ralphbean)      #364, Fix copr links.
  https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/pull/364
- (@pypingou)       #365, Adjust the pagure processor for the new pagure message format
  https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/pull/365

Commits

- 6cabffc38 Fix this cgit test.
  https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/6cabffc38
- 3a0861851 Conglomerate irc meeting events (for fedora-hubs).
  https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/3a0861851
- a1d63ca68 Adjust the pagure processor for the new format of the fedmsg message sent
  https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/a1d63ca68
- 9ac1caf3f Adjust the pagure processor for PR comment editing
  https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/9ac1caf3f
- 8af38a1a4 Rename TestIssueCommentEditLegacy to TestIssueCommentEdit
  https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/8af38a1a4
- 25875edb6 Fix copr links.
  https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/25875edb6
- edfa5e688 Adjust the pagure processor for the new pagure message format
  https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/edfa5e688

0.15.10
-------

Pull Requests

- (@ralphbean)      #359, Fix situation where pagure messages have zero comments.
  https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/pull/359

Commits

- 34ff3a732 Fix situation where pagure messages have zero comments.
  https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/34ff3a732
- 15b507dd0 Typofix.
  https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/15b507dd0

0.15.9
------

Pull Requests

- (@ralphbean)      #357, Filter out None values from copr here.
  https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/pull/357
- (@ralphbean)      #358, Handle new mdapi format.
  https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/pull/358

Commits

- 9cb81048a Filter out None values from copr here.
  https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/9cb81048a
- 80d56e989 Handle new mdapi format.
  https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/80d56e989
- 5a077034d Typofix.
  https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/5a077034d

0.15.8
------

Pull Requests

- (@ralphbean)      #354, Handle edits to pagure issue comments.
  https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/pull/354
- (@ralphbean)      #355, Handle a whole slough of new squirely releng messages.
  https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/pull/355

Commits

- b5f03c760 Handle edits to pagure issue comments.
  https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/b5f03c760
- b67615175 Handle a whole slough of new squirely releng messages.
  https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/b67615175

0.15.7
------

Pull Requests

- (@ralphbean)      #349, Return package-centric information about taskotron events.
  https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/pull/349
- (@ralphbean)      #350, Make mailman activity look a little more interesting in gource.
  https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/pull/350
- (@ralphbean)      #351, Replace newlines with spaces for mailman subjects.
  https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/pull/351

Commits

- 166776c0d Return package-centric information about taskotron events.
  https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/166776c0d
- 9bcb39f0d Make mailman activity look a little more interesting in gource.
  https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/9bcb39f0d
- c9a8cb021 Whitespace.
  https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/c9a8cb021
- 3935f77fb Replace newlines with spaces for mailman subjects.
  https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/3935f77fb

0.15.6
------

Pull Requests

- (@ralphbean)      #343, Change text of mdapi subtitle.
  https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/pull/343
- (@ralphbean)      #344, Add some preliminary processors for the new pungi-koji compose stuff.
  https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/pull/344
- (@ralphbean)      #347, Remove the "markup" stuff.
  https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/pull/347
- (@ralphbean)      #346, Add a conglomerator for mailman3 messages.
  https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/pull/346
- (@ralphbean)      #348, Processor and handler for new nagios messages.
  https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/pull/348

Commits

- c82fd4c42 Change text of mdapi subtitle.
  https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/c82fd4c42
- 0982dc1d8 Remove +0/-0 text.
  https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/0982dc1d8
- 801309cd0 Add some preliminary processors for the new pungi-koji compose stuff.
  https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/801309cd0
- 559fe2685 More pungi-koji stuff.
  https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/559fe2685
- a4ee3be77 Use the new location field passed along by pungi-koji.
  https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/a4ee3be77
- ad0b2caa8 Add a conglomerator for mailman3 messages.
  https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/ad0b2caa8
- cbf328c66 Remove the "markup" stuff.
  https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/cbf328c66
- ffcda6d6b Processor and handler for new nagios messages.
  https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/ffcda6d6b
- abef89168 Forgotten setup.py line.
  https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/abef89168
- eb6f1faa6 Remove debug statement.
  https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/eb6f1faa6
- 295105785 Smash case, as per review.
  https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/295105785
- 5b5abb0b9 Fix subject stripping.
  https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/5b5abb0b9
- b9d36e25c Copyright years.
  https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/b9d36e25c
- d96c71f57 Cosmetic whitespace.
  https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/d96c71f57

0.15.5
------

Pull Requests

- (@ralphbean)      #325, Various fixes for autocloud.
  https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/pull/325
- (@ralphbean)      #327, New processor for two-week atomic releng messages.
  https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/pull/327
- (@ralphbean)      #324, Use aliases for bodhi links
  https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/pull/324
- (@ralphbean)      #328, Add links for bodhi buildroot overrides.
  https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/pull/328
- (@ralphbean)      #329, Handle github "deployment" messages.
  https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/pull/329
- (@ralphbean)      #331, Add a conglomerator for bodhi buildroot overrides.
  https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/pull/331
- (@puiterwijk)     #332, buildsys.py needs pytz
  https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/pull/332
- (@puiterwijk)     #333, Add github.issue.labeled subtitle
  https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/pull/333
- (@puiterwijk)     #334, If only status is updated, show status in subtitle
  https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/pull/334
- (@ralphbean)      #330, Add hardcoded avatars for some system users.
  https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/pull/330
- (@ralphbean)      #335, Add atomic icon for atomic messages.
  https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/pull/335
- (@pypingou)       #336, Add support and test for anitya's messages about flagged projects
  https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/pull/336
- (@ralphbean)      #339, Test and fix mailman3 archived-at links that are surrounded with arrow braces.
  https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/pull/339
- (@pypingou)       #341, Mdapi processor
  https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/pull/341

Commits

- f997d8649 Use aliases for bodhi links in the last few places where its missing.
  https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/f997d8649
- 1e775b208 pep8.
  https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/1e775b208
- dc66d39ee Various fixes for autocloud.
  https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/dc66d39ee
- 264d9620d New processor for two-week atomic releng messages.
  https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/264d9620d
- 4babded14 Add hardcoded avatars for some system users.
  https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/4babded14
- 1e786e1aa Add links for bodhi buildroot overrides.
  https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/1e786e1aa
- b8dd96e0a Handle github "deployment" messages.
  https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/b8dd96e0a
- b5b61f47b Add a conglomerator for bodhi buildroot overrides.
  https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/b5b61f47b
- a87f41591 Use nose to run the tests.
  https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/a87f41591
- 2cba8fac2 buildsys.py needs pytz
  https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/2cba8fac2
- 6f9635933 Add github.issue.labeled subtitle
  https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/6f9635933
- ca3ac00ff If only status is updated, show status in subtitle
  https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/ca3ac00ff
- f0dbe654c Add atomic icon for atomic messages.
  https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/f0dbe654c
- 1522086a5 Add support and test for anitya's messages about flagged projects
  https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/1522086a5
- f86f60d35 Fix the tests
  https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/f86f60d35
- a70d87f9c Fix the tests, again
  https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/a70d87f9c
- ba8804c41 Let's be forward compatible and support flag messages including the packages
  https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/ba8804c41
- 6ec90bb95 Fix typo and adjust the unit-tests to include tests with packages information
  https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/6ec90bb95
- 1be3b8078 When we have packages information, it should return them
  https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/1be3b8078
- 3fdde3e42 Test and fix mailman3 archived-at links that are surrounded with arrow braces.
  https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/3fdde3e42
- 0948044b5 Python3 support.
  https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/0948044b5
- b6ad013a3 Add the mdapi processor
  https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/b6ad013a3
- 3e9bc64a4 Add the mdapi unit-tests
  https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/3e9bc64a4
- 80361b9fe Fix build for py2.6
  https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/80361b9fe
- 6ac6207b9 Remove unused import.
  https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/6ac6207b9
- 78538f6bf Strip parenthetical suffix from package names.
  https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/78538f6bf
- e38703409 Some updates to mdapi.
  https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/e38703409
- b73c12380 Whitespace.
  https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/b73c12380

0.15.4
------

Pull Requests

- (@mkrizek)        #323, Add taskotron
  https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/pull/323

Commits

- a5db97622 Add taskotron
  https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/a5db97622
- 72a0ea692 Update example.patch from our latest cgit.
  https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/72a0ea692
- 4075781cb Add taskotron icon
  https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/4075781cb
- 8db04d202 Remove old CHANGELOG header.
  https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/8db04d202

0.15.3
------

Pull Requests

- (@ralphbean)      #321, Handle new "reason" from hotness.
  https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/pull/321
- (@pypingou)       #322, Change the wording from packager owner to maintainers
  https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/pull/322

Commits

- 0390e57d6 Handle new "reason" from hotness.
  https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/0390e57d6
- db97d9cc7 Leverage doc/requirements.txt
  https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/db97d9cc7
- 509a75b1c Change the wording from packager owner to maintainers
  https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/509a75b1c

0.15.2
------

Pull Requests

- (@sayanchowdhury) add Proccessor and Tests for autocloud `#317
  <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/pull/317>`_
- (@ralphbean)      Improve the doc with the list of topics. `#319
  <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/pull/319>`_
- (@ralphbean)      Add and test an infragit processor. `#318
  <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/pull/318>`_

Commits

- Fix a bodhi conglomerator link. `808ae1afc
  <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/808ae1afc>`_
- Add processor for autocloud messages. `24896c8c8
  <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/24896c8c8>`_
- add tests for autocloud `f47d351ff
  <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/f47d351ff>`_
- fix issues and and tests for autocloud `016e88bf0
  <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/016e88bf0>`_
- minor PEP8 fixes `6a6fd81df
  <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/6a6fd81df>`_
- fix the copyright year and holder `b0184c9e0
  <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/b0184c9e0>`_
- 1. change the test image name to Fedora-Cloud-Base 2. Add icon, secondary_icon along with tests 3. Fix link and tests for the link `0c09a135d
  <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/0c09a135d>`_
- Remove these unspecified tests. `c0429b06c
  <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/c0429b06c>`_
- Add and test an infragit processor. `7cd5a0d9e
  <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/7cd5a0d9e>`_
- Include links to datagrepper queries in the docs. `4c90530b5
  <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/4c90530b5>`_
- Check for Unspecified instead of None. `9d12cffe5
  <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/9d12cffe5>`_
- Use mako to make this way more awesome. `bc4aaed95
  <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/bc4aaed95>`_
- Turns out re2 doesn't even have a findall method... `7cf235bab
  <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/7cf235bab>`_

0.15.1
------

- Use badge.award 'description' in long_form `dbb892eb6 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/dbb892eb635154ffcd6bb9427436120991c8d775>`_
- Merge pull request #280 from pranavk/develop `1b0cf481f <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/1b0cf481f5f4699bf3deacce07ec741f649a58d3>`_
- Attempt to add titles to github PR/issue openings `649637393 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/649637393f21049120ba80304e528591f9d7bebe>`_
- Fix some syntax errors. `8ac39b3af <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/8ac39b3af0294c53c197d94b214293bc48510ef9>`_
- make tests pass `b2214a082 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/b2214a0820c1c69bd3d0b30e42c409062957c927>`_
- Merge pull request #282 from fedora-infra/issue-open-titles `d438f45d6 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/d438f45d6c2735b787b4761a5c051df8874032bb>`_
- Faster, please. `28170f2d9 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/28170f2d91678a98ee585746ae51e83595a77b13>`_
- Link directly to pagure comments. `633a39bbf <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/633a39bbfe3373eabbd7fbd79494d2d0fbd4c3ce>`_
- Merge pull request #283 from fedora-infra/feature/pagure-links `9d1feda98 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/9d1feda98397ba0ec02b1472354e34e78cd87381>`_
- Update language for pagure messages. `bd3da61ef <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/bd3da61efd0bf6a53c5f0621da3620a935f34dc1>`_
- Merge pull request #284 from fedora-infra/feature/pagure-language-changes `837191f7d <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/837191f7da987ec46885c2affac1ed3f40b902da>`_
- We should return a link... for #link things in irc meetings. `2b0ad74ab <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/2b0ad74ab30231c49c2f282d8308f1c131dca7a6>`_
- Remove spurious print statement. `f1748ed76 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/f1748ed7682c4202bd43e9fcfdad879b23c72563>`_
- Merge pull request #285 from fedora-infra/feature/link-link `8e3e2128c <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/8e3e2128c32f2584b8e6af78787c97391adb9a86>`_
- Update Koschei URL `4e08316e3 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/4e08316e3a206680584bddc36b6f096a71635c9a>`_
- Merge pull request #287 from mizdebsk/koschei `634098d16 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/634098d167c8dc7216094bd2ea65a8d85c7d6ca6>`_
- Adjust the docstring to reflect the test `2aef1ebcd <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/2aef1ebcdba69559e898fcc9f075fb5050cba36f>`_
- Add logic to process messages sent by pkgdb when changing the koschei monitoring flag `554038f11 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/554038f1133f5fdc4937eea864773fc5ec441501>`_
- Add unit-tests for the message sent by pkgdb when updating the koschei monitoring flag `97351e2f7 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/97351e2f7c2b125f3964786201d2585d1e7d4503>`_
- Add missing space to make the link work properly `43664879c <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/43664879ce6af5daf2fc076cf488e281ac76fb70>`_
- Add test message of a failed scratch build with information about the target `ba65c7241 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/ba65c72414c4dacf3a7d330a58939f436c326fff>`_
- Specify the target of the build if we can extract it from the message `a60706c22 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/a60706c22cfa47e26aa4cc48d7b0e1e985af7984>`_
- Merge pull request #288 from fedora-infra/pkgdb_koschei `2a3066914 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/2a3066914f9a5f1fe21fd59ee15f959c876b80e9>`_
- Merge pull request #289 from fedora-infra/scratch_with_target `79294105f <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/79294105ffb9377af3692679c82369a4d091212c>`_
- Careful for x-archived-at being None. `92e77072a <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/92e77072a61a57385df5a40822dd8e32a0d90b84>`_
- Fix grammar for github.pull_request.synchronize `42df2c3d4 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/42df2c3d4b92e108c96c1e3f33d43ee21ca99504>`_
- Merge pull request #290 from fedora-infra/synchronize-past-tense `7a1c74a81 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/7a1c74a81ec1ec1d631e662dffa0a971171def01>`_
- Update pagure comment links. `b23e24247 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/b23e242473d749ed7c1256981d2cbce5dea04ab1>`_
- Merge pull request #292 from fedora-infra/feature/pagure-link `60b33fe40 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/60b33fe4029c5739b8fa6eaaf058c1841324a41c>`_
- Ansible conglomerator (for fedora-hubs) `6a1d55773 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/6a1d55773ea33902cbebd94d3ef8fc5423e7ce01>`_
- Handle case where constituents have been pre-filtered. `e8e760e0e <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/e8e760e0e0361cbf6cffad5133f0db6c57b13b84>`_
- Tagger conglomerator (for fedora-hubs) `6e6202e39 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/6e6202e39804be3ac64db2e8badec5aecb4390ad>`_
- Consistency. `ec985c8d0 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/ec985c8d0f9910f533b0c3f303deaee5cb4673d9>`_
- Remove duplicate declaration. `ef62ab93e <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/ef62ab93e6002fa2f7e35fa495eec2b217ef8ea8>`_
- Merge pull request #294 from fedora-infra/feature/tagger-conglomerator `8a70eb667 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/8a70eb6671567fb37864ef641822310d42f3b97a>`_
- Drop hardcoding of humanized time in the test. `4eb882116 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/4eb882116db88926d8862d2d7702d26227b99d03>`_
- Try to handle all these plural cases. `c55e09523 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/c55e09523adc135b7c79b9e6eecb1374c1775267>`_
- Merge pull request #293 from fedora-infra/feature/ansible-conglomerator `9cf772c48 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/9cf772c48bb68ad4cbf95b77b554f54ec70c69d8>`_
- 0.5.10 `3bc79cebf <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/3bc79cebf66a9c42aaa06cd78aa96941055a445f>`_
- Fix incorrect key. `8e33726e0 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/8e33726e0ca3fa8597d4ea46659d3ff8732377a6>`_
- Merge pull request #295 from fedora-infra/feature/mm2-fix `43f26b3af <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/43f26b3af8563909806193fa934d31ecc443f897>`_
- Remove hardcoded relative time from tests. `435080a85 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/435080a85579bbd79d7ebafcd6f0d2bd3032fce0>`_
- Copr conglomerator. `7c7fdce89 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/7c7fdce89753a77a87e87eebf126d39f11998b03>`_
- Merge pull request #296 from fedora-infra/feature/copr-conglomerators `a4874f254 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/a4874f2547141cde45e338afe614677e69a61a5c>`_
- Protect ourselves from lists. `8ecfad370 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/8ecfad3709de3f94745a7aa37388b8fbccf97a43>`_
- Merge pull request #297 from fedora-infra/feature/buildsys-fix-weirdness `7b82342ab <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/7b82342ab7c8e7f89835d6598346c4b96b1bbbaf>`_
- 0.5.11 `9a2b24c52 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/9a2b24c52160956c1d00b84099e7531e0aec3d21>`_
- Update copr urls `ad8a1092b <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/ad8a1092b759adebf765939a18c1bf9134bc916e>`_
- Fix #96  "in advance of" should read "newer than" `684c98411 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/684c984118c52126154ad4b03bacf1497635a4b9>`_
- Update tests `facff07e6 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/facff07e62f74251c72eae2cea73441c2f3df365>`_
- Be still more careful with this mm2 field. `7a6a3e161 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/7a6a3e161f7f0cff08eaa52b201fe387b9287994>`_
- Merge pull request #299 from vhalli/develop `6d5f2f800 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/6d5f2f800f8fb4a8bab6369e447923bdc21c2e65>`_
- Merge pull request #300 from fedora-infra/feature/mm2-fix-again `883b464dc <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/883b464dcd31fead4391df14a6f5b42b658382f3>`_
- Merge pull request #298 from opoplawski/copr `ec625c4aa <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/ec625c4aa086fd481873f83ed35d718725bf70e0>`_
- Rename this to Legacy so it gets hidden from the html docs. `d9a8a3c0f <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/d9a8a3c0f93fae6e7cb4cbca7fc2e110f06e741f>`_
- Adjust this to match. `c6ad8b491 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/c6ad8b4917f54f13247d444f196ea1ffb45ff075>`_
- Fix for #277 unhandled 'pagure.issue.drop' messages `1f727829a <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/1f727829aeac4bc102a9ceba67a8b826d301f6a9>`_
- Merge pull request #301 from Ghost-script/Fix `7ed111ccc <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/7ed111ccc2804827b10dbd0db48971640b30eb3f>`_
- Handle a case where there is a different nested message for the-new-hotness. `e39da1936 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/e39da193613680d5de9474fdacd2b8061f964c5e>`_
- Merge pull request #303 from fedora-infra/feature/handle-another-hotness-case `57bfb6ec3 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/57bfb6ec38cc01dbad1d250bdf3a3e8546d31121>`_
- Be **extra** careful. `edc7e61db <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/edc7e61db2e4eb02719136c2ebe4c87a0cd4b5d2>`_
- Merge pull request #304 from fedora-infra/feature/extra-careful `0f1f01a9e <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/0f1f01a9e1dc603da537332a341eb7e9f3b217a4>`_
- Update conglomerators for fedmsg API change. `e50a2b823 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/e50a2b823885ac1fe3939979ef52b1900b5a3f5e>`_
- Processor for bodhi.masher.start `4df2b4247 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/4df2b42471886333a9a7946a3f9a04234b23e781>`_
- Truncate bodhi update titles when they're ridiculous long. `055d24de0 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/055d24de0aef5f3fecb8436e22dd8449dac31a98>`_
- Merge pull request #309 from fedora-infra/feature/truncate-update-title `056b867e8 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/056b867e8194036895196670460fe39638ce6112>`_
- Merge pull request #308 from fedora-infra/feature/bodhi-mash-start `181db5834 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/181db5834d733fc699d95c0da9c44a01c0cf19ef>`_
- Merge pull request #305 from fedora-infra/feature/subjective-conglomeration `ef932e552 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/ef932e552740ae7bc2cdc248551684f1d26b3965>`_
- Handle edge-case in copr conglomerator. `f759b6c0c <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/f759b6c0c891fb8d82ac0e960a0a49652870e6ac>`_
- 0.15.0 `c0039fb20 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/c0039fb20b080c2697b64e67f9fb4d0404ca8603>`_
- Fix links for bodhi2. `4c245b36d <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/4c245b36d3fc21df20bc8afd1db9f2b044e1461c>`_
- Merge pull request #315 from fedora-infra/feature/bodhi-links `23d65d33d <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/23d65d33d3821da0957f334a9830060c9d944047>`_

0.5.9
-----

- Add support for pagure's message about commits `180899ccc <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/180899cccd6950cd8930ac574fc8d13997639236>`_
- User email2fas to be a little more FAS' username friendly `2aac21a45 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/2aac21a45a69fe8f06804eb841472564957e80ad>`_
- Merge pull request #276 from fedora-infra/more_pagure `a7570d83a <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/a7570d83a193f7f7f42e6ff4fde2e342206337c8>`_
- 0.5.9 `fd241927e <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/fd241927ef852979c0ab227d7b508b247be69a7e>`_

0.5.8
-----

- Try to avoid pagure exceptions for some unhandled message type. `6488cea86 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/6488cea8620c97a1e6b6a8abc4846bc9dec69ed9>`_
- Merge pull request #274 from fedora-infra/feature/dance-around-pagure `494ca8edd <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/494ca8edda22469554edae6e02e5474d752ea96f>`_

0.5.7
-----

- Fix problems with pagure processor and test suite. `de7fc3f22 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/de7fc3f2264ab9e39d36070d76fafd83a848b43c>`_
- Merge pull request #273 from fedora-infra/feature/fix-pagure-tests `e5096fd5f <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/e5096fd5f9668bfabc039520a13535bfd116f5f7>`_

0.5.6
-----

- Fix pagure regex. `6b451b01b <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/6b451b01b7c2043f92f46ef59349edb2e2a46841>`_
- Merge pull request #269 from fedora-infra/feature/pagure-regex `99da5003c <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/99da5003ce7395c5795e0e53967417d0a8e1d942>`_
- Add arrow for the travis tests. `dc9b9a2a5 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/dc9b9a2a5f2e2aa550d15fca1212bfb0c81bcaa0>`_
- Fix a typo in the FAF processor. `ed6798fb8 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/ed6798fb8dbb0417f4e71f1b24092f57d13304ef>`_
- Merge pull request #270 from fedora-infra/feature/typofix `ac080c469 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/ac080c469da14ac2f08ab33812fb34d09a7cada2>`_
- Update Koschei icon link `4e4f33824 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/4e4f33824bcf993d96c138364dfce871ef935f96>`_
- Merge pull request #271 from msimacek/feature/koschei-icon `aae60812a <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/aae60812a91e86ad8a41bc0fdd583acd085545bf>`_
- Add logic for the pagure's PR.flag.added and PR.flag.updated messages `ea86921ae <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/ea86921ae03d8cf5d485ae0acaccad9c9e41eb9e>`_
- Add unit-tests for pagure's PR.flag.added and PR.flag.updated messages `d37d61010 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/d37d6101014a0bf616c603187f2f85e73a36afa0>`_
- Adjust the subtitle as per @ralphbean's suggestions `86ec32958 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/86ec32958ca0914a1cfd9df52d939775654968a6>`_
- Merge pull request #272 from fedora-infra/pagure_flags `e9b580933 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/e9b580933f744e6cefa43267e59b64e090eb58d7>`_

0.5.5
-----

- Fix syntax errors. `05452d49c <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/05452d49cfeca05ce21bc30f8a6b688f37201076>`_

0.5.4
-----

- shorten Fedimg messages `31f79d788 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/31f79d788f4c09cbf8b60671120428d0869e7a00>`_
- remove deprecated comment `ec3e8afac <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/ec3e8afac0071b528edb186b2a5cea249fce9199>`_
- add this missing tmpl line `a7da68284 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/a7da68284846347b07f3a1553a598430d0b12813>`_
- print extra details for fedimg actions when applicable `c78bde198 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/c78bde198a7cdaf4f385af1d51720444180dd91a>`_
- update tests for new extra dict in fedimg output `7e0ccafa3 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/7e0ccafa3732f96c8ca267112321662620ff33fd>`_
- tests: test for fedimg task complete message `14e3abea2 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/14e3abea2e647368e24d035b18c0639240d79107>`_
- typofix `bd845a291 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/bd845a2913706e1071967ad6a75a5877c528fc17>`_
- tests: there should be this icon here `9c07cba0e <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/9c07cba0e3f7bb930b92a6903a76740c211512f5>`_
- expand on the fedimg docstrings in the tests `0c3293715 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/0c32937156fd8977434be26a5ae156f53893bbde>`_
- oops -- need icons here, too `39d97f5dd <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/39d97f5dd401eb98da85ab71973344d3470dfcee>`_
- tests: add some expected objects for Fedimg `8458c011a <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/8458c011aa79c7a95744dd70b293c8a656c9c1b8>`_
- tests: missed tmpl assignment `cfe9ed6fb <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/cfe9ed6fbdc285dbac5d8fb075ce67f60bb9c18b>`_
- fedimg: refactor subtitle code a bit (fedimg tests run now) `6bc60607d <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/6bc60607da2fa98852b88b553857faba2a81352f>`_
- fedimg docstrings: s/awarded/published/g `3599044af <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/3599044af53c290804baf0ae5057f57ca16aa81c>`_
- Merge pull request #260 from fedora-infra/feature/improve-fedimg-details `8ba23df1e <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/8ba23df1e9f2747544ded447ffba2bb63be784a9>`_
- Extract the "package" from inconsistent admin action messages in a consistent way. `fa2d9a2b1 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/fa2d9a2b1dd29fe3c2636c5bb5c663ef4ac5673d>`_
- Merge pull request #267 from fedora-infra/feature/admin-action-fix `5144e9f1d <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/5144e9f1dc97e6452839f1f87fda5334e9ef4afe>`_

0.5.3
-----

- Try to make admin actions more understandable. `1b7508962 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/1b75089623fa375808a94a4fc3d40f8c06013ac5>`_
- Careful that there is no "agent" field. `1a7485e6e <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/1a7485e6ecc2efdc5fdf82287b5ec828d442694d>`_
- Merge pull request #262 from fedora-infra/feature/admin-actions-redux `68e1febe2 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/68e1febe2f5c48105368181135d608a667e56df5>`_
- Merge pull request #264 from fedora-infra/feature/scm-no-agent `98c969cda <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/98c969cdad1fe123da8344a7937fffa778215b9f>`_
- Fix broken links to election events. `0f2983b15 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/0f2983b1504eef39256185bbeea112f931d33224>`_
- Merge pull request #265 from fedora-infra/feature/voting-link `082a6ca76 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/082a6ca761ccf62f8bae2986d50515a985f04c67>`_
- Handle fp.o addresses. `8fcca42b0 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/8fcca42b02653085ae955482d96d68aaac3aa5a6>`_
- Merge pull request #266 from fedora-infra/feature/fp-o-addresses `8674c71cb <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/8674c71cbc9b9f95ab1fff89bb9ea9176a4e18c4>`_

0.5.2
-----

- shorten Fedimg messages `31f79d788 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/31f79d788f4c09cbf8b60671120428d0869e7a00>`_
- remove deprecated comment `ec3e8afac <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/ec3e8afac0071b528edb186b2a5cea249fce9199>`_
- add this missing tmpl line `a7da68284 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/a7da68284846347b07f3a1553a598430d0b12813>`_
- print extra details for fedimg actions when applicable `c78bde198 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/c78bde198a7cdaf4f385af1d51720444180dd91a>`_
- update tests for new extra dict in fedimg output `7e0ccafa3 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/7e0ccafa3732f96c8ca267112321662620ff33fd>`_
- tests: test for fedimg task complete message `14e3abea2 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/14e3abea2e647368e24d035b18c0639240d79107>`_
- Try to make admin actions more understandable. `1b7508962 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/1b75089623fa375808a94a4fc3d40f8c06013ac5>`_
- Careful that there is no "agent" field. `1a7485e6e <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/1a7485e6ecc2efdc5fdf82287b5ec828d442694d>`_
- Merge pull request #262 from fedora-infra/feature/admin-actions-redux `68e1febe2 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/68e1febe2f5c48105368181135d608a667e56df5>`_
- Merge pull request #264 from fedora-infra/feature/scm-no-agent `98c969cda <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/98c969cdad1fe123da8344a7937fffa778215b9f>`_
- Fix broken links to election events. `0f2983b15 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/0f2983b1504eef39256185bbeea112f931d33224>`_
- Merge pull request #265 from fedora-infra/feature/voting-link `082a6ca76 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/082a6ca761ccf62f8bae2986d50515a985f04c67>`_
- Handle fp.o addresses. `8fcca42b0 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/8fcca42b02653085ae955482d96d68aaac3aa5a6>`_
- Merge pull request #266 from fedora-infra/feature/fp-o-addresses `8674c71cb <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/8674c71cbc9b9f95ab1fff89bb9ea9176a4e18c4>`_
- 0.5.3 `7b220635f <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/7b220635ffc04b989844d2e2fe5e1031baa5b4cc>`_
- typofix `bd845a291 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/bd845a2913706e1071967ad6a75a5877c528fc17>`_
- tests: there should be this icon here `9c07cba0e <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/9c07cba0e3f7bb930b92a6903a76740c211512f5>`_
- expand on the fedimg docstrings in the tests `0c3293715 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/0c32937156fd8977434be26a5ae156f53893bbde>`_
- oops -- need icons here, too `39d97f5dd <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/39d97f5dd401eb98da85ab71973344d3470dfcee>`_
- tests: add some expected objects for Fedimg `8458c011a <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/8458c011aa79c7a95744dd70b293c8a656c9c1b8>`_
- tests: missed tmpl assignment `cfe9ed6fb <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/cfe9ed6fbdc285dbac5d8fb075ce67f60bb9c18b>`_
- fedimg: refactor subtitle code a bit (fedimg tests run now) `6bc60607d <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/6bc60607da2fa98852b88b553857faba2a81352f>`_
- fedimg docstrings: s/awarded/published/g `3599044af <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/3599044af53c290804baf0ae5057f57ca16aa81c>`_
- Merge pull request #260 from fedora-infra/feature/improve-fedimg-details `8ba23df1e <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/8ba23df1e9f2747544ded447ffba2bb63be784a9>`_
- Extract the "package" from inconsistent admin action messages in a consistent way. `fa2d9a2b1 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/fa2d9a2b1dd29fe3c2636c5bb5c663ef4ac5673d>`_
- Merge pull request #267 from fedora-infra/feature/admin-action-fix `5144e9f1d <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/5144e9f1dc97e6452839f1f87fda5334e9ef4afe>`_
- 0.5.4 `ec1894aa0 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/ec1894aa0542caed2ca88790cabcc34f6b21866a>`_
- Fix syntax errors. `05452d49c <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/05452d49cfeca05ce21bc30f8a6b688f37201076>`_
- 0.5.5 `20f0a7fde <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/20f0a7fdeb22be4d17ae449cfc2a67546333dfff>`_
- Fix pagure regex. `6b451b01b <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/6b451b01b7c2043f92f46ef59349edb2e2a46841>`_
- Merge pull request #269 from fedora-infra/feature/pagure-regex `99da5003c <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/99da5003ce7395c5795e0e53967417d0a8e1d942>`_
- Add arrow for the travis tests. `dc9b9a2a5 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/dc9b9a2a5f2e2aa550d15fca1212bfb0c81bcaa0>`_
- Fix a typo in the FAF processor. `ed6798fb8 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/ed6798fb8dbb0417f4e71f1b24092f57d13304ef>`_
- Merge pull request #270 from fedora-infra/feature/typofix `ac080c469 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/ac080c469da14ac2f08ab33812fb34d09a7cada2>`_
- Update Koschei icon link `4e4f33824 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/4e4f33824bcf993d96c138364dfce871ef935f96>`_
- Merge pull request #271 from msimacek/feature/koschei-icon `aae60812a <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/aae60812a91e86ad8a41bc0fdd583acd085545bf>`_
- Add logic for the pagure's PR.flag.added and PR.flag.updated messages `ea86921ae <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/ea86921ae03d8cf5d485ae0acaccad9c9e41eb9e>`_
- Add unit-tests for pagure's PR.flag.added and PR.flag.updated messages `d37d61010 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/d37d6101014a0bf616c603187f2f85e73a36afa0>`_
- Adjust the subtitle as per @ralphbean's suggestions `86ec32958 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/86ec32958ca0914a1cfd9df52d939775654968a6>`_
- Merge pull request #272 from fedora-infra/pagure_flags `e9b580933 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/e9b580933f744e6cefa43267e59b64e090eb58d7>`_
- 0.5.6 `f614770e5 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/f614770e534b212d4e1ea547d7be50ef9562f044>`_
- Fix problems with pagure processor and test suite. `de7fc3f22 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/de7fc3f2264ab9e39d36070d76fafd83a848b43c>`_
- Merge pull request #273 from fedora-infra/feature/fix-pagure-tests `e5096fd5f <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/e5096fd5f9668bfabc039520a13535bfd116f5f7>`_
- 0.5.7 `d2db17c2b <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/d2db17c2b117dc018dc8e5c4076dfa982690fe11>`_
- Try to avoid pagure exceptions for some unhandled message type. `6488cea86 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/6488cea8620c97a1e6b6a8abc4846bc9dec69ed9>`_
- Merge pull request #274 from fedora-infra/feature/dance-around-pagure `494ca8edd <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/494ca8edda22469554edae6e02e5474d752ea96f>`_
- 0.5.8 `a42949a58 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/a42949a58e0f9bbf637eab05d018e8cc4da6a96d>`_
- Add support for pagure's message about commits `180899ccc <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/180899cccd6950cd8930ac574fc8d13997639236>`_
- User email2fas to be a little more FAS' username friendly `2aac21a45 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/2aac21a45a69fe8f06804eb841472564957e80ad>`_
- Merge pull request #276 from fedora-infra/more_pagure `a7570d83a <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/a7570d83a193f7f7f42e6ff4fde2e342206337c8>`_
- 0.5.9 `fd241927e <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/fd241927ef852979c0ab227d7b508b247be69a7e>`_
- 0.5.9 `28d44e3d3 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/28d44e3d31dfec7a71785fb3049d55d833d0fb16>`_
- Use badge.award 'description' in long_form `dbb892eb6 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/dbb892eb635154ffcd6bb9427436120991c8d775>`_
- Merge pull request #280 from pranavk/develop `1b0cf481f <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/1b0cf481f5f4699bf3deacce07ec741f649a58d3>`_
- Attempt to add titles to github PR/issue openings `649637393 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/649637393f21049120ba80304e528591f9d7bebe>`_
- Fix some syntax errors. `8ac39b3af <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/8ac39b3af0294c53c197d94b214293bc48510ef9>`_
- make tests pass `b2214a082 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/b2214a0820c1c69bd3d0b30e42c409062957c927>`_
- Merge pull request #282 from fedora-infra/issue-open-titles `d438f45d6 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/d438f45d6c2735b787b4761a5c051df8874032bb>`_
- Faster, please. `28170f2d9 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/28170f2d91678a98ee585746ae51e83595a77b13>`_
- Link directly to pagure comments. `633a39bbf <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/633a39bbfe3373eabbd7fbd79494d2d0fbd4c3ce>`_
- Merge pull request #283 from fedora-infra/feature/pagure-links `9d1feda98 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/9d1feda98397ba0ec02b1472354e34e78cd87381>`_
- Update language for pagure messages. `bd3da61ef <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/bd3da61efd0bf6a53c5f0621da3620a935f34dc1>`_
- Merge pull request #284 from fedora-infra/feature/pagure-language-changes `837191f7d <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/837191f7da987ec46885c2affac1ed3f40b902da>`_
- We should return a link... for #link things in irc meetings. `2b0ad74ab <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/2b0ad74ab30231c49c2f282d8308f1c131dca7a6>`_
- Remove spurious print statement. `f1748ed76 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/f1748ed7682c4202bd43e9fcfdad879b23c72563>`_
- Merge pull request #285 from fedora-infra/feature/link-link `8e3e2128c <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/8e3e2128c32f2584b8e6af78787c97391adb9a86>`_
- Update Koschei URL `4e08316e3 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/4e08316e3a206680584bddc36b6f096a71635c9a>`_
- Merge pull request #287 from mizdebsk/koschei `634098d16 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/634098d167c8dc7216094bd2ea65a8d85c7d6ca6>`_
- Adjust the docstring to reflect the test `2aef1ebcd <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/2aef1ebcdba69559e898fcc9f075fb5050cba36f>`_
- Add logic to process messages sent by pkgdb when changing the koschei monitoring flag `554038f11 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/554038f1133f5fdc4937eea864773fc5ec441501>`_
- Add unit-tests for the message sent by pkgdb when updating the koschei monitoring flag `97351e2f7 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/97351e2f7c2b125f3964786201d2585d1e7d4503>`_
- Add missing space to make the link work properly `43664879c <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/43664879ce6af5daf2fc076cf488e281ac76fb70>`_
- Add test message of a failed scratch build with information about the target `ba65c7241 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/ba65c72414c4dacf3a7d330a58939f436c326fff>`_
- Specify the target of the build if we can extract it from the message `a60706c22 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/a60706c22cfa47e26aa4cc48d7b0e1e985af7984>`_
- Merge pull request #288 from fedora-infra/pkgdb_koschei `2a3066914 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/2a3066914f9a5f1fe21fd59ee15f959c876b80e9>`_
- Merge pull request #289 from fedora-infra/scratch_with_target `79294105f <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/79294105ffb9377af3692679c82369a4d091212c>`_
- Careful for x-archived-at being None. `92e77072a <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/92e77072a61a57385df5a40822dd8e32a0d90b84>`_
- Fix grammar for github.pull_request.synchronize `42df2c3d4 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/42df2c3d4b92e108c96c1e3f33d43ee21ca99504>`_
- Merge pull request #290 from fedora-infra/synchronize-past-tense `7a1c74a81 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/7a1c74a81ec1ec1d631e662dffa0a971171def01>`_
- Update pagure comment links. `b23e24247 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/b23e242473d749ed7c1256981d2cbce5dea04ab1>`_
- Merge pull request #292 from fedora-infra/feature/pagure-link `60b33fe40 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/60b33fe4029c5739b8fa6eaaf058c1841324a41c>`_
- Ansible conglomerator (for fedora-hubs) `6a1d55773 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/6a1d55773ea33902cbebd94d3ef8fc5423e7ce01>`_
- Handle case where constituents have been pre-filtered. `e8e760e0e <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/e8e760e0e0361cbf6cffad5133f0db6c57b13b84>`_
- Tagger conglomerator (for fedora-hubs) `6e6202e39 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/6e6202e39804be3ac64db2e8badec5aecb4390ad>`_
- Consistency. `ec985c8d0 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/ec985c8d0f9910f533b0c3f303deaee5cb4673d9>`_
- Remove duplicate declaration. `ef62ab93e <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/ef62ab93e6002fa2f7e35fa495eec2b217ef8ea8>`_
- Merge pull request #294 from fedora-infra/feature/tagger-conglomerator `8a70eb667 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/8a70eb6671567fb37864ef641822310d42f3b97a>`_
- Drop hardcoding of humanized time in the test. `4eb882116 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/4eb882116db88926d8862d2d7702d26227b99d03>`_
- Try to handle all these plural cases. `c55e09523 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/c55e09523adc135b7c79b9e6eecb1374c1775267>`_
- Merge pull request #293 from fedora-infra/feature/ansible-conglomerator `9cf772c48 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/9cf772c48bb68ad4cbf95b77b554f54ec70c69d8>`_
- 0.5.10 `3bc79cebf <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/3bc79cebf66a9c42aaa06cd78aa96941055a445f>`_
- Fix incorrect key. `8e33726e0 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/8e33726e0ca3fa8597d4ea46659d3ff8732377a6>`_
- Merge pull request #295 from fedora-infra/feature/mm2-fix `43f26b3af <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/43f26b3af8563909806193fa934d31ecc443f897>`_
- Remove hardcoded relative time from tests. `435080a85 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/435080a85579bbd79d7ebafcd6f0d2bd3032fce0>`_
- Copr conglomerator. `7c7fdce89 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/7c7fdce89753a77a87e87eebf126d39f11998b03>`_
- Merge pull request #296 from fedora-infra/feature/copr-conglomerators `a4874f254 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/a4874f2547141cde45e338afe614677e69a61a5c>`_
- Protect ourselves from lists. `8ecfad370 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/8ecfad3709de3f94745a7aa37388b8fbccf97a43>`_
- Merge pull request #297 from fedora-infra/feature/buildsys-fix-weirdness `7b82342ab <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/7b82342ab7c8e7f89835d6598346c4b96b1bbbaf>`_

0.5.11
------

- Fix incorrect key. `8e33726e0 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/8e33726e0ca3fa8597d4ea46659d3ff8732377a6>`_
- Merge pull request #295 from fedora-infra/feature/mm2-fix `43f26b3af <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/43f26b3af8563909806193fa934d31ecc443f897>`_
- Remove hardcoded relative time from tests. `435080a85 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/435080a85579bbd79d7ebafcd6f0d2bd3032fce0>`_
- Copr conglomerator. `7c7fdce89 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/7c7fdce89753a77a87e87eebf126d39f11998b03>`_
- Merge pull request #296 from fedora-infra/feature/copr-conglomerators `a4874f254 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/a4874f2547141cde45e338afe614677e69a61a5c>`_
- Protect ourselves from lists. `8ecfad370 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/8ecfad3709de3f94745a7aa37388b8fbccf97a43>`_
- Merge pull request #297 from fedora-infra/feature/buildsys-fix-weirdness `7b82342ab <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/7b82342ab7c8e7f89835d6598346c4b96b1bbbaf>`_

0.5.10
------

- Added tests for "fmn.rule.update" `22e424de0 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/22e424de0867369917fd9afe49083bf8bb26aac9>`_
- shorten Fedimg messages `31f79d788 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/31f79d788f4c09cbf8b60671120428d0869e7a00>`_
- remove deprecated comment `ec3e8afac <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/ec3e8afac0071b528edb186b2a5cea249fce9199>`_
- add this missing tmpl line `a7da68284 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/a7da68284846347b07f3a1553a598430d0b12813>`_
- print extra details for fedimg actions when applicable `c78bde198 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/c78bde198a7cdaf4f385af1d51720444180dd91a>`_
- update tests for new extra dict in fedimg output `7e0ccafa3 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/7e0ccafa3732f96c8ca267112321662620ff33fd>`_
- tests: test for fedimg task complete message `14e3abea2 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/14e3abea2e647368e24d035b18c0639240d79107>`_
- Merge pull request #257 from Ghost-script/bug247 `0b1d4ea22 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/0b1d4ea221133d09ab460561cc48855d2226c405>`_
- FAF (ABRT server) processor with tests `f08878aa5 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/f08878aa5ea081379874aa4bc0d7e98e62ac43f3>`_
- Merge pull request #259 from mbrysa/faf `19cc66e50 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/19cc66e50d57957826c6e3951c72705c628a9255>`_
- Sometimes, there is no blog post title. `706fdf3ee <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/706fdf3ee130f6df2b3eec298007368994c99a2b>`_
- Merge pull request #261 from fedora-infra/feature/no-planet-title `1cb772115 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/1cb77211559aab2b9a7318492d9699f5fb131d08>`_
- 0.5.2 `052ce32e7 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/052ce32e7806dcea41defca8051900122270221f>`_
- Try to make admin actions more understandable. `1b7508962 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/1b75089623fa375808a94a4fc3d40f8c06013ac5>`_
- Careful that there is no "agent" field. `1a7485e6e <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/1a7485e6ecc2efdc5fdf82287b5ec828d442694d>`_
- Merge pull request #262 from fedora-infra/feature/admin-actions-redux `68e1febe2 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/68e1febe2f5c48105368181135d608a667e56df5>`_
- Merge pull request #264 from fedora-infra/feature/scm-no-agent `98c969cda <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/98c969cdad1fe123da8344a7937fffa778215b9f>`_
- Fix broken links to election events. `0f2983b15 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/0f2983b1504eef39256185bbeea112f931d33224>`_
- Merge pull request #265 from fedora-infra/feature/voting-link `082a6ca76 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/082a6ca761ccf62f8bae2986d50515a985f04c67>`_
- Handle fp.o addresses. `8fcca42b0 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/8fcca42b02653085ae955482d96d68aaac3aa5a6>`_
- Merge pull request #266 from fedora-infra/feature/fp-o-addresses `8674c71cb <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/8674c71cbc9b9f95ab1fff89bb9ea9176a4e18c4>`_
- 0.5.3 `7b220635f <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/7b220635ffc04b989844d2e2fe5e1031baa5b4cc>`_
- typofix `bd845a291 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/bd845a2913706e1071967ad6a75a5877c528fc17>`_
- tests: there should be this icon here `9c07cba0e <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/9c07cba0e3f7bb930b92a6903a76740c211512f5>`_
- expand on the fedimg docstrings in the tests `0c3293715 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/0c32937156fd8977434be26a5ae156f53893bbde>`_
- oops -- need icons here, too `39d97f5dd <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/39d97f5dd401eb98da85ab71973344d3470dfcee>`_
- tests: add some expected objects for Fedimg `8458c011a <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/8458c011aa79c7a95744dd70b293c8a656c9c1b8>`_
- tests: missed tmpl assignment `cfe9ed6fb <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/cfe9ed6fbdc285dbac5d8fb075ce67f60bb9c18b>`_
- fedimg: refactor subtitle code a bit (fedimg tests run now) `6bc60607d <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/6bc60607da2fa98852b88b553857faba2a81352f>`_
- fedimg docstrings: s/awarded/published/g `3599044af <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/3599044af53c290804baf0ae5057f57ca16aa81c>`_
- Merge pull request #260 from fedora-infra/feature/improve-fedimg-details `8ba23df1e <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/8ba23df1e9f2747544ded447ffba2bb63be784a9>`_
- Extract the "package" from inconsistent admin action messages in a consistent way. `fa2d9a2b1 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/fa2d9a2b1dd29fe3c2636c5bb5c663ef4ac5673d>`_
- Merge pull request #267 from fedora-infra/feature/admin-action-fix `5144e9f1d <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/5144e9f1dc97e6452839f1f87fda5334e9ef4afe>`_
- 0.5.4 `ec1894aa0 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/ec1894aa0542caed2ca88790cabcc34f6b21866a>`_
- Fix syntax errors. `05452d49c <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/05452d49cfeca05ce21bc30f8a6b688f37201076>`_
- 0.5.5 `20f0a7fde <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/20f0a7fdeb22be4d17ae449cfc2a67546333dfff>`_
- Fix pagure regex. `6b451b01b <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/6b451b01b7c2043f92f46ef59349edb2e2a46841>`_
- Merge pull request #269 from fedora-infra/feature/pagure-regex `99da5003c <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/99da5003ce7395c5795e0e53967417d0a8e1d942>`_
- Add arrow for the travis tests. `dc9b9a2a5 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/dc9b9a2a5f2e2aa550d15fca1212bfb0c81bcaa0>`_
- Fix a typo in the FAF processor. `ed6798fb8 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/ed6798fb8dbb0417f4e71f1b24092f57d13304ef>`_
- Merge pull request #270 from fedora-infra/feature/typofix `ac080c469 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/ac080c469da14ac2f08ab33812fb34d09a7cada2>`_
- Update Koschei icon link `4e4f33824 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/4e4f33824bcf993d96c138364dfce871ef935f96>`_
- Merge pull request #271 from msimacek/feature/koschei-icon `aae60812a <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/aae60812a91e86ad8a41bc0fdd583acd085545bf>`_
- Add logic for the pagure's PR.flag.added and PR.flag.updated messages `ea86921ae <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/ea86921ae03d8cf5d485ae0acaccad9c9e41eb9e>`_
- Add unit-tests for pagure's PR.flag.added and PR.flag.updated messages `d37d61010 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/d37d6101014a0bf616c603187f2f85e73a36afa0>`_
- Adjust the subtitle as per @ralphbean's suggestions `86ec32958 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/86ec32958ca0914a1cfd9df52d939775654968a6>`_
- Merge pull request #272 from fedora-infra/pagure_flags `e9b580933 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/e9b580933f744e6cefa43267e59b64e090eb58d7>`_
- 0.5.6 `f614770e5 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/f614770e534b212d4e1ea547d7be50ef9562f044>`_
- Fix problems with pagure processor and test suite. `de7fc3f22 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/de7fc3f2264ab9e39d36070d76fafd83a848b43c>`_
- Merge pull request #273 from fedora-infra/feature/fix-pagure-tests `e5096fd5f <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/e5096fd5f9668bfabc039520a13535bfd116f5f7>`_
- 0.5.7 `d2db17c2b <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/d2db17c2b117dc018dc8e5c4076dfa982690fe11>`_
- Try to avoid pagure exceptions for some unhandled message type. `6488cea86 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/6488cea8620c97a1e6b6a8abc4846bc9dec69ed9>`_
- Merge pull request #274 from fedora-infra/feature/dance-around-pagure `494ca8edd <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/494ca8edda22469554edae6e02e5474d752ea96f>`_
- 0.5.8 `a42949a58 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/a42949a58e0f9bbf637eab05d018e8cc4da6a96d>`_
- Add support for pagure's message about commits `180899ccc <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/180899cccd6950cd8930ac574fc8d13997639236>`_
- User email2fas to be a little more FAS' username friendly `2aac21a45 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/2aac21a45a69fe8f06804eb841472564957e80ad>`_
- Merge pull request #276 from fedora-infra/more_pagure `a7570d83a <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/a7570d83a193f7f7f42e6ff4fde2e342206337c8>`_
- 0.5.9 `fd241927e <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/fd241927ef852979c0ab227d7b508b247be69a7e>`_
- 0.5.9 `28d44e3d3 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/28d44e3d31dfec7a71785fb3049d55d833d0fb16>`_
- Use badge.award 'description' in long_form `dbb892eb6 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/dbb892eb635154ffcd6bb9427436120991c8d775>`_
- Merge pull request #280 from pranavk/develop `1b0cf481f <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/1b0cf481f5f4699bf3deacce07ec741f649a58d3>`_
- Attempt to add titles to github PR/issue openings `649637393 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/649637393f21049120ba80304e528591f9d7bebe>`_
- Fix some syntax errors. `8ac39b3af <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/8ac39b3af0294c53c197d94b214293bc48510ef9>`_
- make tests pass `b2214a082 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/b2214a0820c1c69bd3d0b30e42c409062957c927>`_
- Merge pull request #282 from fedora-infra/issue-open-titles `d438f45d6 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/d438f45d6c2735b787b4761a5c051df8874032bb>`_
- Faster, please. `28170f2d9 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/28170f2d91678a98ee585746ae51e83595a77b13>`_
- Link directly to pagure comments. `633a39bbf <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/633a39bbfe3373eabbd7fbd79494d2d0fbd4c3ce>`_
- Merge pull request #283 from fedora-infra/feature/pagure-links `9d1feda98 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/9d1feda98397ba0ec02b1472354e34e78cd87381>`_
- Update language for pagure messages. `bd3da61ef <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/bd3da61efd0bf6a53c5f0621da3620a935f34dc1>`_
- Merge pull request #284 from fedora-infra/feature/pagure-language-changes `837191f7d <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/837191f7da987ec46885c2affac1ed3f40b902da>`_
- We should return a link... for #link things in irc meetings. `2b0ad74ab <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/2b0ad74ab30231c49c2f282d8308f1c131dca7a6>`_
- Remove spurious print statement. `f1748ed76 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/f1748ed7682c4202bd43e9fcfdad879b23c72563>`_
- Merge pull request #285 from fedora-infra/feature/link-link `8e3e2128c <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/8e3e2128c32f2584b8e6af78787c97391adb9a86>`_
- Update Koschei URL `4e08316e3 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/4e08316e3a206680584bddc36b6f096a71635c9a>`_
- Merge pull request #287 from mizdebsk/koschei `634098d16 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/634098d167c8dc7216094bd2ea65a8d85c7d6ca6>`_
- Adjust the docstring to reflect the test `2aef1ebcd <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/2aef1ebcdba69559e898fcc9f075fb5050cba36f>`_
- Add logic to process messages sent by pkgdb when changing the koschei monitoring flag `554038f11 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/554038f1133f5fdc4937eea864773fc5ec441501>`_
- Add unit-tests for the message sent by pkgdb when updating the koschei monitoring flag `97351e2f7 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/97351e2f7c2b125f3964786201d2585d1e7d4503>`_
- Add missing space to make the link work properly `43664879c <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/43664879ce6af5daf2fc076cf488e281ac76fb70>`_
- Add test message of a failed scratch build with information about the target `ba65c7241 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/ba65c72414c4dacf3a7d330a58939f436c326fff>`_
- Specify the target of the build if we can extract it from the message `a60706c22 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/a60706c22cfa47e26aa4cc48d7b0e1e985af7984>`_
- Merge pull request #288 from fedora-infra/pkgdb_koschei `2a3066914 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/2a3066914f9a5f1fe21fd59ee15f959c876b80e9>`_
- Merge pull request #289 from fedora-infra/scratch_with_target `79294105f <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/79294105ffb9377af3692679c82369a4d091212c>`_
- Careful for x-archived-at being None. `92e77072a <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/92e77072a61a57385df5a40822dd8e32a0d90b84>`_
- Fix grammar for github.pull_request.synchronize `42df2c3d4 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/42df2c3d4b92e108c96c1e3f33d43ee21ca99504>`_
- Merge pull request #290 from fedora-infra/synchronize-past-tense `7a1c74a81 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/7a1c74a81ec1ec1d631e662dffa0a971171def01>`_
- Update pagure comment links. `b23e24247 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/b23e242473d749ed7c1256981d2cbce5dea04ab1>`_
- Merge pull request #292 from fedora-infra/feature/pagure-link `60b33fe40 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/60b33fe4029c5739b8fa6eaaf058c1841324a41c>`_
- Ansible conglomerator (for fedora-hubs) `6a1d55773 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/6a1d55773ea33902cbebd94d3ef8fc5423e7ce01>`_
- Handle case where constituents have been pre-filtered. `e8e760e0e <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/e8e760e0e0361cbf6cffad5133f0db6c57b13b84>`_
- Tagger conglomerator (for fedora-hubs) `6e6202e39 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/6e6202e39804be3ac64db2e8badec5aecb4390ad>`_
- Consistency. `ec985c8d0 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/ec985c8d0f9910f533b0c3f303deaee5cb4673d9>`_
- Remove duplicate declaration. `ef62ab93e <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/ef62ab93e6002fa2f7e35fa495eec2b217ef8ea8>`_
- Merge pull request #294 from fedora-infra/feature/tagger-conglomerator `8a70eb667 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/8a70eb6671567fb37864ef641822310d42f3b97a>`_
- Drop hardcoding of humanized time in the test. `4eb882116 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/4eb882116db88926d8862d2d7702d26227b99d03>`_
- Try to handle all these plural cases. `c55e09523 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/c55e09523adc135b7c79b9e6eecb1374c1775267>`_
- Merge pull request #293 from fedora-infra/feature/ansible-conglomerator `9cf772c48 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/9cf772c48bb68ad4cbf95b77b554f54ec70c69d8>`_

0.5.1
-----

- Test against multiple version of six.  We have an old version on epel7. `3f47d4d88 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/3f47d4d880fc0f20adc4497dc59bf57a93c52d1d>`_
- Be careful with old python-six. `80aa83234 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/80aa8323438fd5da8875c63ee22ca4e27355201a>`_
- Adjust tox to test old python-six. `c637f3b94 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/c637f3b94d2a114a0892a821b737789d954bebbd>`_
- Merge pull request #258 from fedora-infra/feature/six-careful `db1435539 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/db1435539315b020e14710d247333dbef917a6ab>`_

0.5.0
-----

- Be careful with a null host from koji. `8c28d021d <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/8c28d021dddbe8804584414735036251a15772c6>`_
- Merge pull request #244 from fedora-infra/feature/careful-with-null-host `09e2a442a <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/09e2a442a690935aaf14010d92dbb0e14913c96b>`_
- 0.4.10 `80908230f <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/80908230f39b7cb65bf2c065b2a4a31d964e6545>`_
- Use nice package icons where we can. `d4cf3aba7 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/d4cf3aba7774fe7ac5ea2c820fa83f9607e79c8d>`_
- Remove redundant line. `eb9bdd171 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/eb9bdd1712a757d705badca54d6d8904b07b060a>`_
- Merge pull request #245 from fedora-infra/feature/package-icons `2ea3f0892 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/2ea3f0892ceaf573c4703b15eb3a7cf752eb03f1>`_
- Add unit-tests for pkgdb messages sent when someone asks for a package to be unretired `923b3e918 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/923b3e9186bc0d83c26a21f4417e02ce33d13982>`_
- Adjust the pkgdb processor for messages asking for unretirement `e75627f85 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/e75627f8567b4f3fa96370a078127427fd00d9b3>`_
- Merge pull request #246 from fedora-infra/missing_pkgdb `3aa1190e3 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/3aa1190e3b0046a2d319a8df5ae41615511eea5f>`_
- 0.4.11 `b6b3f80f5 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/b6b3f80f5c59bc0ead82cc3428c779f5d8f87bf1>`_
- Try to workaround an odd variation in message structure. `c7f8dfae3 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/c7f8dfae32c491d8d06077d7e3cafc96454f9e96>`_
- Merge pull request #248 from fedora-infra/feature/anitya-workaround `e89c8f171 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/e89c8f171118b54f4ac94de680a0cdf99c7af359>`_
- Port to Python 3: `e659faa93 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/e659faa93072e4c366f4b5670a247cc9ba59710c>`_
- Merge pull request #249 from bkabrda/develop `0fcd3f770 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/0fcd3f77066ae7df7d168e0d476404f55c74de83>`_
- Add tox config for fun and profit. `3846162f3 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/3846162f3e6da44fc7eae7cb4aefc69aca06dab9>`_
- Add .tox to gitignore. `247d26166 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/247d261666514d6b426b761bdd0e96e9d1c330e3>`_
- Handle bodhi errata messages for #96. `4266f9c82 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/4266f9c82a589fac2c4e6b3a382d4c4a6451ec9e>`_
- Use the errata email for the long_form repr.  Fixes #96. `2b73918a8 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/2b73918a8951815c4f647f0d3da0ba885958c9a6>`_
- Handle new update karma threshold messages. `f7895a2c6 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/f7895a2c6928daff60760533205c9b638231af31>`_
- Merge pull request #251 from fedora-infra/feature/new-bodhi-messages `411bddc17 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/411bddc17f9ed6ca5c8324bce4961cdd889fc1f6>`_
- Merge pull request #250 from fedora-infra/feature/tox `36d9f5652 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/36d9f56524cb11cb0ac90c81047a45d9837a8baf>`_
- Use the bodhi "alias" instead of "title" if available. `917471103 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/917471103052886c971cd54f82818c964f78c006>`_
- Merge pull request #253 from fedora-infra/feature/use-bodhi-alias `c468b2a4e <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/c468b2a4e2329a1e375b7e0ea500f9048bbde237>`_
- Rename all occurences of "gravatar" to "avatar". `3da40c955 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/3da40c95593a4dff41a696732e209148e89ecf4a>`_
- Comment out a perennially-failing, network-dependent test case. `6560390b6 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/6560390b6cc11ab6f6d4ba5b1cd0f597970381f7>`_
- Remove unnecessary lines. `6e6b3f041 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/6e6b3f0416ef1be81fc35e9b107f15634f585935>`_
- Fix typo'd return value. `4df5e94a5 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/4df5e94a5d15971fcc4baca7078d7b4f006c961d>`_
- Merge pull request #254 from fedora-infra/feature/remove-gravatar `a5f06793c <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/a5f06793c4296c6ee9dadaae8053186fc9e91403>`_
- Add zanata processor and tests. `d4c0deed2 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/d4c0deed25fdb724d29d45c0f2690aadf42c95cf>`_
- Merge pull request #255 from fedora-infra/feature/zanata `b6599b694 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/b6599b69401acc2a7d3c52d42d621181f739211d>`_

0.4.9
-----

- Be more careful with null task_ids. `1b0a00659 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/1b0a0065924fcfbfd71ef2c1e8dfa17269cd44bb>`_
- PEP8. `fe593bca9 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/fe593bca98a6e7f04aabea1d57f22dc6e6dcf10d>`_

0.4.8
-----

- Add the Pagure processor for pagure's fedmsg messages `f1ce03a90 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/f1ce03a9019cce32cf3a42a03f89a8fdb5ba7ca9>`_
- Add unit-tests for pagure's fedmsg messages `85173cd70 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/85173cd704c795bbdb67f16e2e2d123d10c7bb00>`_
- Declare the pagure processor in the setup.py script `8d6450c9f <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/8d6450c9f4b5762e7c0cd644c063ca8c384bfc3f>`_
- Merge pull request #238 from fedora-infra/pagure `599ac8072 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/599ac8072418912b3fe12bb84bfb7e64032c6249>`_
- Include the comment text in emails about bodhi comments. `576fe8ce5 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/576fe8ce527a317d3f3c4a7baed32355e2afdc05>`_
- Trim end of line spaces `f55d11e62 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/f55d11e626b2a63d3f539f73561366af55d1d675>`_
- Add support to anitya for odd changes `380d8c454 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/380d8c454dd519b4d569aae5ac90a61e83977502>`_
- Add unit-tests for odd new upstream version `6e6d6f37a <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/6e6d6f37a74dc641bd2111018e77f3ff24711e2d>`_
- Adjust docstring to represent the action `e495b3ac3 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/e495b3ac3fa4d7390c869e8756fdbf21d1820180>`_
- Merge pull request #239 from fedora-infra/feature/fix-some-bodhi-things `96f883a24 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/96f883a24b4e53bad1345e415b98e5cdc98bfa05>`_
- Merge pull request #240 from fedora-infra/fix_docstring `945b74ba7 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/945b74ba721b881a91f3bcfc83ddfd441807151f>`_
- Handle new hotness message type. `1ba0b6909 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/1ba0b69090812bd2974a2106b6985ed6c404416b>`_
- These koji tests results are always changing.  We'll need to mock this long-term. `575fdc1e3 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/575fdc1e32088a6008a84a41b83757114d6798da>`_
- Merge pull request #242 from fedora-infra/feature/new-hotness-messages `cdaf5cf73 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/cdaf5cf7399452ebba055d69a218120f55517edb>`_

0.4.7
-----

- Be careful with the trac ticket summary. `6b2373fe7 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/6b2373fe70ed500f557b99e35c50038de2876c66>`_
- Strip out None values from the bodhi usernames list. `bb52a3440 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/bb52a3440c0797bee280c817c85d764552e6c241>`_
- Merge pull request #235 from fedora-infra/feature/bodhi-anon `c9733443b <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/c9733443bd148a64958e900d93917a0bd28251d9>`_
- Merge pull request #234 from fedora-infra/feature/fix-trac-summary `74305eafa <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/74305eafa82ce48ecc1d3af41f7b0b554fb52c3f>`_
- (unrelated) these failure tests are unsustainable.  they change underneath all the time... `9ec4ec087 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/9ec4ec0871b20a090378214ed1209e1fca03664c>`_
- Add long_form for koji scratch builds. `12044f462 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/12044f462eeb28a5b5c8c1ceaaacdd978e33866c>`_
- Merge pull request #236 from fedora-infra/feature/longform-for-scratch `b387c333e <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/b387c333e6077cfb928447886a0d49685fba046e>`_
- De-duplicate subtitles from long_form representations. `312bb250e <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/312bb250e649c45fb6f0be20cbdc4e13cb7d341e>`_
- Merge pull request #237 from fedora-infra/feature/de-duplicate-subtitle `e7bf1014d <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/e7bf1014d3d87a5eee038a783126db2cf104f84b>`_

0.4.6
-----

- (meetbot) use the agent's name where available. `22b9d8280 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/22b9d82800db58ba860afad308b7ae780fea96d3>`_
- Merge pull request #231 from fedora-infra/feature/meetbot-tweaks `ad46e8983 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/ad46e8983eb5844522b25513bdda9053d317c817>`_
- Add more info about why karma was given `cdeaf8070 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/cdeaf8070bb58809f725ad9bf6d367724339185a>`_
- Merge pull request #232 from fedora-infra/feature/karma-tweaks `c8ca14c43 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/c8ca14c4304c2d3765af3d10c5b9b363579cb6d2>`_
- Shorten git commit emails if they have already been seen. `452eb15ec <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/452eb15ec42e093cb4ecf9cbe477885d23c6cfb4>`_
- Merge pull request #233 from fedora-infra/feature/seen-commits `514d67a0d <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/514d67a0dc128afa9b8b433476bb3f46ccd557b1>`_

0.4.5
-----

- Add processor for new karma messages. `c018104f9 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/c018104f9a13cd052b7875c535935ed9ec5e6e4f>`_
- Adding Anitya tests for new version of packages detected mapped to multiple packages `0f1ae6b0d <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/0f1ae6b0ddd5415a9bac8b8e7d44bfde7b4539f9>`_
- Removing N from the list of values passed to list_to_series() function `6684e7e60 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/6684e7e6021487db3ddf1856f21dcdfa74f159ad>`_
- Merge pull request #228 from Ghost-script/anitya `775595942 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/77559594284e461ad058bbe3d77010aa82045020>`_
- Merge pull request #222 from fedora-infra/feature/karma `44e5bf4ee <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/44e5bf4ee80439f553f3fa4bf2b33e439fcb657d>`_
- Add tests and implementation for new meetbot line items. `6a96132c4 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/6a96132c4358d89947bc050ddfac3c625da293ad>`_
- Ignore koji longform tests if koji is not installed. `e2b53ef44 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/e2b53ef44b7d04d45acfbecdb3098d2360d255b1>`_
- Merge pull request #229 from fedora-infra/feature/halp-items `02bd9406b <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/02bd9406b73b686643b899785182ed6b150b1604>`_
- Merge pull request #230 from fedora-infra/feature/ignore-koji-longform-if-no-koji `83aad3c45 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/83aad3c45b25c67c7804c81a92874955dcaaa591>`_

0.4.4
-----

- Make github longform tests conditional. `4f46090dd <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/4f46090ddb15c676b51b5b8537220612349b6a68>`_
- Move zodbot tests to their own file, and make the long_form part conditional like the others. `0a99a6226 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/0a99a6226856c77ec35eb18a9e12eda7fa0d69b0>`_
- Merge pull request #213 from fedora-infra/feature/more-longform-conditionals `b030cf966 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/b030cf96603fd6117874814c2f04dab31dcb0b6f>`_
- Don't return prematurely if parent task is still open. `1f80bf7c2 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/1f80bf7c2e666378f23ebe5c83d5e1222142c3c7>`_
- Merge pull request #214 from fedora-infra/feature/koji-longform-fix `fd9cea78a <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/fd9cea78a2eeb68ffc91791ef224d254fa414e1e>`_
- Handle case where result never gets defined. `727bbe1c7 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/727bbe1c7085bd0a7e32ae2afdb75461328307e9>`_
- Add new copr fields to the docs. `d7cb97119 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/d7cb97119ec87d6e2576779f0ad9cd8f17b63fb0>`_
- Adjust copr.end subtitle to indicate the version of the build. `186811dac <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/186811dacbf3b268240b31d927236d58716df024>`_
- Add a long_form representation for copr build completions. `7488a49e9 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/7488a49e9d1df4c5f5c73a53bd6daa77228ab16a>`_
- Add a build failure test just to make sure we have all the bases covered. `b4eb0807f <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/b4eb0807f6855a14028606669c344ff890f4bce3>`_
- There is more info here now... `d8f8e3713 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/d8f8e3713a7ba091d2e2374d39d17732cb0839f8>`_
- Add a link to more useful logs at @danvratil's suggestion. `0a46fdd69 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/0a46fdd69e86884aa4ac00de06eae58adf54151d>`_
- Also link to root.log. `dd1c085a8 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/dd1c085a8698e19b9ff5da3b43f6c8ea5e234a49>`_
- Oh, and of course, https please. `4a15d69c5 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/4a15d69c51a808fb4ad9973bf9e7c5b600731961>`_
- Merge pull request #215 from fedora-infra/feature/fancy-copr-messages `7367a5f53 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/7367a5f536ee8c1b569b15ace59115684948b3f8>`_
- Merge pull request #216 from fedora-infra/feature/koji-longform-testfix `a223aa0e2 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/a223aa0e23337fb96d05577af566f5d5dd7e504c>`_
- Added Github Page_Build Message Handler `587bd3275 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/587bd327563465d71fe74575a663c2b207cdf448>`_
- Merge pull request #217 from Ghost-script/page_build `b88644e06 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/b88644e0614188ccce6edc4d2db428caba805d0d>`_
- Added Github Tead_Add message handler `1fb35abab <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/1fb35abab91ac60d09a87533a65de714d474eec1>`_
- Merge pull request #219 from Ghost-script/team_add `f6f593bd7 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/f6f593bd7fb4d483f4c297cb1f19ae6acdf5606c>`_
- Use FAS openid libravatar first for git.receive messages And porting scm tests from __init__.py to scm.py `45c2f47d1 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/45c2f47d14a610b4e736eadb8fedac91e7ed148a>`_
- These should be here. `94ece2b33 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/94ece2b3381b23846870484f57e2d06cb2a1908d>`_
- Merge pull request #221 from Ghost-script/openid_libravatar `49e3df842 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/49e3df8421549b59d2f843123427cd0540c82fd2>`_
- Add icon url for fedimg logo. `77f83a329 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/77f83a32964258644930e9a8734cab9299debbb2>`_
- Added message handler and tests for Github member (added to)/(removed from) messages `4f747e0f3 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/4f747e0f39b26529670d642d03496e05b1d5e814>`_
- Merge pull request #227 from Ghost-script/github_member `f50e03724 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/f50e03724e1f8ccdb1e16f0a3dcdfd13d24e5377>`_
- Merge pull request #223 from fedora-infra/feature/fix-conglomerate `738d431ea <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/738d431ea1c2faec67f2837bee54853926fbfe35>`_
- Merge pull request #224 from fedora-infra/feature/fedimg-icon `ef48b3a85 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/ef48b3a85873fa297f447cb34411e9c3f17c7c83>`_

0.4.3
-----

- Comment out the buildsys cancel long form test. `f50eda651 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/f50eda6519a76f8eacf8e681e2b41e831c7ff7b6>`_
- Be more careful with these timestamps. `64f6116cf <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/64f6116cf59a0eda0fab1ff1a709ae8fe804cb7a>`_

0.4.2
-----

- Comment out the buildsys cancel long form test. `f50eda651 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/f50eda6519a76f8eacf8e681e2b41e831c7ff7b6>`_
- Be more careful with these timestamps. `64f6116cf <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/64f6116cf59a0eda0fab1ff1a709ae8fe804cb7a>`_
- 0.4.3 `4bbd5b245 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/4bbd5b245314d6705cab494d68598eaf152db2d9>`_
- Make github longform tests conditional. `4f46090dd <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/4f46090ddb15c676b51b5b8537220612349b6a68>`_
- Move zodbot tests to their own file, and make the long_form part conditional like the others. `0a99a6226 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/0a99a6226856c77ec35eb18a9e12eda7fa0d69b0>`_
- Merge pull request #213 from fedora-infra/feature/more-longform-conditionals `b030cf966 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/b030cf96603fd6117874814c2f04dab31dcb0b6f>`_
- Don't return prematurely if parent task is still open. `1f80bf7c2 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/1f80bf7c2e666378f23ebe5c83d5e1222142c3c7>`_
- Merge pull request #214 from fedora-infra/feature/koji-longform-fix `fd9cea78a <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/fd9cea78a2eeb68ffc91791ef224d254fa414e1e>`_
- Handle case where result never gets defined. `727bbe1c7 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/727bbe1c7085bd0a7e32ae2afdb75461328307e9>`_
- Add new copr fields to the docs. `d7cb97119 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/d7cb97119ec87d6e2576779f0ad9cd8f17b63fb0>`_
- Adjust copr.end subtitle to indicate the version of the build. `186811dac <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/186811dacbf3b268240b31d927236d58716df024>`_
- Add a long_form representation for copr build completions. `7488a49e9 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/7488a49e9d1df4c5f5c73a53bd6daa77228ab16a>`_
- Add a build failure test just to make sure we have all the bases covered. `b4eb0807f <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/b4eb0807f6855a14028606669c344ff890f4bce3>`_
- There is more info here now... `d8f8e3713 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/d8f8e3713a7ba091d2e2374d39d17732cb0839f8>`_
- Add a link to more useful logs at @danvratil's suggestion. `0a46fdd69 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/0a46fdd69e86884aa4ac00de06eae58adf54151d>`_
- Also link to root.log. `dd1c085a8 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/dd1c085a8698e19b9ff5da3b43f6c8ea5e234a49>`_
- Oh, and of course, https please. `4a15d69c5 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/4a15d69c51a808fb4ad9973bf9e7c5b600731961>`_
- Merge pull request #215 from fedora-infra/feature/fancy-copr-messages `7367a5f53 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/7367a5f536ee8c1b569b15ace59115684948b3f8>`_
- Merge pull request #216 from fedora-infra/feature/koji-longform-testfix `a223aa0e2 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/a223aa0e23337fb96d05577af566f5d5dd7e504c>`_
- Added Github Page_Build Message Handler `587bd3275 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/587bd327563465d71fe74575a663c2b207cdf448>`_
- Merge pull request #217 from Ghost-script/page_build `b88644e06 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/b88644e0614188ccce6edc4d2db428caba805d0d>`_
- Added Github Tead_Add message handler `1fb35abab <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/1fb35abab91ac60d09a87533a65de714d474eec1>`_
- Merge pull request #219 from Ghost-script/team_add `f6f593bd7 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/f6f593bd7fb4d483f4c297cb1f19ae6acdf5606c>`_
- Add processor for new karma messages. `c018104f9 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/c018104f9a13cd052b7875c535935ed9ec5e6e4f>`_
- Use FAS openid libravatar first for git.receive messages And porting scm tests from __init__.py to scm.py `45c2f47d1 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/45c2f47d14a610b4e736eadb8fedac91e7ed148a>`_
- These should be here. `94ece2b33 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/94ece2b3381b23846870484f57e2d06cb2a1908d>`_
- Merge pull request #221 from Ghost-script/openid_libravatar `49e3df842 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/49e3df8421549b59d2f843123427cd0540c82fd2>`_
- Add icon url for fedimg logo. `77f83a329 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/77f83a32964258644930e9a8734cab9299debbb2>`_
- Added message handler and tests for Github member (added to)/(removed from) messages `4f747e0f3 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/4f747e0f39b26529670d642d03496e05b1d5e814>`_
- Merge pull request #227 from Ghost-script/github_member `f50e03724 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/f50e03724e1f8ccdb1e16f0a3dcdfd13d24e5377>`_
- Merge pull request #223 from fedora-infra/feature/fix-conglomerate `738d431ea <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/738d431ea1c2faec67f2837bee54853926fbfe35>`_
- Merge pull request #224 from fedora-infra/feature/fedimg-icon `ef48b3a85 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/ef48b3a85873fa297f447cb34411e9c3f17c7c83>`_
- 0.4.4 `eb6b92dfd <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/eb6b92dfde4de6aea8f7046ae501d53bb3c41028>`_
- Adding Anitya tests for new version of packages detected mapped to multiple packages `0f1ae6b0d <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/0f1ae6b0ddd5415a9bac8b8e7d44bfde7b4539f9>`_
- Removing N from the list of values passed to list_to_series() function `6684e7e60 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/6684e7e6021487db3ddf1856f21dcdfa74f159ad>`_
- Merge pull request #228 from Ghost-script/anitya `775595942 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/77559594284e461ad058bbe3d77010aa82045020>`_
- Merge pull request #222 from fedora-infra/feature/karma `44e5bf4ee <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/44e5bf4ee80439f553f3fa4bf2b33e439fcb657d>`_
- Add tests and implementation for new meetbot line items. `6a96132c4 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/6a96132c4358d89947bc050ddfac3c625da293ad>`_
- Ignore koji longform tests if koji is not installed. `e2b53ef44 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/e2b53ef44b7d04d45acfbecdb3098d2360d255b1>`_
- Merge pull request #229 from fedora-infra/feature/halp-items `02bd9406b <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/02bd9406b73b686643b899785182ed6b150b1604>`_
- Merge pull request #230 from fedora-infra/feature/ignore-koji-longform-if-no-koji `83aad3c45 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/83aad3c45b25c67c7804c81a92874955dcaaa591>`_
- 0.4.5 `23dece4ef <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/23dece4ef26b2e5d4e8d75429512ba7ffee6139a>`_
- (meetbot) use the agent's name where available. `22b9d8280 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/22b9d82800db58ba860afad308b7ae780fea96d3>`_
- Merge pull request #231 from fedora-infra/feature/meetbot-tweaks `ad46e8983 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/ad46e8983eb5844522b25513bdda9053d317c817>`_
- Add more info about why karma was given `cdeaf8070 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/cdeaf8070bb58809f725ad9bf6d367724339185a>`_
- Merge pull request #232 from fedora-infra/feature/karma-tweaks `c8ca14c43 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/c8ca14c4304c2d3765af3d10c5b9b363579cb6d2>`_
- Shorten git commit emails if they have already been seen. `452eb15ec <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/452eb15ec42e093cb4ecf9cbe477885d23c6cfb4>`_
- Merge pull request #233 from fedora-infra/feature/seen-commits `514d67a0d <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/514d67a0dc128afa9b8b433476bb3f46ccd557b1>`_
- 0.4.6 `379251578 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/37925157809c583753982158edc34f4ef021eac4>`_
- Be careful with the trac ticket summary. `6b2373fe7 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/6b2373fe70ed500f557b99e35c50038de2876c66>`_
- Strip out None values from the bodhi usernames list. `bb52a3440 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/bb52a3440c0797bee280c817c85d764552e6c241>`_
- Merge pull request #235 from fedora-infra/feature/bodhi-anon `c9733443b <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/c9733443bd148a64958e900d93917a0bd28251d9>`_
- Merge pull request #234 from fedora-infra/feature/fix-trac-summary `74305eafa <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/74305eafa82ce48ecc1d3af41f7b0b554fb52c3f>`_
- (unrelated) these failure tests are unsustainable.  they change underneath all the time... `9ec4ec087 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/9ec4ec0871b20a090378214ed1209e1fca03664c>`_
- Add long_form for koji scratch builds. `12044f462 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/12044f462eeb28a5b5c8c1ceaaacdd978e33866c>`_
- Merge pull request #236 from fedora-infra/feature/longform-for-scratch `b387c333e <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/b387c333e6077cfb928447886a0d49685fba046e>`_
- De-duplicate subtitles from long_form representations. `312bb250e <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/312bb250e649c45fb6f0be20cbdc4e13cb7d341e>`_
- Merge pull request #237 from fedora-infra/feature/de-duplicate-subtitle `e7bf1014d <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/e7bf1014d3d87a5eee038a783126db2cf104f84b>`_
- 0.4.7 `5e5ef52d8 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/5e5ef52d8cd326eaf28051e73e692f6ce0c503eb>`_
- Add the Pagure processor for pagure's fedmsg messages `f1ce03a90 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/f1ce03a9019cce32cf3a42a03f89a8fdb5ba7ca9>`_
- Add unit-tests for pagure's fedmsg messages `85173cd70 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/85173cd704c795bbdb67f16e2e2d123d10c7bb00>`_
- Declare the pagure processor in the setup.py script `8d6450c9f <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/8d6450c9f4b5762e7c0cd644c063ca8c384bfc3f>`_
- Merge pull request #238 from fedora-infra/pagure `599ac8072 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/599ac8072418912b3fe12bb84bfb7e64032c6249>`_
- Include the comment text in emails about bodhi comments. `576fe8ce5 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/576fe8ce527a317d3f3c4a7baed32355e2afdc05>`_
- Trim end of line spaces `f55d11e62 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/f55d11e626b2a63d3f539f73561366af55d1d675>`_
- Add support to anitya for odd changes `380d8c454 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/380d8c454dd519b4d569aae5ac90a61e83977502>`_
- Add unit-tests for odd new upstream version `6e6d6f37a <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/6e6d6f37a74dc641bd2111018e77f3ff24711e2d>`_
- Adjust docstring to represent the action `e495b3ac3 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/e495b3ac3fa4d7390c869e8756fdbf21d1820180>`_
- Merge pull request #239 from fedora-infra/feature/fix-some-bodhi-things `96f883a24 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/96f883a24b4e53bad1345e415b98e5cdc98bfa05>`_
- Merge pull request #240 from fedora-infra/fix_docstring `945b74ba7 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/945b74ba721b881a91f3bcfc83ddfd441807151f>`_
- Handle new hotness message type. `1ba0b6909 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/1ba0b69090812bd2974a2106b6985ed6c404416b>`_
- These koji tests results are always changing.  We'll need to mock this long-term. `575fdc1e3 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/575fdc1e32088a6008a84a41b83757114d6798da>`_
- Merge pull request #242 from fedora-infra/feature/new-hotness-messages `cdaf5cf73 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/cdaf5cf7399452ebba055d69a218120f55517edb>`_
- 0.4.8 `3b88e2a5b <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/3b88e2a5b9506061faf8d345dab186f13c41bb95>`_
- Be more careful with null task_ids. `1b0a00659 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/1b0a0065924fcfbfd71ef2c1e8dfa17269cd44bb>`_
- PEP8. `fe593bca9 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/fe593bca98a6e7f04aabea1d57f22dc6e6dcf10d>`_
- 0.4.9 `2d7f90f9a <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/2d7f90f9ae53a2f449b6ad785d726ef4fb1b7a62>`_
- Be careful with a null host from koji. `8c28d021d <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/8c28d021dddbe8804584414735036251a15772c6>`_
- Merge pull request #244 from fedora-infra/feature/careful-with-null-host `09e2a442a <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/09e2a442a690935aaf14010d92dbb0e14913c96b>`_
- 0.4.10 `80908230f <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/80908230f39b7cb65bf2c065b2a4a31d964e6545>`_
- Use nice package icons where we can. `d4cf3aba7 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/d4cf3aba7774fe7ac5ea2c820fa83f9607e79c8d>`_
- Remove redundant line. `eb9bdd171 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/eb9bdd1712a757d705badca54d6d8904b07b060a>`_
- Merge pull request #245 from fedora-infra/feature/package-icons `2ea3f0892 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/2ea3f0892ceaf573c4703b15eb3a7cf752eb03f1>`_
- Add unit-tests for pkgdb messages sent when someone asks for a package to be unretired `923b3e918 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/923b3e9186bc0d83c26a21f4417e02ce33d13982>`_
- Adjust the pkgdb processor for messages asking for unretirement `e75627f85 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/e75627f8567b4f3fa96370a078127427fd00d9b3>`_
- Merge pull request #246 from fedora-infra/missing_pkgdb `3aa1190e3 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/3aa1190e3b0046a2d319a8df5ae41615511eea5f>`_

0.4.11
------

- Use nice package icons where we can. `d4cf3aba7 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/d4cf3aba7774fe7ac5ea2c820fa83f9607e79c8d>`_
- Remove redundant line. `eb9bdd171 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/eb9bdd1712a757d705badca54d6d8904b07b060a>`_
- Merge pull request #245 from fedora-infra/feature/package-icons `2ea3f0892 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/2ea3f0892ceaf573c4703b15eb3a7cf752eb03f1>`_
- Add unit-tests for pkgdb messages sent when someone asks for a package to be unretired `923b3e918 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/923b3e9186bc0d83c26a21f4417e02ce33d13982>`_
- Adjust the pkgdb processor for messages asking for unretirement `e75627f85 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/e75627f8567b4f3fa96370a078127427fd00d9b3>`_
- Merge pull request #246 from fedora-infra/missing_pkgdb `3aa1190e3 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/3aa1190e3b0046a2d319a8df5ae41615511eea5f>`_

0.4.10
------

- Add a long_form field for message about uploading files to the lookaside cache `86432850d <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/86432850d2a6f631817672a9ac10e7c5526d9eb5>`_
- Fix getting the current folder so that we can call that file directly `e73fe2b97 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/e73fe2b971e543a85b6487b457228f86d10c435d>`_
- Adjust the example patch for the change in cgit version `05e6f1f46 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/05e6f1f468ed481bbf49e06628fa6b445012a704>`_
- Add unit-tests for the long_form format of uploading to the lookaside cache `f980ec535 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/f980ec535d8e8eb348e296b4d87ec4dae14b193b>`_
- Merge pull request #209 from fedora-infra/long_form_lookaside `a37198d07 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/a37198d07a701cab168238ee0f8e9158f4984e16>`_
- Update this test to use a real build from somewhere. `0199f78c1 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/0199f78c1c1c13fa6ea1adea8cf74e0d57e000e2>`_
- Implement a long-form value for koji builds. `3bc8b1cc4 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/3bc8b1cc406c03a53e15e68c231c04c78d72e0f1>`_
- Add a way to disable these ourselves in koji and travis-ci. `aa6808eea <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/aa6808eea64e5a80aedcdd81d2691bd7978fcfaf>`_
- Add long-form values for trac tickets. `e1ec60be1 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/e1ec60be1f562f9faf31f7224ac5ed369ce88559>`_
- (anitya) Substitute Fedora package name for project name if available. `c99580a13 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/c99580a13a8268853b51f73193effd40ee3de5bd>`_
- Be on the safe side. `e964f8a9c <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/e964f8a9cf884486e64786748ea527bdc032ebad>`_
- Merge pull request #212 from fedora-infra/feature/anitya-sub-in-package-name `97573944f <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/97573944f7e9e69fcefdebb243b18b6352ee3b65>`_
- Merge pull request #211 from fedora-infra/feature/trac-longform `94a38f832 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/94a38f83291f794b6c1fb8e3abd065829b9af6ff>`_
- Also test longform for failed builds. `67c5fbab0 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/67c5fbab0335e822b670e4b379f0a7a020977ed4>`_
- Also test longform for cancelled builds. `9bab7ad7f <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/9bab7ad7f25863d84d3c2b686e2a7e4f7b706b6f>`_
- Merge pull request #210 from fedora-infra/feature/koji-longform `c60343c09 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/c60343c091d221cfbdef64d3b47e793f53bd2fed>`_
- 0.4.2 `900b4a596 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/900b4a596867d7c09b6fecd85353b40d010290ed>`_
- Comment out the buildsys cancel long form test. `f50eda651 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/f50eda6519a76f8eacf8e681e2b41e831c7ff7b6>`_
- Be more careful with these timestamps. `64f6116cf <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/64f6116cf59a0eda0fab1ff1a709ae8fe804cb7a>`_
- 0.4.3 `4bbd5b245 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/4bbd5b245314d6705cab494d68598eaf152db2d9>`_
- Make github longform tests conditional. `4f46090dd <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/4f46090ddb15c676b51b5b8537220612349b6a68>`_
- Move zodbot tests to their own file, and make the long_form part conditional like the others. `0a99a6226 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/0a99a6226856c77ec35eb18a9e12eda7fa0d69b0>`_
- Merge pull request #213 from fedora-infra/feature/more-longform-conditionals `b030cf966 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/b030cf96603fd6117874814c2f04dab31dcb0b6f>`_
- Don't return prematurely if parent task is still open. `1f80bf7c2 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/1f80bf7c2e666378f23ebe5c83d5e1222142c3c7>`_
- Merge pull request #214 from fedora-infra/feature/koji-longform-fix `fd9cea78a <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/fd9cea78a2eeb68ffc91791ef224d254fa414e1e>`_
- Handle case where result never gets defined. `727bbe1c7 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/727bbe1c7085bd0a7e32ae2afdb75461328307e9>`_
- Add new copr fields to the docs. `d7cb97119 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/d7cb97119ec87d6e2576779f0ad9cd8f17b63fb0>`_
- Adjust copr.end subtitle to indicate the version of the build. `186811dac <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/186811dacbf3b268240b31d927236d58716df024>`_
- Add a long_form representation for copr build completions. `7488a49e9 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/7488a49e9d1df4c5f5c73a53bd6daa77228ab16a>`_
- Add a build failure test just to make sure we have all the bases covered. `b4eb0807f <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/b4eb0807f6855a14028606669c344ff890f4bce3>`_
- There is more info here now... `d8f8e3713 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/d8f8e3713a7ba091d2e2374d39d17732cb0839f8>`_
- Add a link to more useful logs at @danvratil's suggestion. `0a46fdd69 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/0a46fdd69e86884aa4ac00de06eae58adf54151d>`_
- Also link to root.log. `dd1c085a8 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/dd1c085a8698e19b9ff5da3b43f6c8ea5e234a49>`_
- Oh, and of course, https please. `4a15d69c5 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/4a15d69c51a808fb4ad9973bf9e7c5b600731961>`_
- Merge pull request #215 from fedora-infra/feature/fancy-copr-messages `7367a5f53 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/7367a5f536ee8c1b569b15ace59115684948b3f8>`_
- Merge pull request #216 from fedora-infra/feature/koji-longform-testfix `a223aa0e2 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/a223aa0e23337fb96d05577af566f5d5dd7e504c>`_
- Added Github Page_Build Message Handler `587bd3275 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/587bd327563465d71fe74575a663c2b207cdf448>`_
- Merge pull request #217 from Ghost-script/page_build `b88644e06 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/b88644e0614188ccce6edc4d2db428caba805d0d>`_
- Added Github Tead_Add message handler `1fb35abab <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/1fb35abab91ac60d09a87533a65de714d474eec1>`_
- Merge pull request #219 from Ghost-script/team_add `f6f593bd7 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/f6f593bd7fb4d483f4c297cb1f19ae6acdf5606c>`_
- Add processor for new karma messages. `c018104f9 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/c018104f9a13cd052b7875c535935ed9ec5e6e4f>`_
- Use FAS openid libravatar first for git.receive messages And porting scm tests from __init__.py to scm.py `45c2f47d1 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/45c2f47d14a610b4e736eadb8fedac91e7ed148a>`_
- These should be here. `94ece2b33 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/94ece2b3381b23846870484f57e2d06cb2a1908d>`_
- Merge pull request #221 from Ghost-script/openid_libravatar `49e3df842 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/49e3df8421549b59d2f843123427cd0540c82fd2>`_
- Add icon url for fedimg logo. `77f83a329 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/77f83a32964258644930e9a8734cab9299debbb2>`_
- Added message handler and tests for Github member (added to)/(removed from) messages `4f747e0f3 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/4f747e0f39b26529670d642d03496e05b1d5e814>`_
- Merge pull request #227 from Ghost-script/github_member `f50e03724 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/f50e03724e1f8ccdb1e16f0a3dcdfd13d24e5377>`_
- Merge pull request #223 from fedora-infra/feature/fix-conglomerate `738d431ea <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/738d431ea1c2faec67f2837bee54853926fbfe35>`_
- Merge pull request #224 from fedora-infra/feature/fedimg-icon `ef48b3a85 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/ef48b3a85873fa297f447cb34411e9c3f17c7c83>`_
- 0.4.4 `eb6b92dfd <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/eb6b92dfde4de6aea8f7046ae501d53bb3c41028>`_
- Adding Anitya tests for new version of packages detected mapped to multiple packages `0f1ae6b0d <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/0f1ae6b0ddd5415a9bac8b8e7d44bfde7b4539f9>`_
- Removing N from the list of values passed to list_to_series() function `6684e7e60 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/6684e7e6021487db3ddf1856f21dcdfa74f159ad>`_
- Merge pull request #228 from Ghost-script/anitya `775595942 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/77559594284e461ad058bbe3d77010aa82045020>`_
- Merge pull request #222 from fedora-infra/feature/karma `44e5bf4ee <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/44e5bf4ee80439f553f3fa4bf2b33e439fcb657d>`_
- Add tests and implementation for new meetbot line items. `6a96132c4 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/6a96132c4358d89947bc050ddfac3c625da293ad>`_
- Ignore koji longform tests if koji is not installed. `e2b53ef44 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/e2b53ef44b7d04d45acfbecdb3098d2360d255b1>`_
- Merge pull request #229 from fedora-infra/feature/halp-items `02bd9406b <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/02bd9406b73b686643b899785182ed6b150b1604>`_
- Merge pull request #230 from fedora-infra/feature/ignore-koji-longform-if-no-koji `83aad3c45 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/83aad3c45b25c67c7804c81a92874955dcaaa591>`_
- 0.4.5 `23dece4ef <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/23dece4ef26b2e5d4e8d75429512ba7ffee6139a>`_
- (meetbot) use the agent's name where available. `22b9d8280 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/22b9d82800db58ba860afad308b7ae780fea96d3>`_
- Merge pull request #231 from fedora-infra/feature/meetbot-tweaks `ad46e8983 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/ad46e8983eb5844522b25513bdda9053d317c817>`_
- Add more info about why karma was given `cdeaf8070 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/cdeaf8070bb58809f725ad9bf6d367724339185a>`_
- Merge pull request #232 from fedora-infra/feature/karma-tweaks `c8ca14c43 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/c8ca14c4304c2d3765af3d10c5b9b363579cb6d2>`_
- Shorten git commit emails if they have already been seen. `452eb15ec <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/452eb15ec42e093cb4ecf9cbe477885d23c6cfb4>`_
- Merge pull request #233 from fedora-infra/feature/seen-commits `514d67a0d <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/514d67a0dc128afa9b8b433476bb3f46ccd557b1>`_
- 0.4.6 `379251578 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/37925157809c583753982158edc34f4ef021eac4>`_
- Be careful with the trac ticket summary. `6b2373fe7 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/6b2373fe70ed500f557b99e35c50038de2876c66>`_
- Strip out None values from the bodhi usernames list. `bb52a3440 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/bb52a3440c0797bee280c817c85d764552e6c241>`_
- Merge pull request #235 from fedora-infra/feature/bodhi-anon `c9733443b <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/c9733443bd148a64958e900d93917a0bd28251d9>`_
- Merge pull request #234 from fedora-infra/feature/fix-trac-summary `74305eafa <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/74305eafa82ce48ecc1d3af41f7b0b554fb52c3f>`_
- (unrelated) these failure tests are unsustainable.  they change underneath all the time... `9ec4ec087 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/9ec4ec0871b20a090378214ed1209e1fca03664c>`_
- Add long_form for koji scratch builds. `12044f462 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/12044f462eeb28a5b5c8c1ceaaacdd978e33866c>`_
- Merge pull request #236 from fedora-infra/feature/longform-for-scratch `b387c333e <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/b387c333e6077cfb928447886a0d49685fba046e>`_
- De-duplicate subtitles from long_form representations. `312bb250e <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/312bb250e649c45fb6f0be20cbdc4e13cb7d341e>`_
- Merge pull request #237 from fedora-infra/feature/de-duplicate-subtitle `e7bf1014d <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/e7bf1014d3d87a5eee038a783126db2cf104f84b>`_
- 0.4.7 `5e5ef52d8 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/5e5ef52d8cd326eaf28051e73e692f6ce0c503eb>`_
- Add the Pagure processor for pagure's fedmsg messages `f1ce03a90 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/f1ce03a9019cce32cf3a42a03f89a8fdb5ba7ca9>`_
- Add unit-tests for pagure's fedmsg messages `85173cd70 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/85173cd704c795bbdb67f16e2e2d123d10c7bb00>`_
- Declare the pagure processor in the setup.py script `8d6450c9f <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/8d6450c9f4b5762e7c0cd644c063ca8c384bfc3f>`_
- Merge pull request #238 from fedora-infra/pagure `599ac8072 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/599ac8072418912b3fe12bb84bfb7e64032c6249>`_
- Include the comment text in emails about bodhi comments. `576fe8ce5 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/576fe8ce527a317d3f3c4a7baed32355e2afdc05>`_
- Trim end of line spaces `f55d11e62 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/f55d11e626b2a63d3f539f73561366af55d1d675>`_
- Add support to anitya for odd changes `380d8c454 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/380d8c454dd519b4d569aae5ac90a61e83977502>`_
- Add unit-tests for odd new upstream version `6e6d6f37a <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/6e6d6f37a74dc641bd2111018e77f3ff24711e2d>`_
- Adjust docstring to represent the action `e495b3ac3 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/e495b3ac3fa4d7390c869e8756fdbf21d1820180>`_
- Merge pull request #239 from fedora-infra/feature/fix-some-bodhi-things `96f883a24 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/96f883a24b4e53bad1345e415b98e5cdc98bfa05>`_
- Merge pull request #240 from fedora-infra/fix_docstring `945b74ba7 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/945b74ba721b881a91f3bcfc83ddfd441807151f>`_
- Handle new hotness message type. `1ba0b6909 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/1ba0b69090812bd2974a2106b6985ed6c404416b>`_
- These koji tests results are always changing.  We'll need to mock this long-term. `575fdc1e3 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/575fdc1e32088a6008a84a41b83757114d6798da>`_
- Merge pull request #242 from fedora-infra/feature/new-hotness-messages `cdaf5cf73 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/cdaf5cf7399452ebba055d69a218120f55517edb>`_
- 0.4.8 `3b88e2a5b <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/3b88e2a5b9506061faf8d345dab186f13c41bb95>`_
- Be more careful with null task_ids. `1b0a00659 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/1b0a0065924fcfbfd71ef2c1e8dfa17269cd44bb>`_
- PEP8. `fe593bca9 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/fe593bca98a6e7f04aabea1d57f22dc6e6dcf10d>`_
- 0.4.9 `2d7f90f9a <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/2d7f90f9ae53a2f449b6ad785d726ef4fb1b7a62>`_
- Be careful with a null host from koji. `8c28d021d <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/8c28d021dddbe8804584414735036251a15772c6>`_
- Merge pull request #244 from fedora-infra/feature/careful-with-null-host `09e2a442a <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/09e2a442a690935aaf14010d92dbb0e14913c96b>`_

0.4.1
-----

- Handle None at the end of mass branch... ;p `e197b8cfd <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/e197b8cfd08d83c28c6fd0323d09c3f36058431d>`_
- Create long-form output for github events. `aace64d95 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/aace64d95af6270e68e561018a3d55c8beba3208>`_
- Include full irc logs in meetbot long_form repr. `7baa7c9fd <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/7baa7c9fdcdc3093596496a60d354ef96071ac49>`_
- Merge pull request #200 from fedora-infra/feature/more-long-form `57c239cb2 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/57c239cb28c0be043450f1f3aa858bba001317e2>`_
- Modernize these fas examples. `9b66461b4 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/9b66461b49e29d40b58e8047d539456af6828c3d>`_
- Convert one FAS example into a legacy test. `3610f5373 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/3610f5373a7440b523c6ad6fe5d3805c14e2f3ea>`_
- Merge pull request #201 from fedora-infra/feature/legacy-fas `08b066f71 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/08b066f71cfa84571b0da93ecf5c6a525de0914f>`_
- Add some debugging around the fas cache lock. `dceb30b96 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/dceb30b96b2eb53f24ea69b9591f48b204dc9773>`_
- Merge pull request #202 from fedora-infra/feature/debugging `adb030de1 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/adb030de10d6a1d2ba47317de625c235812b4419>`_
- Handle "release" messages from github. `b5de46eaa <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/b5de46eaaac5b193a01fc810d60d074f2c7123db>`_
- Merge pull request #203 from fedora-infra/feature/github-releases `68b366138 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/68b36613875cde28d44472c34a0de7f714e278cd>`_
- Pkgdb dropped the from_branch information when requesting a new branch `fd8dba4bb <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/fd8dba4bb183e88ed80f2b0d0b20306dc47580d1>`_
- Adjust the unit-tests to reflect the changes on the messages sent by pkgdb `aa5dc85c0 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/aa5dc85c08c291fe5f6cd24069aa4ef4a12d5c4c>`_
- Merge pull request #204 from fedora-infra/pkgdb_drop_from_branch `c272313de <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/c272313de337ee7763a2b0986631cbe0466be4ee>`_
- Fix elections messages. `3fec1f459 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/3fec1f459b682ed2b75278c94110b1780ad2d1db>`_
- Convert github.watch messages to github.star. `fbdf5fe1c <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/fbdf5fe1c8d47c13064c4ae9b3e036bcc6a9c656>`_
- Associate usernames and packages with the hotness followup messages. `1e5d95ca7 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/1e5d95ca76f14763a9d38b11b2785e979d5134c4>`_
- Merge pull request #206 from fedora-infra/feature/more-github-fixes `3f31862e3 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/3f31862e3ad71584736649aee8a544c7d0d73876>`_
- Merge pull request #207 from fedora-infra/feature/hotness-users `2dc580447 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/2dc5804477f112c6bf623c1980aec058c361e163>`_
- Merge pull request #205 from fedora-infra/feature/elections-fix `5dad82741 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/5dad82741471a050af66b612b5acf8a6ff346624>`_

0.4.0
-----

- Handle Fedora Atomic ftpsync links. `882c623bd <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/882c623bd98f9572612899c85bcbbabb91e5f879>`_
- Merge pull request #189 from fedora-infra/feature/atomic-links `5f4357368 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/5f4357368d8009ee3c45fb8e3625378fa8ca627b>`_
- The summershum icon moved. `77f01db46 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/77f01db4623d2b894b28cbfc4243eb07cbeadfa9>`_
- PEP8. `14008cf14 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/14008cf1440133e7999538302e90b8b082d37d94>`_
- Handle hotness.project.map messages. `916876f53 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/916876f53d5601b2dd202eb31172018b3331bd03>`_
- Merge pull request #191 from fedora-infra/feature/hotness-mapping `7c767a849 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/7c767a849f1763d2a044eb4ed017c383cee45889>`_
- Merge pull request #190 from fedora-infra/feature/summershum-icon-change `78b6f5e2a <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/78b6f5e2ae3757191ef8c51597fb1a95ec154c38>`_
- Find out the package concerned when processing admin.action.status.updpte `69613068c <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/69613068cc12341ff832ee1386c6f4d67d82d361>`_
- When returning the list of packages, cover the new branch request messages `68b3caf71 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/68b3caf71d410a85a3f25ddbeba94201b1a3dee8>`_
- Add the explanatory message in the human readable format `536153367 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/536153367bacf54083cb43aed4b1962aa66dc487>`_
- Add a new test: an update message for a new branch request that is denied `e13a84d5a <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/e13a84d5a3f90aada480cc730b91fbba48225164>`_
- Merge pull request #192 from fedora-infra/fix_pkgdb_for_admin_actions `0b4327faf <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/0b4327faf081c862c4ee6418df72224e4f7d3de7>`_
- 0.3.10 `036ee5bbb <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/036ee5bbb6aafcf2808b563df7fa19878b98d8a6>`_
- Create test to elicit the error from #193. `2fa9cb4e1 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/2fa9cb4e1670475cac0eab0e3fed99511b5bf1e8>`_
- Fix #193. `65270ecd1 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/65270ecd1d6a8c4b68778711746561fbf36b0621>`_
- Merge pull request #194 from fedora-infra/feature/fix-pkgdb-messages `15d0a6c7a <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/15d0a6c7ad9bb0efb316898b619b82ed7a721543>`_
- 0.3.11 `ace76a125 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/ace76a125718fe28d0e2e95d39bd768ead5190fc>`_
- Move bodhi tests to their own module. `6ff109049 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/6ff1090492c0923e351bced438f7837fa7b2e616>`_
- Handle bodhi.stack.save messages. `fba701bba <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/fba701bbaf070f96b496ff1898b11b94cb6c4ee4>`_
- Handle bodhi.stack.delete messages. `529620de6 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/529620de620c58678c0b40906c976cc7dcd3e01a>`_
- Handle bodhi.update.edit messages. `bb945a037 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/bb945a037d621fa7685f2ce64ed2b43622229818>`_
- Handle new sigul messages (via koji). `442be7de2 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/442be7de22adef9cd8121bab21e4a0d042d2d0c4>`_
- Merge pull request #196 from fedora-infra/feature/sigul `6b7f2cec2 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/6b7f2cec2b23b84097ed0f31219909c4efcfaf5d>`_
- 0.3.12 `2cf84d830 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/2cf84d830016ea9f44830468a678ec786809a4a7>`_
- Handle bodhi1 and bodhi2 buildroot override messages. `1e4e9ded7 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/1e4e9ded73afed97b4b19756d5b30812fd966aeb>`_
- Handle mashtask and update.complete.* messages. `d67d0bb9d <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/d67d0bb9d80e79fc1602988421a13afc6923fafe>`_
- Handle bodhi.update.eject messages from the mash process. `52cd572a1 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/52cd572a104bbaf05de4be4e14b8f858d11faa52>`_
- Mention the sigkey in the rpm.sign subtitle. `82797fb70 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/82797fb701a80ada5ab902779a05b25e97695fa7>`_
- Merge pull request #197 from fedora-infra/feature/sigkey `08e02b792 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/08e02b79265767b5055b9b00297794490b82fdd6>`_
- Merge pull request #195 from fedora-infra/feature/bodhi2 `4780ce209 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/4780ce209043ac2d4fa98a47e58711689350fc94>`_
- Fix tests. `aa2753037 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/aa275303744c3b06029a0008b78290244547959d>`_
- Merge pull request #198 from fedora-infra/feature/more-grouped-attrs `9804090f2 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/9804090f24f7187fa1ffe9b1ab867f6b8f92ffbc>`_
- Demote this error message. `39531fd41 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/39531fd4198cd65053e0fe3208784cec106a1210>`_
- Merge pull request #199 from fedora-infra/feature/demote-error-message `88353d4cf <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/88353d4cfc3527e004bd6957e0f61f95255f92f3>`_

0.3.9
-----

- Add and test the second kind of hotness followup message. `2dd8a3029 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/2dd8a30291c2eda3ab8e6290daae0c5d537a1d34>`_
- Mark a test as Legacy that should have been marked so a while ago. `4319119b4 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/4319119b49138590d505a1b32a022083769076af>`_
- No longer stuff package owners in msg2usernames for pkgdb. `1389de4f2 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/1389de4f295823cae23d60227e32d1f75b3e58f6>`_
- Merge pull request #184 from fedora-infra/feature/hotness-followup2 `cac1a95e5 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/cac1a95e5ef3da2edcb2e1fe3bd6420730dd11f4>`_
- Merge pull request #185 from fedora-infra/feature/pkgdb-usernames-kludge-removal `53443d205 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/53443d205f064269adae20db6c74b96f97f31b3e>`_

0.3.8
-----

- Add support for the messages sent by anitya when the admins delete a distribution `0f1a7f1d1 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/0f1a7f1d1863939760f81f21d4af5c458d376355>`_
- Fix up topic in anitya's tests `fd54958e4 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/fd54958e4484248f8f08f63bec571b6b26305d52>`_
- One more adjustement in the anitya's tests `4de012eb2 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/4de012eb25dd574e99671fd8daf80ebf032072b4>`_
- Fix topic for the anitya tests `f8f4e5295 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/f8f4e5295670748e4c14627d9bb5afbb78b681a5>`_
- Fix anitya's unit-tests `f1e55074c <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/f1e55074c4f56dfc664da4443b25177accb6d6a1>`_
- Merge pull request #182 from fedora-infra/delete_distro `34bed947b <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/34bed947b591bdb6c646ff9fbd9ae04b9a2d9b97>`_

0.3.7
-----

- Distinguish between these two anitya examples. `728f1e3b5 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/728f1e3b58aad49d66b19728ff4585f65b212f77>`_
- Typofix. `0d15c4c83 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/0d15c4c83f1dab6dd21c6910419d1a10a37d5be7>`_
- Merge pull request #178 from fedora-infra/feature/anitya-de-duplicate `001d0a503 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/001d0a5038f14f665506e9d6512f8586aea2ca71>`_
- anitya is behind ssl now. `0b7bfd039 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/0b7bfd0393a40cbe38f341620b0c420f16045904>`_
- Whoops!  Include hotness tests in the main battery. `1b38710bf <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/1b38710bfbc0e959104421be0d1626c355c20a72>`_
- Point hotness messages at partner-bz if they are from the staging environment. `a6fd536a7 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/a6fd536a7064a472c2d6a98b3197871354d26e7e>`_
- Point stg koji messages at the stg koji hub. `8984cbca7 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/8984cbca7b8287d3eb3db420fe2fc589a94f3c4c>`_
- Merge pull request #179 from fedora-infra/feature/links `ca4f3f678 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/ca4f3f678c5695f7b7efc8631ff35911a1dadadd>`_
- First pass at mirrormanager message handling. `232b817d0 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/232b817d016872996251ea7feb4459110f9ec401>`_
- netblocks messages. `2308e08f2 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/2308e08f27a9388fd956bdd1d260f7ee6ff09594>`_
- Fix string comparison in the fedimg proc. `2988d50cd <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/2988d50cdef4a2c617f20817911826f2f7863f0e>`_
- Merge pull request #181 from fedora-infra/feature/fedimg-comparison `d936eb60f <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/d936eb60f8eb83a9e03ee7bdc7d795fabb74d43a>`_
- Merge pull request #180 from fedora-infra/feature/mm2 `9bdc8293a <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/9bdc8293adb7928cf91fb80dcecd621c259cc57e>`_

0.3.6
-----

- Apparently we're not guaranteed to have this value. `3720084c7 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/3720084c7280772a34dff80cff996bce4e6c49d6>`_
- Merge pull request #164 from fedora-infra/feature/yet-another-anitya-fix `4d0486963 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/4d04869639fea1fe106ddd737a2666c6d388a8e5>`_
- Add unit-test for pkgdb's message about monitor status change `92e377a87 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/92e377a87ed20ca9d156a0a59555882bc16c433f>`_
- Adjust the pkgdb processor to handle the change in monitoring status `6d0f58fed <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/6d0f58fed357f528daa6a68356d1fe1eb5ade4ce>`_
- Remove trailing slash on pkgdb objects both in the logic and the tests `13a363f40 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/13a363f40aa5d18ace71cf6f2f1ffe1501186e31>`_
- Merge pull request #166 from fedora-infra/pkgdb `cc8274752 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/cc82747520f05ee08abc8329b3421be5ea4ad1d4>`_
- Handle mailman links with and without prefixes. `3f5d6b15e <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/3f5d6b15edbf63f0bdcbcd9d06c761113b839b5f>`_
- mailman:  convert emails to fas usernames where we can. `ce35a7abb <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/ce35a7abbf810b1e88bfab0221da81f9ce557410>`_
- mailman:  No longer chop up emails into usernames. `146235413 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/14623541345dd598785b9271b89b539c6d54d0ab>`_
- Merge pull request #167 from fedora-infra/feature/mailman-fixes `2328588fe <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/2328588fe93f14c161eda76c360d52bb6e849204>`_
- Move fas tests out into their own file. `d77079aa5 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/d77079aa538c0e2da40356fe74ba30e1c3c763c8>`_
- Add fas tests that actually cover current messages. `85c2d7e4f <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/85c2d7e4fa33a0a8fe8a405b1a18879f9d2ce9fa>`_
- Merge pull request #169 from fedora-infra/feature/fas-fixes `50e9715d0 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/50e9715d0188acb933f18de03eb404323383a68d>`_
- lookaside: Dehardcode some assumptions `9391abfee <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/9391abfee6bd02fa499c81dd4a14cde8e18915f2>`_
- Merge pull request #170 from bochecha/feature/lookasidemsgs `526d28373 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/526d2837387265ee82dc430ae2cce233d4dfbdcd>`_
- Handle anitya's fedmsg message when an admin removes a version of a project `df274699d <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/df274699d5ab967e81157b8fb2ce4521be07f496>`_
- Merge pull request #171 from fedora-infra/drop_version_anitya `130ee11e0 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/130ee11e071bcfbfa3ff2f4b97647f8e654c4649>`_
- Clarify the purpose of the anitya.project.add.tried message. `8e9fef33a <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/8e9fef33ae422534fe07d921331d29a97835c232>`_
- Fix test failures for conglomerator ordering. `690d1182b <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/690d1182b0a6b8c273b0c06faa4af07dfc8d24ce>`_
- Merge pull request #173 from fedora-infra/feature/conglom-ordering `66a923908 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/66a923908cd2f26b8bc2e0b72a97d20fa12cdb32>`_
- Merge pull request #172 from fedora-infra/feature/anitya-try `0385f486f <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/0385f486fda27f7f8f1073796dc5be090f6cbb5c>`_
- Remove a bunch of the wiki upload messages. `25f6fa69e <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/25f6fa69e40ae5813b7550eef15dc03acb402cf0>`_
- Merge pull request #174 from fedora-infra/feature/new-wiki-upload `681f485e0 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/681f485e04b281e3e607da4a71525bf69069407a>`_
- A BySubject pkgdb conglomerator. `4921a5dfa <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/4921a5dfa49112861a70cfc5e585290dcad40aee>`_
- Reorganize and add two more ACL conglomerators. `af26e8ad8 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/af26e8ad80a549be645bb48eeef2af149bcf7174>`_
- Switch order here. `bcc7f56ba <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/bcc7f56ba5378aae63f8b4f3650a07799bcc5046>`_
- The New Hotness `b50f491d9 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/b50f491d9bc499ac5110c06a3f6671dd57ff8df8>`_
- Possessive nouns. `b6b9a9d59 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/b6b9a9d596c555db9994371934358dad14dc2400>`_
- Add forgotten koji task states. `d7eb88edd <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/d7eb88eddbb12257b34a309937933ea1f3d9279e>`_
- Merge pull request #176 from fedora-infra/feature/hotness `b05104234 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/b051042347fdb61ff59add69fc73cbd462a8239c>`_
- Merge pull request #177 from fedora-infra/feature/pkgdb-conglom `9a56d0d69 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/9a56d0d69ddb5c46cfecf9cf50d922a4fe068c25>`_

0.3.5
-----

- Handle legacy anitya messages. `d052cb001 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/d052cb001dea8a7ec8766221ebcf27420b2de0d8>`_
- Merge pull request #163 from fedora-infra/feature/anitya-fixes `e117278ed <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/e117278ed8c4df2f3382c579cd3c10e216457b6f>`_

0.3.4
-----

- Require a particularly modern fedmsg for building the docs. `4cff9aee1 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/4cff9aee1b735480b9d8e887bbf4f24bbba9a8ab>`_
- Fix doc_utilities. `39d76afce <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/39d76afce8fbedde2fa9dc8353160b208d961a9f>`_
- Merge pull request #157 from fedora-infra/feature/fix-doc-utilities `e44639b5a <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/e44639b5ab80fa9c89111d6957f4a9028c021bf9>`_
- Add groups field to koschei.package.state.change `bd803dd63 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/bd803dd63a4c4175c5dd8ed25b2ad4bbca311122>`_
- Merge pull request #158 from msimacek/feature/koschei `77b94ee68 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/77b94ee6809464db47523cb7a2912be1569cbbf4>`_
- Update the unit-tests for anitya's update message `16e9eda19 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/16e9eda1994c7e2a171f8f4d6a089a54b0a9ae3f>`_
- Fix the anitya processor for the update message `faaee82d6 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/faaee82d68f45cce264e7d869985e914601ae2e8>`_
- Fix the message sent by anitya and adjust the expectations as well `69d060e26 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/69d060e26e5e4c81c9c66473cdc446b16dd28897>`_
- Fix subtitle for anitya, inverted old and new releases `e8664961c <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/e8664961c4d1542457b5d9b9236c9753660e4959>`_
- Add failing test case for #160. `3f92641c0 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/3f92641c047cbabd150e6c7a79584024b68d73de>`_
- Fix #160. `1efc6d618 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/1efc6d6184808c8fe5bfc5d3920f68d0e2e20d7f>`_
- Add unit-tests for a message of update having no "old" version being updated `672d66c9b <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/672d66c9bdc70bc90f76dc0e97717558453fbefd>`_
- Adjust the anitya processor for message having no "old" version being updated `3452e6733 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/3452e6733dadcadd6fb004b45468b2194253c163>`_
- Merge pull request #161 from fedora-infra/feature/more-pkgdb-fixes `41b24ef89 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/41b24ef899d426bf1779aa2471bc8de276d7bfda>`_
- Merge pull request #159 from fedora-infra/fix_anitya `2b6bc5fe0 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/2b6bc5fe0222f83ff709cfd29291db5c9a78af33>`_
- Have anitya re-use pkgdb's icon for now. `e3be0f1d5 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/e3be0f1d581e13e4b9b8f80148c1ab669671c15b>`_
- Merge pull request #162 from fedora-infra/feature/anitya-metadata `82d007fb9 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/82d007fb964127070a3c972fc8d6d7175a7174c5>`_

0.3.3
-----

- Fix doc building. `216283439 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/216283439b2084c472b7474d997fc3d745760892>`_
- Merge pull request #152 from fedora-infra/feature/doc-fix `3a27bd980 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/3a27bd980b0595ca79ca396fd65e0a0c66e3e480>`_
- Adjust the cnucnuweb processor and rename it to anitya processor `f56f91a31 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/f56f91a31d88e70d97dca1262224abdcd57ee97d>`_
- Rename the cnucnuweb processor to anitya processor `b7b75444a <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/b7b75444a8abad43f32a2049cc204c83c7fa4345>`_
- Adjust the cnucnuweb unit-tests for anitya `9a8c23cfb <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/9a8c23cfb82d186e5d8c4ce512080a5645c7d0df>`_
- Rename the cnucnuweb unit-tests to anitya `cc2d84ec4 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/cc2d84ec428aea8b110836c89202c9b85d322494>`_
- Run the anitya unit-tests `3694ba826 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/3694ba8261fcdbdd0316254dd691f1f5f1c79ac7>`_
- Use the anitya processor instead of the cnucnuweb one `3e4e8fd30 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/3e4e8fd303186bfaf787dc8a58f9d1cd5e864443>`_
- Merge pull request #153 from fedora-infra/anitya `c8cee4658 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/c8cee46584fd613b58e5a26860c8a2428794360e>`_
- Add processor for Koschei messages `5ce91f4ef <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/5ce91f4ef9ec4cc5dc095289504c255a4d4b49ef>`_
- Test for KoscheiProcessor `01c04bd53 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/01c04bd53c9fc2d819662118bcf6fb17ec750fcd>`_
- Fix out-of-sync docstring `336fd4665 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/336fd46656c8a45b5055a5c641166f8f56de96d9>`_
- Adjust the anitya.project.map.update to reflect how it looks in reality `e116f64bf <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/e116f64bfc17a71fbd0f5841d39a9277407f4f8d>`_
- Adjust the anitya unit-tests so that the example messages fit the reality `036ac065b <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/036ac065b8ea608bfacf1ab8d8cdd44a2eac1544>`_
- Add logic to support removal of project mapping in anitya `bbeabe08f <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/bbeabe08fbe1fe00e515fab895b96e89807cfaae>`_
- Add unit-tests for the removal of project mapping in anitya `2457e6f44 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/2457e6f44a2cfaba6f5e6c703736762fc542a375>`_
- Adjust the unit-tests for the anitya.project.remove messages to reflect the reality `0db4a3cc5 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/0db4a3cc574c7bd6f13a40a0508e0d59b080ac65>`_
- Remove build_task_id and repo_id fields from the message `3eb169c07 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/3eb169c07815f9d1c0cfe4bd88b3e848adbe8736>`_
- Add subtitle for transition from ignored `61283c5d6 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/61283c5d6cde3711327b2bb64c83ee9a299d429b>`_
- Include repo and koji instance in subtitle `e45546a5e <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/e45546a5e24da7160c151f5a89075f5088d43e77>`_
- Merge pull request #155 from msimacek/feature/koschei `129c4bf2b <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/129c4bf2b74ccab93dd99dde4a9dd72afec6fc69>`_
- Set the right topic prefix for anitya. `7cc7f8d07 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/7cc7f8d0725f358355cd160d4ce0bceac0840eab>`_
- Change the example topics. `af991d628 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/af991d628638458be0e32b6bcb83162a917614ae>`_
- Get fedoraproject emails without having to query fas.  Fix libravatars. `fc39cf40c <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/fc39cf40ceb9ae850a470ffa07cf6e831abeb01b>`_
- PEP8. `12ccf915a <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/12ccf915a14ffcd59ab4bde2cb54ba45059f6ea4>`_
- Add a non-fedora user to get avatars and usernames right. `bdead3c90 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/bdead3c9091506bfdc771b8d50790c85ad4a329d>`_
- Merge pull request #154 from fedora-infra/anitya `0e94efcd2 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/0e94efcd20c408e225c487e1020a987310568bc0>`_

0.3.2
-----

- Fix doc building. `216283439 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/216283439b2084c472b7474d997fc3d745760892>`_
- Merge pull request #152 from fedora-infra/feature/doc-fix `3a27bd980 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/3a27bd980b0595ca79ca396fd65e0a0c66e3e480>`_
- Adjust the cnucnuweb processor and rename it to anitya processor `f56f91a31 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/f56f91a31d88e70d97dca1262224abdcd57ee97d>`_
- Rename the cnucnuweb processor to anitya processor `b7b75444a <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/b7b75444a8abad43f32a2049cc204c83c7fa4345>`_
- Adjust the cnucnuweb unit-tests for anitya `9a8c23cfb <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/9a8c23cfb82d186e5d8c4ce512080a5645c7d0df>`_
- Rename the cnucnuweb unit-tests to anitya `cc2d84ec4 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/cc2d84ec428aea8b110836c89202c9b85d322494>`_
- Run the anitya unit-tests `3694ba826 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/3694ba8261fcdbdd0316254dd691f1f5f1c79ac7>`_
- Use the anitya processor instead of the cnucnuweb one `3e4e8fd30 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/3e4e8fd303186bfaf787dc8a58f9d1cd5e864443>`_
- Merge pull request #153 from fedora-infra/anitya `c8cee4658 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/c8cee46584fd613b58e5a26860c8a2428794360e>`_
- Add processor for Koschei messages `5ce91f4ef <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/5ce91f4ef9ec4cc5dc095289504c255a4d4b49ef>`_
- Test for KoscheiProcessor `01c04bd53 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/01c04bd53c9fc2d819662118bcf6fb17ec750fcd>`_
- Fix out-of-sync docstring `336fd4665 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/336fd46656c8a45b5055a5c641166f8f56de96d9>`_
- Adjust the anitya.project.map.update to reflect how it looks in reality `e116f64bf <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/e116f64bfc17a71fbd0f5841d39a9277407f4f8d>`_
- Adjust the anitya unit-tests so that the example messages fit the reality `036ac065b <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/036ac065b8ea608bfacf1ab8d8cdd44a2eac1544>`_
- Add logic to support removal of project mapping in anitya `bbeabe08f <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/bbeabe08fbe1fe00e515fab895b96e89807cfaae>`_
- Add unit-tests for the removal of project mapping in anitya `2457e6f44 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/2457e6f44a2cfaba6f5e6c703736762fc542a375>`_
- Adjust the unit-tests for the anitya.project.remove messages to reflect the reality `0db4a3cc5 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/0db4a3cc574c7bd6f13a40a0508e0d59b080ac65>`_
- Remove build_task_id and repo_id fields from the message `3eb169c07 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/3eb169c07815f9d1c0cfe4bd88b3e848adbe8736>`_
- Add subtitle for transition from ignored `61283c5d6 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/61283c5d6cde3711327b2bb64c83ee9a299d429b>`_
- Include repo and koji instance in subtitle `e45546a5e <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/e45546a5e24da7160c151f5a89075f5088d43e77>`_
- Merge pull request #155 from msimacek/feature/koschei `129c4bf2b <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/129c4bf2b74ccab93dd99dde4a9dd72afec6fc69>`_
- Set the right topic prefix for anitya. `7cc7f8d07 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/7cc7f8d0725f358355cd160d4ce0bceac0840eab>`_
- Change the example topics. `af991d628 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/af991d628638458be0e32b6bcb83162a917614ae>`_
- Get fedoraproject emails without having to query fas.  Fix libravatars. `fc39cf40c <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/fc39cf40ceb9ae850a470ffa07cf6e831abeb01b>`_
- PEP8. `12ccf915a <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/12ccf915a14ffcd59ab4bde2cb54ba45059f6ea4>`_
- Add a non-fedora user to get avatars and usernames right. `bdead3c90 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/bdead3c9091506bfdc771b8d50790c85ad4a329d>`_
- Merge pull request #154 from fedora-infra/anitya `0e94efcd2 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/0e94efcd20c408e225c487e1020a987310568bc0>`_
- 0.3.3 `fc0d4ddc9 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/fc0d4ddc99ecb3489977ee3442cc318e0e981bcd>`_
- Require a particularly modern fedmsg for building the docs. `4cff9aee1 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/4cff9aee1b735480b9d8e887bbf4f24bbba9a8ab>`_
- Fix doc_utilities. `39d76afce <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/39d76afce8fbedde2fa9dc8353160b208d961a9f>`_
- Merge pull request #157 from fedora-infra/feature/fix-doc-utilities `e44639b5a <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/e44639b5ab80fa9c89111d6957f4a9028c021bf9>`_
- Add groups field to koschei.package.state.change `bd803dd63 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/bd803dd63a4c4175c5dd8ed25b2ad4bbca311122>`_
- Merge pull request #158 from msimacek/feature/koschei `77b94ee68 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/77b94ee6809464db47523cb7a2912be1569cbbf4>`_
- Update the unit-tests for anitya's update message `16e9eda19 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/16e9eda1994c7e2a171f8f4d6a089a54b0a9ae3f>`_
- Fix the anitya processor for the update message `faaee82d6 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/faaee82d68f45cce264e7d869985e914601ae2e8>`_
- Fix the message sent by anitya and adjust the expectations as well `69d060e26 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/69d060e26e5e4c81c9c66473cdc446b16dd28897>`_
- Fix subtitle for anitya, inverted old and new releases `e8664961c <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/e8664961c4d1542457b5d9b9236c9753660e4959>`_
- Add failing test case for #160. `3f92641c0 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/3f92641c047cbabd150e6c7a79584024b68d73de>`_
- Fix #160. `1efc6d618 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/1efc6d6184808c8fe5bfc5d3920f68d0e2e20d7f>`_
- Add unit-tests for a message of update having no "old" version being updated `672d66c9b <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/672d66c9bdc70bc90f76dc0e97717558453fbefd>`_
- Adjust the anitya processor for message having no "old" version being updated `3452e6733 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/3452e6733dadcadd6fb004b45468b2194253c163>`_
- Merge pull request #161 from fedora-infra/feature/more-pkgdb-fixes `41b24ef89 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/41b24ef899d426bf1779aa2471bc8de276d7bfda>`_
- Merge pull request #159 from fedora-infra/fix_anitya `2b6bc5fe0 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/2b6bc5fe0222f83ff709cfd29291db5c9a78af33>`_
- Have anitya re-use pkgdb's icon for now. `e3be0f1d5 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/e3be0f1d581e13e4b9b8f80148c1ab669671c15b>`_
- Merge pull request #162 from fedora-infra/feature/anitya-metadata `82d007fb9 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/82d007fb964127070a3c972fc8d6d7175a7174c5>`_
- 0.3.4 `62897a2d7 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/62897a2d786d35c8c091836fa578a47b299a2ea3>`_
- Handle legacy anitya messages. `d052cb001 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/d052cb001dea8a7ec8766221ebcf27420b2de0d8>`_
- Merge pull request #163 from fedora-infra/feature/anitya-fixes `e117278ed <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/e117278ed8c4df2f3382c579cd3c10e216457b6f>`_
- 0.3.5 `e1378fc0e <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/e1378fc0e8e6ce5c58ce1780491e419002da702c>`_
- Apparently we're not guaranteed to have this value. `3720084c7 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/3720084c7280772a34dff80cff996bce4e6c49d6>`_
- Merge pull request #164 from fedora-infra/feature/yet-another-anitya-fix `4d0486963 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/4d04869639fea1fe106ddd737a2666c6d388a8e5>`_
- Add unit-test for pkgdb's message about monitor status change `92e377a87 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/92e377a87ed20ca9d156a0a59555882bc16c433f>`_
- Adjust the pkgdb processor to handle the change in monitoring status `6d0f58fed <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/6d0f58fed357f528daa6a68356d1fe1eb5ade4ce>`_
- Remove trailing slash on pkgdb objects both in the logic and the tests `13a363f40 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/13a363f40aa5d18ace71cf6f2f1ffe1501186e31>`_
- Merge pull request #166 from fedora-infra/pkgdb `cc8274752 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/cc82747520f05ee08abc8329b3421be5ea4ad1d4>`_
- Handle mailman links with and without prefixes. `3f5d6b15e <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/3f5d6b15edbf63f0bdcbcd9d06c761113b839b5f>`_
- mailman:  convert emails to fas usernames where we can. `ce35a7abb <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/ce35a7abbf810b1e88bfab0221da81f9ce557410>`_
- mailman:  No longer chop up emails into usernames. `146235413 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/14623541345dd598785b9271b89b539c6d54d0ab>`_
- Merge pull request #167 from fedora-infra/feature/mailman-fixes `2328588fe <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/2328588fe93f14c161eda76c360d52bb6e849204>`_
- Move fas tests out into their own file. `d77079aa5 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/d77079aa538c0e2da40356fe74ba30e1c3c763c8>`_
- Add fas tests that actually cover current messages. `85c2d7e4f <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/85c2d7e4fa33a0a8fe8a405b1a18879f9d2ce9fa>`_
- Merge pull request #169 from fedora-infra/feature/fas-fixes `50e9715d0 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/50e9715d0188acb933f18de03eb404323383a68d>`_
- lookaside: Dehardcode some assumptions `9391abfee <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/9391abfee6bd02fa499c81dd4a14cde8e18915f2>`_
- Merge pull request #170 from bochecha/feature/lookasidemsgs `526d28373 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/526d2837387265ee82dc430ae2cce233d4dfbdcd>`_
- Handle anitya's fedmsg message when an admin removes a version of a project `df274699d <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/df274699d5ab967e81157b8fb2ce4521be07f496>`_
- Merge pull request #171 from fedora-infra/drop_version_anitya `130ee11e0 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/130ee11e071bcfbfa3ff2f4b97647f8e654c4649>`_
- Clarify the purpose of the anitya.project.add.tried message. `8e9fef33a <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/8e9fef33ae422534fe07d921331d29a97835c232>`_
- Fix test failures for conglomerator ordering. `690d1182b <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/690d1182b0a6b8c273b0c06faa4af07dfc8d24ce>`_
- Merge pull request #173 from fedora-infra/feature/conglom-ordering `66a923908 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/66a923908cd2f26b8bc2e0b72a97d20fa12cdb32>`_
- Merge pull request #172 from fedora-infra/feature/anitya-try `0385f486f <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/0385f486fda27f7f8f1073796dc5be090f6cbb5c>`_
- Remove a bunch of the wiki upload messages. `25f6fa69e <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/25f6fa69e40ae5813b7550eef15dc03acb402cf0>`_
- Merge pull request #174 from fedora-infra/feature/new-wiki-upload `681f485e0 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/681f485e04b281e3e607da4a71525bf69069407a>`_
- A BySubject pkgdb conglomerator. `4921a5dfa <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/4921a5dfa49112861a70cfc5e585290dcad40aee>`_
- Reorganize and add two more ACL conglomerators. `af26e8ad8 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/af26e8ad80a549be645bb48eeef2af149bcf7174>`_
- Switch order here. `bcc7f56ba <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/bcc7f56ba5378aae63f8b4f3650a07799bcc5046>`_
- The New Hotness `b50f491d9 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/b50f491d9bc499ac5110c06a3f6671dd57ff8df8>`_
- Possessive nouns. `b6b9a9d59 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/b6b9a9d596c555db9994371934358dad14dc2400>`_
- Add forgotten koji task states. `d7eb88edd <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/d7eb88eddbb12257b34a309937933ea1f3d9279e>`_
- Merge pull request #176 from fedora-infra/feature/hotness `b05104234 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/b051042347fdb61ff59add69fc73cbd462a8239c>`_
- Merge pull request #177 from fedora-infra/feature/pkgdb-conglom `9a56d0d69 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/9a56d0d69ddb5c46cfecf9cf50d922a4fe068c25>`_
- 0.3.6 `4257c1a44 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/4257c1a44e6706a0cb0b1539f096077e333a99e5>`_
- Distinguish between these two anitya examples. `728f1e3b5 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/728f1e3b58aad49d66b19728ff4585f65b212f77>`_
- Typofix. `0d15c4c83 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/0d15c4c83f1dab6dd21c6910419d1a10a37d5be7>`_
- Merge pull request #178 from fedora-infra/feature/anitya-de-duplicate `001d0a503 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/001d0a5038f14f665506e9d6512f8586aea2ca71>`_
- anitya is behind ssl now. `0b7bfd039 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/0b7bfd0393a40cbe38f341620b0c420f16045904>`_
- Whoops!  Include hotness tests in the main battery. `1b38710bf <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/1b38710bfbc0e959104421be0d1626c355c20a72>`_
- Point hotness messages at partner-bz if they are from the staging environment. `a6fd536a7 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/a6fd536a7064a472c2d6a98b3197871354d26e7e>`_
- Point stg koji messages at the stg koji hub. `8984cbca7 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/8984cbca7b8287d3eb3db420fe2fc589a94f3c4c>`_
- Merge pull request #179 from fedora-infra/feature/links `ca4f3f678 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/ca4f3f678c5695f7b7efc8631ff35911a1dadadd>`_
- First pass at mirrormanager message handling. `232b817d0 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/232b817d016872996251ea7feb4459110f9ec401>`_
- netblocks messages. `2308e08f2 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/2308e08f27a9388fd956bdd1d260f7ee6ff09594>`_
- Fix string comparison in the fedimg proc. `2988d50cd <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/2988d50cdef4a2c617f20817911826f2f7863f0e>`_
- Merge pull request #181 from fedora-infra/feature/fedimg-comparison `d936eb60f <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/d936eb60f8eb83a9e03ee7bdc7d795fabb74d43a>`_
- Merge pull request #180 from fedora-infra/feature/mm2 `9bdc8293a <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/9bdc8293adb7928cf91fb80dcecd621c259cc57e>`_
- 0.3.7 `7b06763ec <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/7b06763ec4f1526c6b2ce96430864fa289cfb36d>`_
- Add support for the messages sent by anitya when the admins delete a distribution `0f1a7f1d1 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/0f1a7f1d1863939760f81f21d4af5c458d376355>`_
- Fix up topic in anitya's tests `fd54958e4 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/fd54958e4484248f8f08f63bec571b6b26305d52>`_
- One more adjustement in the anitya's tests `4de012eb2 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/4de012eb25dd574e99671fd8daf80ebf032072b4>`_
- Fix topic for the anitya tests `f8f4e5295 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/f8f4e5295670748e4c14627d9bb5afbb78b681a5>`_
- Fix anitya's unit-tests `f1e55074c <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/f1e55074c4f56dfc664da4443b25177accb6d6a1>`_
- Merge pull request #182 from fedora-infra/delete_distro `34bed947b <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/34bed947b591bdb6c646ff9fbd9ae04b9a2d9b97>`_
- 0.3.8 `5e2791f74 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/5e2791f74b3ef0b9dad193cc39c4e5422cc33289>`_
- Add and test the second kind of hotness followup message. `2dd8a3029 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/2dd8a30291c2eda3ab8e6290daae0c5d537a1d34>`_
- Mark a test as Legacy that should have been marked so a while ago. `4319119b4 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/4319119b49138590d505a1b32a022083769076af>`_
- No longer stuff package owners in msg2usernames for pkgdb. `1389de4f2 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/1389de4f295823cae23d60227e32d1f75b3e58f6>`_
- Merge pull request #184 from fedora-infra/feature/hotness-followup2 `cac1a95e5 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/cac1a95e5ef3da2edcb2e1fe3bd6420730dd11f4>`_
- Merge pull request #185 from fedora-infra/feature/pkgdb-usernames-kludge-removal `53443d205 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/53443d205f064269adae20db6c74b96f97f31b3e>`_
- 0.3.9 `f4ded79be <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/f4ded79be7b568d1e1b12778b28563e0af63c584>`_
- Handle Fedora Atomic ftpsync links. `882c623bd <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/882c623bd98f9572612899c85bcbbabb91e5f879>`_
- Merge pull request #189 from fedora-infra/feature/atomic-links `5f4357368 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/5f4357368d8009ee3c45fb8e3625378fa8ca627b>`_
- The summershum icon moved. `77f01db46 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/77f01db4623d2b894b28cbfc4243eb07cbeadfa9>`_
- PEP8. `14008cf14 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/14008cf1440133e7999538302e90b8b082d37d94>`_
- Handle hotness.project.map messages. `916876f53 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/916876f53d5601b2dd202eb31172018b3331bd03>`_
- Merge pull request #191 from fedora-infra/feature/hotness-mapping `7c767a849 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/7c767a849f1763d2a044eb4ed017c383cee45889>`_
- Merge pull request #190 from fedora-infra/feature/summershum-icon-change `78b6f5e2a <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/78b6f5e2ae3757191ef8c51597fb1a95ec154c38>`_
- Find out the package concerned when processing admin.action.status.updpte `69613068c <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/69613068cc12341ff832ee1386c6f4d67d82d361>`_
- When returning the list of packages, cover the new branch request messages `68b3caf71 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/68b3caf71d410a85a3f25ddbeba94201b1a3dee8>`_
- Add the explanatory message in the human readable format `536153367 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/536153367bacf54083cb43aed4b1962aa66dc487>`_
- Add a new test: an update message for a new branch request that is denied `e13a84d5a <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/e13a84d5a3f90aada480cc730b91fbba48225164>`_
- Merge pull request #192 from fedora-infra/fix_pkgdb_for_admin_actions `0b4327faf <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/0b4327faf081c862c4ee6418df72224e4f7d3de7>`_
- 0.3.10 `036ee5bbb <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/036ee5bbb6aafcf2808b563df7fa19878b98d8a6>`_
- Create test to elicit the error from #193. `2fa9cb4e1 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/2fa9cb4e1670475cac0eab0e3fed99511b5bf1e8>`_
- Fix #193. `65270ecd1 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/65270ecd1d6a8c4b68778711746561fbf36b0621>`_
- Merge pull request #194 from fedora-infra/feature/fix-pkgdb-messages `15d0a6c7a <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/15d0a6c7ad9bb0efb316898b619b82ed7a721543>`_
- 0.3.11 `ace76a125 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/ace76a125718fe28d0e2e95d39bd768ead5190fc>`_
- Handle new sigul messages (via koji). `442be7de2 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/442be7de22adef9cd8121bab21e4a0d042d2d0c4>`_
- Merge pull request #196 from fedora-infra/feature/sigul `6b7f2cec2 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/6b7f2cec2b23b84097ed0f31219909c4efcfaf5d>`_

0.3.12
------

- Handle new sigul messages (via koji). `442be7de2 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/442be7de22adef9cd8121bab21e4a0d042d2d0c4>`_
- Merge pull request #196 from fedora-infra/feature/sigul `6b7f2cec2 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/6b7f2cec2b23b84097ed0f31219909c4efcfaf5d>`_

0.3.11
------

- Create test to elicit the error from #193. `2fa9cb4e1 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/2fa9cb4e1670475cac0eab0e3fed99511b5bf1e8>`_
- Fix #193. `65270ecd1 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/65270ecd1d6a8c4b68778711746561fbf36b0621>`_
- Merge pull request #194 from fedora-infra/feature/fix-pkgdb-messages `15d0a6c7a <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/15d0a6c7ad9bb0efb316898b619b82ed7a721543>`_

0.3.10
------

- Add basic documentation on how to get started with fedmsg_meta_fedora_infrastructure `44bcf7c11 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/44bcf7c113dc8d188c4b1197bffa8caa6cb66c39>`_
- Embed the start documentation in the main documentation `2956dff6c <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/2956dff6c60aa62e3ba39d7dfe8d22b4f8b33fb9>`_
- Merge pull request #142 from fedora-infra/start_doc `d18f5e8ce <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/d18f5e8ceda77732e490cd54a74bf62a8bdcf495>`_
- Handle ancient ansible messages with no userid. `8305e290b <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/8305e290bd8d896fbd10fc598e5f46c6d14e289c>`_
- Merge pull request #144 from fedora-infra/feature/legacy-ansible `c2ae68bb0 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/c2ae68bb068db5571fdfd15e525232630384d418>`_
- Handle other kinds of pkgdb status updates. `5b8c5345b <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/5b8c5345b1b365ded1ac583d768a2f753c7e3454>`_
- Mark these pkgdb examples as Legacy `dbb15f79e <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/dbb15f79efc9fcea6468f60c74c1b268c53db355>`_
- Handle ancient koji messages that do not have tag info. `c71f146fd <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/c71f146fd13ae77083f4401a77e7f6a1a01e38db>`_
- Return the full patch for scm long_form. `7f93e7174 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/7f93e71743c8f1c07abf993fb8bf7324432e7589>`_
- Remove errant print statement. `e1aef8055 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/e1aef8055fd3b9a92ff0d0908356d0a87eb30853>`_
- Fix fedorahosted repo links that do not end with '.git' `135eaa4fc <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/135eaa4fc4367cd16176a310126fead81268b222>`_
- Merge pull request #149 from fedora-infra/feature/hosted-git-fixlist `9f518717b <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/9f518717b432d617044b12cd7d34b6b019bcc853>`_
- Merge pull request #145 from fedora-infra/feature/more-pkgdb `75338058d <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/75338058d8431dce292402bba9dddd1ecdeb4a47>`_
- Merge pull request #148 from fedora-infra/feature/patch-long-form `50d2e38d5 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/50d2e38d54cde33bc32015845aa914ba05676947>`_
- Merge pull request #147 from fedora-infra/feature/legacy-tagless `4a05f88a9 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/4a05f88a9295309c1e1ed0336ad576d076f12755>`_
- Revert these at @pypingou's suggestion. `13661ec89 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/13661ec8988d9d82a238883c968897aa02cd93ef>`_
- Merge pull request #146 from fedora-infra/feature/pkgdb-legacy `d2a61a143 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/d2a61a1439d9067d3c61d5315f01aba14e0d20c0>`_
- Handle enhanced bugzilla messages. `d0896ec55 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/d0896ec55c7cb775c924d3c79e943f418f634ea3>`_
- Merge pull request #151 from fedora-infra/feature/enhanced-bugzilla `30436b137 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/30436b137e47229a5a399db432cdf2d75119ad5d>`_
- 0.3.2 `154b44808 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/154b448087765d9d7291fd572ed1c8cc019fa309>`_
- Fix doc building. `216283439 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/216283439b2084c472b7474d997fc3d745760892>`_
- Merge pull request #152 from fedora-infra/feature/doc-fix `3a27bd980 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/3a27bd980b0595ca79ca396fd65e0a0c66e3e480>`_
- Adjust the cnucnuweb processor and rename it to anitya processor `f56f91a31 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/f56f91a31d88e70d97dca1262224abdcd57ee97d>`_
- Rename the cnucnuweb processor to anitya processor `b7b75444a <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/b7b75444a8abad43f32a2049cc204c83c7fa4345>`_
- Adjust the cnucnuweb unit-tests for anitya `9a8c23cfb <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/9a8c23cfb82d186e5d8c4ce512080a5645c7d0df>`_
- Rename the cnucnuweb unit-tests to anitya `cc2d84ec4 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/cc2d84ec428aea8b110836c89202c9b85d322494>`_
- Run the anitya unit-tests `3694ba826 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/3694ba8261fcdbdd0316254dd691f1f5f1c79ac7>`_
- Use the anitya processor instead of the cnucnuweb one `3e4e8fd30 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/3e4e8fd303186bfaf787dc8a58f9d1cd5e864443>`_
- Merge pull request #153 from fedora-infra/anitya `c8cee4658 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/c8cee46584fd613b58e5a26860c8a2428794360e>`_
- Add processor for Koschei messages `5ce91f4ef <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/5ce91f4ef9ec4cc5dc095289504c255a4d4b49ef>`_
- Test for KoscheiProcessor `01c04bd53 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/01c04bd53c9fc2d819662118bcf6fb17ec750fcd>`_
- Fix out-of-sync docstring `336fd4665 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/336fd46656c8a45b5055a5c641166f8f56de96d9>`_
- Adjust the anitya.project.map.update to reflect how it looks in reality `e116f64bf <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/e116f64bfc17a71fbd0f5841d39a9277407f4f8d>`_
- Adjust the anitya unit-tests so that the example messages fit the reality `036ac065b <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/036ac065b8ea608bfacf1ab8d8cdd44a2eac1544>`_
- Add logic to support removal of project mapping in anitya `bbeabe08f <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/bbeabe08fbe1fe00e515fab895b96e89807cfaae>`_
- Add unit-tests for the removal of project mapping in anitya `2457e6f44 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/2457e6f44a2cfaba6f5e6c703736762fc542a375>`_
- Adjust the unit-tests for the anitya.project.remove messages to reflect the reality `0db4a3cc5 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/0db4a3cc574c7bd6f13a40a0508e0d59b080ac65>`_
- Remove build_task_id and repo_id fields from the message `3eb169c07 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/3eb169c07815f9d1c0cfe4bd88b3e848adbe8736>`_
- Add subtitle for transition from ignored `61283c5d6 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/61283c5d6cde3711327b2bb64c83ee9a299d429b>`_
- Include repo and koji instance in subtitle `e45546a5e <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/e45546a5e24da7160c151f5a89075f5088d43e77>`_
- Merge pull request #155 from msimacek/feature/koschei `129c4bf2b <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/129c4bf2b74ccab93dd99dde4a9dd72afec6fc69>`_
- Set the right topic prefix for anitya. `7cc7f8d07 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/7cc7f8d0725f358355cd160d4ce0bceac0840eab>`_
- Change the example topics. `af991d628 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/af991d628638458be0e32b6bcb83162a917614ae>`_
- Get fedoraproject emails without having to query fas.  Fix libravatars. `fc39cf40c <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/fc39cf40ceb9ae850a470ffa07cf6e831abeb01b>`_
- PEP8. `12ccf915a <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/12ccf915a14ffcd59ab4bde2cb54ba45059f6ea4>`_
- Add a non-fedora user to get avatars and usernames right. `bdead3c90 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/bdead3c9091506bfdc771b8d50790c85ad4a329d>`_
- Merge pull request #154 from fedora-infra/anitya `0e94efcd2 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/0e94efcd20c408e225c487e1020a987310568bc0>`_
- 0.3.3 `fc0d4ddc9 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/fc0d4ddc99ecb3489977ee3442cc318e0e981bcd>`_
- Require a particularly modern fedmsg for building the docs. `4cff9aee1 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/4cff9aee1b735480b9d8e887bbf4f24bbba9a8ab>`_
- Fix doc_utilities. `39d76afce <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/39d76afce8fbedde2fa9dc8353160b208d961a9f>`_
- Merge pull request #157 from fedora-infra/feature/fix-doc-utilities `e44639b5a <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/e44639b5ab80fa9c89111d6957f4a9028c021bf9>`_
- Add groups field to koschei.package.state.change `bd803dd63 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/bd803dd63a4c4175c5dd8ed25b2ad4bbca311122>`_
- Merge pull request #158 from msimacek/feature/koschei `77b94ee68 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/77b94ee6809464db47523cb7a2912be1569cbbf4>`_
- Update the unit-tests for anitya's update message `16e9eda19 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/16e9eda1994c7e2a171f8f4d6a089a54b0a9ae3f>`_
- Fix the anitya processor for the update message `faaee82d6 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/faaee82d68f45cce264e7d869985e914601ae2e8>`_
- Fix the message sent by anitya and adjust the expectations as well `69d060e26 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/69d060e26e5e4c81c9c66473cdc446b16dd28897>`_
- Fix subtitle for anitya, inverted old and new releases `e8664961c <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/e8664961c4d1542457b5d9b9236c9753660e4959>`_
- Add failing test case for #160. `3f92641c0 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/3f92641c047cbabd150e6c7a79584024b68d73de>`_
- Fix #160. `1efc6d618 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/1efc6d6184808c8fe5bfc5d3920f68d0e2e20d7f>`_
- Add unit-tests for a message of update having no "old" version being updated `672d66c9b <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/672d66c9bdc70bc90f76dc0e97717558453fbefd>`_
- Adjust the anitya processor for message having no "old" version being updated `3452e6733 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/3452e6733dadcadd6fb004b45468b2194253c163>`_
- Merge pull request #161 from fedora-infra/feature/more-pkgdb-fixes `41b24ef89 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/41b24ef899d426bf1779aa2471bc8de276d7bfda>`_
- Merge pull request #159 from fedora-infra/fix_anitya `2b6bc5fe0 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/2b6bc5fe0222f83ff709cfd29291db5c9a78af33>`_
- Have anitya re-use pkgdb's icon for now. `e3be0f1d5 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/e3be0f1d581e13e4b9b8f80148c1ab669671c15b>`_
- Merge pull request #162 from fedora-infra/feature/anitya-metadata `82d007fb9 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/82d007fb964127070a3c972fc8d6d7175a7174c5>`_
- 0.3.4 `62897a2d7 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/62897a2d786d35c8c091836fa578a47b299a2ea3>`_
- Handle legacy anitya messages. `d052cb001 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/d052cb001dea8a7ec8766221ebcf27420b2de0d8>`_
- Merge pull request #163 from fedora-infra/feature/anitya-fixes `e117278ed <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/e117278ed8c4df2f3382c579cd3c10e216457b6f>`_
- 0.3.5 `e1378fc0e <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/e1378fc0e8e6ce5c58ce1780491e419002da702c>`_
- Apparently we're not guaranteed to have this value. `3720084c7 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/3720084c7280772a34dff80cff996bce4e6c49d6>`_
- Merge pull request #164 from fedora-infra/feature/yet-another-anitya-fix `4d0486963 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/4d04869639fea1fe106ddd737a2666c6d388a8e5>`_
- Add unit-test for pkgdb's message about monitor status change `92e377a87 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/92e377a87ed20ca9d156a0a59555882bc16c433f>`_
- Adjust the pkgdb processor to handle the change in monitoring status `6d0f58fed <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/6d0f58fed357f528daa6a68356d1fe1eb5ade4ce>`_
- Remove trailing slash on pkgdb objects both in the logic and the tests `13a363f40 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/13a363f40aa5d18ace71cf6f2f1ffe1501186e31>`_
- Merge pull request #166 from fedora-infra/pkgdb `cc8274752 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/cc82747520f05ee08abc8329b3421be5ea4ad1d4>`_
- Handle mailman links with and without prefixes. `3f5d6b15e <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/3f5d6b15edbf63f0bdcbcd9d06c761113b839b5f>`_
- mailman:  convert emails to fas usernames where we can. `ce35a7abb <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/ce35a7abbf810b1e88bfab0221da81f9ce557410>`_
- mailman:  No longer chop up emails into usernames. `146235413 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/14623541345dd598785b9271b89b539c6d54d0ab>`_
- Merge pull request #167 from fedora-infra/feature/mailman-fixes `2328588fe <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/2328588fe93f14c161eda76c360d52bb6e849204>`_
- Move fas tests out into their own file. `d77079aa5 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/d77079aa538c0e2da40356fe74ba30e1c3c763c8>`_
- Add fas tests that actually cover current messages. `85c2d7e4f <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/85c2d7e4fa33a0a8fe8a405b1a18879f9d2ce9fa>`_
- Merge pull request #169 from fedora-infra/feature/fas-fixes `50e9715d0 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/50e9715d0188acb933f18de03eb404323383a68d>`_
- lookaside: Dehardcode some assumptions `9391abfee <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/9391abfee6bd02fa499c81dd4a14cde8e18915f2>`_
- Merge pull request #170 from bochecha/feature/lookasidemsgs `526d28373 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/526d2837387265ee82dc430ae2cce233d4dfbdcd>`_
- Handle anitya's fedmsg message when an admin removes a version of a project `df274699d <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/df274699d5ab967e81157b8fb2ce4521be07f496>`_
- Merge pull request #171 from fedora-infra/drop_version_anitya `130ee11e0 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/130ee11e071bcfbfa3ff2f4b97647f8e654c4649>`_
- Clarify the purpose of the anitya.project.add.tried message. `8e9fef33a <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/8e9fef33ae422534fe07d921331d29a97835c232>`_
- Fix test failures for conglomerator ordering. `690d1182b <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/690d1182b0a6b8c273b0c06faa4af07dfc8d24ce>`_
- Merge pull request #173 from fedora-infra/feature/conglom-ordering `66a923908 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/66a923908cd2f26b8bc2e0b72a97d20fa12cdb32>`_
- Merge pull request #172 from fedora-infra/feature/anitya-try `0385f486f <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/0385f486fda27f7f8f1073796dc5be090f6cbb5c>`_
- Remove a bunch of the wiki upload messages. `25f6fa69e <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/25f6fa69e40ae5813b7550eef15dc03acb402cf0>`_
- Merge pull request #174 from fedora-infra/feature/new-wiki-upload `681f485e0 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/681f485e04b281e3e607da4a71525bf69069407a>`_
- A BySubject pkgdb conglomerator. `4921a5dfa <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/4921a5dfa49112861a70cfc5e585290dcad40aee>`_
- Reorganize and add two more ACL conglomerators. `af26e8ad8 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/af26e8ad80a549be645bb48eeef2af149bcf7174>`_
- Switch order here. `bcc7f56ba <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/bcc7f56ba5378aae63f8b4f3650a07799bcc5046>`_
- The New Hotness `b50f491d9 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/b50f491d9bc499ac5110c06a3f6671dd57ff8df8>`_
- Possessive nouns. `b6b9a9d59 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/b6b9a9d596c555db9994371934358dad14dc2400>`_
- Add forgotten koji task states. `d7eb88edd <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/d7eb88eddbb12257b34a309937933ea1f3d9279e>`_
- Merge pull request #176 from fedora-infra/feature/hotness `b05104234 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/b051042347fdb61ff59add69fc73cbd462a8239c>`_
- Merge pull request #177 from fedora-infra/feature/pkgdb-conglom `9a56d0d69 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/9a56d0d69ddb5c46cfecf9cf50d922a4fe068c25>`_
- 0.3.6 `4257c1a44 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/4257c1a44e6706a0cb0b1539f096077e333a99e5>`_
- Distinguish between these two anitya examples. `728f1e3b5 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/728f1e3b58aad49d66b19728ff4585f65b212f77>`_
- Typofix. `0d15c4c83 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/0d15c4c83f1dab6dd21c6910419d1a10a37d5be7>`_
- Merge pull request #178 from fedora-infra/feature/anitya-de-duplicate `001d0a503 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/001d0a5038f14f665506e9d6512f8586aea2ca71>`_
- anitya is behind ssl now. `0b7bfd039 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/0b7bfd0393a40cbe38f341620b0c420f16045904>`_
- Whoops!  Include hotness tests in the main battery. `1b38710bf <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/1b38710bfbc0e959104421be0d1626c355c20a72>`_
- Point hotness messages at partner-bz if they are from the staging environment. `a6fd536a7 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/a6fd536a7064a472c2d6a98b3197871354d26e7e>`_
- Point stg koji messages at the stg koji hub. `8984cbca7 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/8984cbca7b8287d3eb3db420fe2fc589a94f3c4c>`_
- Merge pull request #179 from fedora-infra/feature/links `ca4f3f678 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/ca4f3f678c5695f7b7efc8631ff35911a1dadadd>`_
- First pass at mirrormanager message handling. `232b817d0 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/232b817d016872996251ea7feb4459110f9ec401>`_
- netblocks messages. `2308e08f2 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/2308e08f27a9388fd956bdd1d260f7ee6ff09594>`_
- Fix string comparison in the fedimg proc. `2988d50cd <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/2988d50cdef4a2c617f20817911826f2f7863f0e>`_
- Merge pull request #181 from fedora-infra/feature/fedimg-comparison `d936eb60f <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/d936eb60f8eb83a9e03ee7bdc7d795fabb74d43a>`_
- Merge pull request #180 from fedora-infra/feature/mm2 `9bdc8293a <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/9bdc8293adb7928cf91fb80dcecd621c259cc57e>`_
- 0.3.7 `7b06763ec <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/7b06763ec4f1526c6b2ce96430864fa289cfb36d>`_
- Add support for the messages sent by anitya when the admins delete a distribution `0f1a7f1d1 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/0f1a7f1d1863939760f81f21d4af5c458d376355>`_
- Fix up topic in anitya's tests `fd54958e4 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/fd54958e4484248f8f08f63bec571b6b26305d52>`_
- One more adjustement in the anitya's tests `4de012eb2 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/4de012eb25dd574e99671fd8daf80ebf032072b4>`_
- Fix topic for the anitya tests `f8f4e5295 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/f8f4e5295670748e4c14627d9bb5afbb78b681a5>`_
- Fix anitya's unit-tests `f1e55074c <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/f1e55074c4f56dfc664da4443b25177accb6d6a1>`_
- Merge pull request #182 from fedora-infra/delete_distro `34bed947b <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/34bed947b591bdb6c646ff9fbd9ae04b9a2d9b97>`_
- 0.3.8 `5e2791f74 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/5e2791f74b3ef0b9dad193cc39c4e5422cc33289>`_
- Add and test the second kind of hotness followup message. `2dd8a3029 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/2dd8a30291c2eda3ab8e6290daae0c5d537a1d34>`_
- Mark a test as Legacy that should have been marked so a while ago. `4319119b4 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/4319119b49138590d505a1b32a022083769076af>`_
- No longer stuff package owners in msg2usernames for pkgdb. `1389de4f2 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/1389de4f295823cae23d60227e32d1f75b3e58f6>`_
- Merge pull request #184 from fedora-infra/feature/hotness-followup2 `cac1a95e5 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/cac1a95e5ef3da2edcb2e1fe3bd6420730dd11f4>`_
- Merge pull request #185 from fedora-infra/feature/pkgdb-usernames-kludge-removal `53443d205 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/53443d205f064269adae20db6c74b96f97f31b3e>`_
- 0.3.9 `f4ded79be <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/f4ded79be7b568d1e1b12778b28563e0af63c584>`_
- Handle Fedora Atomic ftpsync links. `882c623bd <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/882c623bd98f9572612899c85bcbbabb91e5f879>`_
- Merge pull request #189 from fedora-infra/feature/atomic-links `5f4357368 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/5f4357368d8009ee3c45fb8e3625378fa8ca627b>`_
- The summershum icon moved. `77f01db46 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/77f01db4623d2b894b28cbfc4243eb07cbeadfa9>`_
- PEP8. `14008cf14 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/14008cf1440133e7999538302e90b8b082d37d94>`_
- Handle hotness.project.map messages. `916876f53 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/916876f53d5601b2dd202eb31172018b3331bd03>`_
- Merge pull request #191 from fedora-infra/feature/hotness-mapping `7c767a849 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/7c767a849f1763d2a044eb4ed017c383cee45889>`_
- Merge pull request #190 from fedora-infra/feature/summershum-icon-change `78b6f5e2a <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/78b6f5e2ae3757191ef8c51597fb1a95ec154c38>`_
- Find out the package concerned when processing admin.action.status.updpte `69613068c <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/69613068cc12341ff832ee1386c6f4d67d82d361>`_
- When returning the list of packages, cover the new branch request messages `68b3caf71 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/68b3caf71d410a85a3f25ddbeba94201b1a3dee8>`_
- Add the explanatory message in the human readable format `536153367 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/536153367bacf54083cb43aed4b1962aa66dc487>`_
- Add a new test: an update message for a new branch request that is denied `e13a84d5a <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/e13a84d5a3f90aada480cc730b91fbba48225164>`_
- Merge pull request #192 from fedora-infra/fix_pkgdb_for_admin_actions `0b4327faf <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/0b4327faf081c862c4ee6418df72224e4f7d3de7>`_

0.3.1
-----

- Catch new subpackages. `19d315a48 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/19d315a48587c1e9798f3271e5b4865cd1b09814>`_

0.3.0
-----

- Koji messages should really have a secondary icon. `920935ecb <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/920935ecb4878aca2f6e5328362e19fd1ebf70a3>`_
- Planet gets an icon too. `7048681ad <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/7048681ad561eb349f8d5c620dfd5474d8ac90cd>`_
- Sort out the tagger icons. `a85d5dd6b <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/a85d5dd6b3e15c6ceb6e0e1c2e18accb24eae38a>`_
- Give askbot an icon, courtsey of @ryanlerch. `111ccfd30 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/111ccfd3056ec0f1d68c81a47c5be3d6209d8d76>`_
- Secondary icons for lookaside messages. `5070bc97e <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/5070bc97efca3f06ebb57cab35fdb115c5c0d0fc>`_
- Make the git fallback icon more consistent with the other categories. `59b07fe99 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/59b07fe9991ef4dd9055be443708f5743f25bd34>`_
- Include the package name in summershum message subtitles. `54ca99f52 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/54ca99f520a180d737b629b1c939aecb7123360b>`_
- Merge pull request #67 from fedora-infra/feature/icons `55bf4269a <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/55bf4269ac045ddea995646420644542aad4eeed>`_
- Merge pull request #68 from fedora-infra/feature/summershum-pkg `5bb493442 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/5bb493442979079e84cd31281e09840f9021becc>`_
- Ansible needs an icon, right? `8ad630df2 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/8ad630df2e34230fd6fc487870c132006d3a0dd7>`_
- And this one badge message could use an icon too. `11248bad1 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/11248bad10d2218483b4c5972c0b7e222cfc474f>`_
- Merge pull request #69 from fedora-infra/feature/more-icons `b8f592e59 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/b8f592e598c4a1741d11bf78d96b00ff304088e0>`_
- 0.2.10 `5864cf427 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/5864cf427080d2241ecb8c08ef32757a39b8fd9f>`_
- A processor for github2fedmsg. `11c95c4d2 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/11c95c4d2b9e2ab01a7f621171e07af13da3148a>`_
- Merge pull request #70 from fedora-infra/feature/github `365cf5365 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/365cf53657f3d1088a25514ba14a1fe6283b3370>`_
- Add tests and processor for the new ftp sync messages. `34bfa48aa <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/34bfa48aa5bf931f4b7d51a1bbe38ad69839fa9b>`_
- Merge pull request #71 from fedora-infra/feature/ftpsync `98e7e293a <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/98e7e293a12b155e93ee422ae8e1a524346bf7ce>`_
- The bytes field is actually 'human readable' `1496bbe72 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/1496bbe722cfeb38ec7a26b1b6834da7d9b4d12f>`_
- 0.2.11 `d5cd3bff5 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/d5cd3bff51d66c5fddebda4cac0bd79564472b16>`_
- Need to pass through the config here... `2ff1888a6 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/2ff1888a60fb9051d6e9a0575193ed4825a2f98b>`_
- BZ processor and a test. `3e7ce519f <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/3e7ce519fad93ee5f0ffedadac4881aa6bff62a3>`_
- Handle messages for "new bugs" `410baa648 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/410baa648361795ded8c915b7b96a68a944b8b76>`_
- Correct module doc. `e91840446 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/e918404463f885f9de89ccfae685419325c290bf>`_
- Merge pull request #72 from fedora-infra/feature/bugzilla `b7b94bcf2 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/b7b94bcf2e463413740d2535cc0f3e3fd4e5a577>`_
- Use https for copr-be. `fb4e6249f <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/fb4e6249f1cc560d089badff9166fa4b158d0dda>`_
- https for wiki links, please. `b26b8ca11 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/b26b8ca11e3554f33335cccc137ea5a3d4704c2a>`_
- https for meetbot, please. `f195772d8 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/f195772d89f333210e36a184c496d5f3ffae37bc>`_
- Merge pull request #73 from fedora-infra/feature/https `162d231a6 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/162d231a6bcc370f0503879a3558c8f92bfdb0ba>`_
- Clarify user role at endmeeting.  Fixes #29. `e74642892 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/e7464289233e0993c1d1366ef14a240ea80ead35>`_
- Merge pull request #74 from fedora-infra/feature/user-at-endmeeting `a8b5cff01 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/a8b5cff014d11de6a22cd49245180630739bddc5>`_
- Remove "slave" field from jenkins `fbf3fc841 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/fbf3fc8417dab72d2981545ffb48495a8cf3be9c>`_
- Merge pull request #75 from fedora-infra/jenkins-take2 `ac853fcee <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/ac853fcee2ace23cf08253dd37f9c4fd02016d6a>`_
- Test tagger rank change messages.  Fixes #14. `e0541cde8 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/e0541cde81c6e250e7349f31a3414501202f0a88>`_
- Merge pull request #76 from fedora-infra/feature/test-tagger-rank `413194c36 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/413194c369704c5ca666a821d12cdf4a70a1801c>`_
- First work on the ElectionsProcessor for fedora-elections `ae75f73e1 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/ae75f73e149b19274fa656790ecef3ad733e6123>`_
- Update the elections Processor now that the messages contain an agent `3b4990e72 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/3b4990e72e465bedb3904b8f7e7022fd02780296>`_
- Adjust the __link__ now that the elections is on apps `f602cfbcf <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/f602cfbcf155ba689c279c60c03412dab288fddc>`_
- Manage messages regarding elections' candidate (new, edit, delete) `dc00a61a8 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/dc00a61a83f6e2bd045c780ea63ea0f8f4a74640>`_
- Adjust the setup.py file to include the elections processor `3c6e15edc <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/3c6e15edc6eb6a9cd03153b8c5913706744223b7>`_
- Import the ElectionsProcessor from the right file `843f8cfde <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/843f8cfde54c792f783314ab04d9fe4eaba47aaa>`_
- Fix trailing slash in the link in the elections processor and make it valid python `3c731ac51 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/3c731ac514d80d66de5fab67eab90b65b4cbc21b>`_
- Fix the usernames method `540b48954 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/540b4895441297c52b450fe3b3d2bad8712cc38d>`_
- pep8 fixes to the fedocal tests `831958858 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/831958858577d313258e333ce709136d397f9dfb>`_
- Fix the name, messages from the elections are of type fedora_elections `1e6d8c61e <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/1e6d8c61e2c79dff8fd55310e30491df1a470115>`_
- Fix the topic for editing or deleting candidates (and not elections) `dd27ca13e <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/dd27ca13efdb07e7dc902ec238f418cf4499adf1>`_
- The messages are only broadcasting one candidate at a time, no list `f59ed4b3a <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/f59ed4b3a943f4f57398c979e6f3b0bd8e84cfcb>`_
- Add unit-tests for the fedora_elections messages `77ebbff64 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/77ebbff649639c3703446494787f5d2b61d8a57a>`_
- Link the unit-tests for fedora_elections into the main test suite `03887eaa1 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/03887eaa143a019500d2ec9f252cfaf090c650c6>`_
- pep8 fixes on the trac tests `90a3d0933 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/90a3d0933c65015eb09a1714e5c656851eea0055>`_
- pep8 fixes on the summershum tests `2080bdca7 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/2080bdca77d44c108e05491a0bc0b3e3c939611f>`_
- pep8 fixes on the mailman3 tests `0b0f1a69b <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/0b0f1a69bf756b2a801767462af8e838386d93d1>`_
- pep8 fixes on the pkgdb tests `7e914cc87 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/7e914cc87a1d3d71734fdb6303b8bdb6571fb8da>`_
- pep8 fixes on the jenkins tests `05d3ddb25 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/05d3ddb2569d713532ed6a0adc2850a996d53d64>`_
- pep8 fixes on the github tests `a4e11b75a <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/a4e11b75a9a32b7abdf3db39070cecd50f3d2459>`_
- pep8 fixes on the askbot tests `723536331 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/7235363314355638a55c5c3e80313da08bc4e939>`_
- pep8 fixes on the ansible tests `29d4de8e7 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/29d4de8e76c5161b37e8bcf2a8f8f19dca22cafc>`_
- pep8 fixes on the pkgdb meta file `9ddcabbee <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/9ddcabbee4dd2b8af6e4300ad0d4ffed7f384df6>`_
- pep8 fixes on the jenkins meta file `5da6fcd04 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/5da6fcd04c68ad387949f3b7c411f1f38bf00863>`_
- pep8 fixes on the fasshim meta file `c090e4281 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/c090e42812cb82b379c4f4f1b729337163ed5d30>`_
- pep8 fixes on the cnucnuweb meta file `cbcd846f9 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/cbcd846f9048088ed35966dc475e822117ed056b>`_
- pep8 fixes on fedmsg.d/base.py `8232320fa <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/8232320fa1bb1583919823337c8f143866aecfe3>`_
- pep8 fixes on the setup.py file `363058da5 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/363058da5b6db9e0a001a75afa2c7725536889a8>`_
- Merge pull request #77 from fedora-infra/elections `7dd0715b4 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/7dd0715b4f1b35363223788689fa6384b982f667>`_
- Merge pull request #78 from fedora-infra/pep8 `b787911bf <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/b787911bf1cc638a660558b7d592b116744cfd67>`_
- Be careful with copr messages here. `5a6fbd0c4 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/5a6fbd0c406db5f935b19f927933332bf3ccee43>`_
- Use the new copr frontend url. `7c0830cfc <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/7c0830cfc9cd235b0e3be872423c30d5da80f235>`_
- Merge pull request #80 from fedora-infra/feature/take-care-with-copr `cf64f50d1 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/cf64f50d1c352b25ff0ac81f9f6c11e619abee01>`_
- Retire this one bodhi masher message. `043dbad9b <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/043dbad9b9f63b7f41cb12591490ff52224dfcba>`_
- Merge pull request #82 from fedora-infra/feature/retire-masher-message `e395dd421 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/e395dd42192265c0ccee92d6d188f5218b0ca5e3>`_
- Give fedmsg.meta its own doc infrastructure. `0b866c2c3 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/0b866c2c364e546cfd26e7fd2ec8460e3da27258>`_
- Merge pull request #83 from fedora-infra/feature/doc-split `7181bf8d6 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/7181bf8d6b089033eb6dd5d830cbc860b2117b6f>`_
- Adjust the URL to point to the right pkgdb2 page `c4249c393 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/c4249c3933e22f3f109baa9ed78242f7052cfaf0>`_
- Adjust the unit-tests to use the correct URL for pkgdb2 `91b941e4f <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/91b941e4f89e3b925e3772713d0ba1bfbe08ffc1>`_
- small pep8 fix to make pep8bot happy `e9f5d285a <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/e9f5d285a4eb5dfdf75493df65d9587fc4ccb361>`_
- Merge pull request #84 from fedora-infra/pkgdb2_url `5136e3434 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/5136e343476edc3271ca1ab3cd70ec10bf512aa8>`_
- Copr icon. `a1d296828 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/a1d296828022853ee88e6b9a45fc587d858df68c>`_
- Test that icon, too. `27d0552cd <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/27d0552cdeec1162a81690c32dfa2d080a94c1e7>`_
- Icons for meetbot. `9e733ea93 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/9e733ea93d33238a01cd0f469db5ea0dcd23c76f>`_
- Just to be sure. `e0c087f96 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/e0c087f961caefa974ac7cbad679db62fbf9eb29>`_
- More being sure. `44ab1f881 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/44ab1f88149818bea1e75e2a63bdfaeb239b8644>`_
- Ignore the topics .rst doc.  It is auto generated. `b884d5b6f <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/b884d5b6fd5caba540f45d8dcbfda7084c656d7c>`_
- Update koji examples. `dc1611712 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/dc1611712652219aa5aa5b5d09ce75c498a004c7>`_
- Merge pull request #87 from fedora-infra/feature/update-koji-examples `5822fe792 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/5822fe792c4bfef104067d9a89f742482083c2d5>`_
- Merge pull request #86 from fedora-infra/feature/meetbot-icon `672917fe3 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/672917fe32cb8ad32de5355bc152fa39c5282dc8>`_
- Merge pull request #85 from fedora-infra/feature/copr-icon `bba920ec1 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/bba920ec1ac21e82551186dad1ff9e3a87f9c77e>`_
- Fix meetbot topic changes. `903861a4e <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/903861a4eb9838c35dec31fe1681f09bb8f33aee>`_
- 0.2.12 `02f169e06 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/02f169e06e923cc74316827ded14b9ea7544a951>`_
- Processor and tests for FMN messages. `f8aa9b47f <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/f8aa9b47f9c678599a846d0c2c558f7ba31edcd0>`_
- Merge pull request #88 from fedora-infra/feature/fmn `9d693257b <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/9d693257b58d9696ddda3795a1c307a9d88072b5>`_
- Actually add the code for this. `9bce4b293 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/9bce4b293e6ec07a7416c63f62f88a3ed3cbb0bd>`_
- Merge branch 'feature/fmn' into develop `2521946b3 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/2521946b36cc08ed6d42de3ca79e50d610597d96>`_
- Pkgdb: Avoid redirects to URL with trailing slash `de99f5914 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/de99f59142fca006260ea74b2ee0a8ef2c06b243>`_
- Merge pull request #92 from tyll/avoid-redirects `4d9387fc8 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/4d9387fc85f1e984769e5b7426bc31f393f31f98>`_
- Pkgdb: Make package retirement messages explicit `42d30bda3 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/42d30bda3ef9464b0a7917f5b19f927cce4a41a3>`_
- Merge pull request #91 from tyll/develop `80fc3d9ea <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/80fc3d9eaeb067fe3a4f098b65e3225497bcb784>`_
- 0.2.13 `4a838f948 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/4a838f9480912806872e902f941a6a28d89acab3>`_
- Fix .rst syntax. `ff4853a39 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/ff4853a390171e944655b9d564f9ee4ebe41a763>`_
- compose: remove unused import `93ff47576 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/93ff47576d37fc49497f7eac43272c2a76d1a503>`_
- Use https where currently possible `62a9c6cbf <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/62a9c6cbf4ab61cf6e489f9c33c798e4721a5e36>`_
- Allow mentions in bodhi comments.  /cc @codeblock. `ffe34c428 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/ffe34c428ba5c6483c0eb76d428c495f0250645d>`_
- Merge pull request #94 from fedora-infra/feature/mentions `56a3b4270 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/56a3b42705cec5e1c821c93096039c1a99adceb7>`_
- Initial go at a fedmsg meta config for the new fedimg service. `b47fa4205 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/b47fa4205c2d3bc616696cac39a20c2a4dc14624>`_
- Typofix `f4a928d1e <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/f4a928d1e6b8ccae65345d964f967860f9ee18a5>`_
- Add marked up text and tests for bodhi messages. `bc68050a5 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/bc68050a55584ae13763c9375f2b2ee239cb307c>`_
- Merge pull request #98 from fedora-infra/feature/marked-up-bodhi `f8b840b96 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/f8b840b966d89e709f9ba18731d42ff1917a75fd>`_
- Merge pull request #93 from tyll/https `7e364d43f <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/7e364d43f2caeb360dfa2cf65613efe33a597e08>`_
- Allow the FAS url to be configurable. `dfab75e91 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/dfab75e91edc6832e79dfc1f4b8e097f95d66dff>`_
- Use a nuancier icon. `e309fb85d <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/e309fb85d03d540d9d9156f4a9dd107db68323ba>`_
- Cook our own avatar links. `84ba908dd <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/84ba908dd4173e35e93b5094abb0160a8f61a5fb>`_
- Use libravatar. `07a3e0a20 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/07a3e0a20c24c3bb7e12d9fc95864074a53fef0b>`_
- Update the tests to expect libravatar. `de7a296da <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/de7a296da74c612712bb8641c7093584dd08af1d>`_
- Merge pull request #100 from fedora-infra/feature/nuancier-icon `880a12c82 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/880a12c828dee94c30f103a20beb972690241f04>`_
- Show icons in docs. `0a02161f4 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/0a02161f4e33e4e7fd1c9d91d5ca1a68eec73528>`_
- Merge pull request #102 from fedora-infra/feature/show-icons-in-docs `25c003e03 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/25c003e030ffe731c9337bf6cb7b512cb06d05ca>`_
- Merge pull request #99 from fedora-infra/feature/configurable-fas-url `403b005f0 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/403b005f019eadaa41214dd64d2b0e528bc4f9c0>`_
- Merge pull request #101 from fedora-infra/feature/libravatar `78d057b2e <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/78d057b2e949588662cbb864a2396eca59ffaf65>`_
- Remove some stuff we don't need. `9fb656b2a <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/9fb656b2af6646355809ef743a06cafb57821fef>`_
- Make successful status 'completed' instead of 'succeeded' `f75a7711a <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/f75a7711ac6f60bcefd84ebd5c7e9318e64744b5>`_
- Tweaks as per @threebean's comments. `40fd23e49 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/40fd23e49903511bf5a3d85209760a84238bee95>`_
- Author --> Authors to match other files. `e6b19ba0b <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/e6b19ba0b3f01fe6f2217bd61f75052efd5e46c4>`_
- Start writing a test for Fedimg fedmsgs. `bb8590a21 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/bb8590a21cec481d262f3ffb71a90f4f22440799>`_
- Looks like this fedimg test passes `5d6e69df5 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/5d6e69df50b03f0ab959f731b4b55bb9d7826c8a>`_
- Typofix `d282bff37 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/d282bff37a3283e3957da7de4096864880c7700a>`_
- PEP 8 `675bfcc7f <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/675bfcc7fdb7ddb034e709f7944610a32a9317b6>`_
- These things aren't sets. `f69d1742f <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/f69d1742fced458564f66343e735b4f6c38a0ded>`_
- Crucial - declare the FedimgProcessor. `7bd2ce597 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/7bd2ce59746ed4b38e2150f8cbd9bd4d0d42c703>`_
- Run fedimg tests as part of the big suite. `7f3bebc6b <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/7f3bebc6b41386dc8832eeff5b9a555eab364804>`_
- Handle github.status messages. `7b3bad3bb <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/7b3bad3bbfcb86ed9c589ac0e6610585d642cee2>`_
- Handle github.delete messages. `4222b6491 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/4222b649189a20efc3fc7efb6131dc90ff768ad5>`_
- Handle pull request review comments. `72ada211c <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/72ada211c98aa4667be0a226013361822a14f051>`_
- Reorganize the way msg2objects works for github so that it makes more sense. `b118d4e1b <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/b118d4e1b8f8f291b283ddefc946785b5ae4bede>`_
- Fix key name. `b742848e2 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/b742848e2f44f49eebeca755a4dbe3c2e15c3627>`_
- py2.6 doesn't support str.format() without indexes `4d112edca <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/4d112edcacfdf203ff9889f67d02c1b5b090756e>`_
- This should be the image name, not the URL. `ca6b47006 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/ca6b47006b471c952e90a32ced32dc1c5c2dc731>`_
- Support commit comments. `a91f1a75b <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/a91f1a75b4648d394268b5ecb42e92d0d9c50b00>`_
- Merge pull request #103 from fedora-infra/feature/fedimg-meta `90379f404 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/90379f404f95757e8b05f04e1b57ce504cfa42f4>`_
- Merge pull request #104 from fedora-infra/feature/more-github-stuff `329d97cd8 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/329d97cd85a08fe3d4bd917bda2e190efcd1827b>`_
- 0.2.14 `9b4e0e58a <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/9b4e0e58aede0a0da96c44503d0c4d2318d85eb1>`_
- Add secondary icons for some cvsadmin and releng stuff. `fc4d4759e <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/fc4d4759e064e22279f7b8d1ddc66ac832dac8a5>`_
- Merge pull request #105 from fedora-infra/feature/some-secondary-icons `4ca3d5e97 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/4ca3d5e9776accc0c70182b0b55197b8e3e46ba8>`_
- Sometimes, these can exist, but be None. `fa432bff7 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/fa432bff7e9b6712d5dbfd1e93af5f9ebaf06959>`_
- Use short hashes here. `8598913ae <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/8598913aec0cfa58563aaa58bbfd5bd00d821cd7>`_
- Merge pull request #106 from fedora-infra/feature/short-hash `f50709d99 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/f50709d99a863412386e2bed523c0681b573a2a2>`_
- Kerneltest message handler and tests. `8d1b08b83 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/8d1b08b837778aa162321157ca53a05df12de7c8>`_
- Merge pull request #108 from fedora-infra/feature/kerneltest `4be76c72d <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/4be76c72df16430cd6570aa700d7359dc6af7f3b>`_
- Remove trailing slash that are no longer is use with elections2 `6201fe737 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/6201fe7371288c7ecdaf9904d9708cece790d4c9>`_
- Adjust the unit-tests to remove the trailing slash `7a38c4c62 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/7a38c4c62586e93495e4534601070729b5c7736a>`_
- Merge pull request #113 from fedora-infra/fix_elections `87f91f142 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/87f91f142d7237a482a99c3255c1de49b0e14a96>`_
- Indicate success of copr builds. `47e4e4e0b <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/47e4e4e0b24a74de7b08d9724ac3eca5968924af>`_
- Handle case where this can be None. `6415d246c <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/6415d246c189635bb93633a30a77ca709420b12b>`_
- Fix bug in subtitle for pkgdb.branch.start `015d6efd1 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/015d6efd11ec67a51babaa98875d565e33904d72>`_
- Merge pull request #114 from fedora-infra/feature/fixups `7abaad2a2 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/7abaad2a2b371ab9da761524806ca17747074c02>`_
- 0.2.15 `cac2991d1 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/cac2991d1acb6c81cb2d2baf237c99b30dc5725e>`_
- Handle an edge case with github messages. `895dab10a <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/895dab10ab8d1881c75cb53d52cab30afb22603e>`_
- Merge pull request #115 from fedora-infra/feature/github-edge-case `a74c6e9cf <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/a74c6e9cfca33b2e2b084eb6ecdaa9bff8adcd35>`_
- Add meta code for fedimg.image.test topic `bb65093d6 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/bb65093d607cd4be6174412fae0b664cafbf0ac0>`_
- Merge pull request #116 from fedora-infra/feature/fedimg-test-messages `89cf61d20 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/89cf61d20a71dea0cc53fc69dc5645f9a228fa13>`_
- Include the chroot in the description of finished builds on copr `3dcb851e9 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/3dcb851e931a6701da069f43a31509d64097fc9c>`_
- Adjust the unit-test for copr messages to reflect the addition of the chroot on the finished build message `5ba200ff9 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/5ba200ff9b6bfb8e03763f7367294f79febbcf91>`_
- Merge pull request #118 from fedora-infra/endbuild_chroot `f513436a2 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/f513436a2bee9b2be883ece084c8693182b45907>`_
- Hide old pkgdb1 retirement messages from the docs. `7d9c23a1b <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/7d9c23a1ba3066cc0d2aae36e7b172dc8ce68441>`_
- Merge pull request #119 from fedora-infra/feature/legacy-retirement `fc257d074 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/fc257d0743793d04e28392ea17b613b0f0298533>`_
- Add support for github.watch messages. `74fd4f45b <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/74fd4f45bd6ecbb06a6f8510464367c94a4d8649>`_
- Handle both starts and stops. `9fbfe371f <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/9fbfe371feab18a85398f535e1956a647a406b98>`_
- Merge pull request #120 from fedora-infra/feature/github-watch `b65ad6ab2 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/b65ad6ab275bba61f4177980d531d0c70c69a503>`_
- Added Class and Test `ccfea0d56 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/ccfea0d56453babd29e490bfbdad5936eaf6e2a0>`_
- added class for fedora college `c140ff8ba <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/c140ff8bac230a57d3ac5613dd5d5cef633070b4>`_
- Minor changes in file description `12329eeda <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/12329eeda662f78eabd2a64fdf6b5bad5c19f038>`_
- Merge pull request #121 from hammadhaleem/develop `ab6154c59 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/ab6154c59eeba5f3d2bff22434b513253a18019b>`_
- The topic packag.update.status is not package.update `9e852081d <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/9e852081d27a47f2569d1d0a2faa831c6ed9d13c>`_
- Handle the pkgdb.package.update messages `24022da8b <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/24022da8b5664e5ab0755ebd943674548fc75207>`_
- Adjust the unit-test name for PackageUpdateStatus `222f977bf <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/222f977bf16adeda8de14ce2b330fc2533ca615f>`_
- Add unit-tests for the package.update topic `a681f1b1f <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/a681f1b1fea2d5d581b63929c35de63f75b1620f>`_
- Merge pull request #122 from fedora-infra/fix_pkgdb `698c279f9 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/698c279f9d9f601540cdd8ea335849d12040fd70>`_
- Get the tests passing again. `b241d815e <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/b241d815ed951ad49abca8e4144d683dbad96c40>`_
- 0.2.16 `1a8d00b18 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/1a8d00b18ce287e6b1a685611df17630fbaa7300>`_
- add several jenkins statuses `2b7f67a68 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/2b7f67a689413978a2b431382f9c4b8582850a2c>`_
- Merge pull request #124 from fedora-infra/jenkins-try-again `de9a741a4 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/de9a741a4530870eb9377a8ac9891a69992c90fc>`_
- 0.2.17 `edd3fe59e <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/edd3fe59ec84ab9c38248a71aa86e5ceeca1b247>`_
- Fix tests. `3643db6e1 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/3643db6e189965561aea38b6ff286e87fcf4faf7>`_
- 0.2.18 `b46069572 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/b46069572f66b9c9ab8d2661b4fa2d38095e07ab>`_
- Comment out time-sensitive test. `1a8fe7b89 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/1a8fe7b89f6f4f7193740f6bb146f67fb2835c73>`_
- Debug missing topic. `b51dcb708 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/b51dcb7087484c8f6256c76beb9c80cb861f6a4e>`_
- Add missing topic. `6a1bd32d2 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/6a1bd32d2a4d8b228de4d1d910820561e2b1ca60>`_
- Merge pull request #126 from fedora-infra/feature/more-jenkins-fixes `22175af34 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/22175af34a7bd05a43356022c86fbb290ee5424a>`_
- Handle pkgdb.package.delete. `eb73eaf92 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/eb73eaf92d1b43dc1eef57245310fa98b09cfb2a>`_
- pkgdb.package.branch.delete and pkgdb.acl.delete `0df5e488d <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/0df5e488d0624548584c19e7f1d48ab17ae7d125>`_
- Merge pull request #128 from fedora-infra/feature/those-other-pkgdb-messages `c9ab3f9ed <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/c9ab3f9ed679144cf75519ced04d469e06d08d66>`_
- Handle the new pkgdb fedmsg messages `7fa96b37c <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/7fa96b37c8cc2c02e94a3d003cfa19e8f6f3e550>`_
- Adjust the unit-tests to test for these new messages `4dbf902f9 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/4dbf902f9977f8be3b94a11a2031c23a44990b93>`_
- Merge pull request #129 from fedora-infra/new_pkgdb `2b1a61c55 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/2b1a61c5557f55efea04db46efd68763ba6a39e0>`_
- There are case where the `action` dict is not there and case where it is `f9b10d582 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/f9b10d582224e2ef903ba25f6b5aabb1e649d514>`_
- Merge pull request #130 from fedora-infra/new_pkgdb `282e8fff2 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/282e8fff213a24bf57b18998f45f863994382dd3>`_
- Handle pkgdb critpath change messages. `5cb94cdb6 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/5cb94cdb6d80453404004edb28056bbb70093e74>`_
- Merge pull request #131 from fedora-infra/feature/critpath-messages `e273a0c1d <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/e273a0c1d3185b017918c74db1dea0ee03c1f590>`_
- 0.2.19 `53205342c <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/53205342c1de9e9b8e36006dcbe178dc173e2ef6>`_
- Throw a threading lock around the fas cache. `f920b11f4 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/f920b11f4a70832888101ad78757bf8e10540935>`_
- Merge pull request #132 from fedora-infra/feature/lock-around-fas-cache `8578931c4 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/8578931c449f37326145bd9ced4b045fee768040>`_
- First bodhi conglomerator. `179b922d5 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/179b922d553e6a3494e42a757378962814e063bc>`_
- Bugfix. `3ff8ebb5a <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/3ff8ebb5a7bc408eba99abc4e1e839177280cb9e>`_
- Unnecessary.  self.produce_template(..) actually includes this. `82e84ec37 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/82e84ec37e0ae2f1ba0e43145f7dad5f4ea6ea17>`_
- Link directly to copr builds. `19229d94a <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/19229d94aa04dc0cebbac61585d2fc19920eabfc>`_
- Merge pull request #134 from fedora-infra/feature/copr-builds `c616a8a9b <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/c616a8a9b0e5dd4a86c627e858cf20fbb0c32979>`_
- Merge pull request #133 from fedora-infra/feature/first-bodhi-conglomerator `0409486e8 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/0409486e80cdffab570d4fec0f769050fc6ba64a>`_
- Hardcode topic_prefix_re. `dd68205b1 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/dd68205b15586b0969e0269c7ccafac86adfe380>`_
- Merge pull request #136 from fedora-infra/feature/topic-prefix-hardcode `6a918f896 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/6a918f896ec08e4fe373dd2a50a1708c9e724821>`_
- Split that one into two different ones: for testing and stable. `e903f7af4 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/e903f7af404245d2180ebc21d0b57ba9a7418ffe>`_
- Add two new bodhi conglomerators. `8e7ae9ddb <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/8e7ae9ddbe8515f7952edc5dac57f828a0344675>`_
- Re-namespace stuff into a submodule.  There's going to be a lot of these... `247bd9a14 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/247bd9a14b868a0289efd174e65eadd6ba5acc02>`_
- Bodhi conglomerators for comments on updates. `6802ced0f <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/6802ced0f36677ee41abd8666532b50c37625cf1>`_
- Update docstrings as per review. `a3be25dbe <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/a3be25dbee4b272d5f5e364915e2a00c1697b205>`_
- Add meta information for the new pkgdb.package.branch.new messages of pkgdb2 `188e77354 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/188e77354274d2c88317794bb415937978e39c36>`_
- Add unit-tests for the pkgdb.package.branch.new messages `5a292463f <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/5a292463f020e5b8c6149071278aa8e9de65ee96>`_
- Show the new status attribute. `b798cf243 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/b798cf2435f32c49b80d73f7d30d3e0ecd0483da>`_
- Handle messages without status gracefully `f57035f5a <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/f57035f5aa69815cde9c498f3dfcccf7db257eec>`_
- Merge pull request #137 from fedora-infra/feature/more-bodhi-conglomerators `04afd1391 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/04afd139185c6876a30925f2a81f629b20ac0a89>`_
- Merge pull request #138 from fedora-infra/new_pkgdb `9c61d3bd6 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/9c61d3bd675d7b3ef2edf961ac77a7d66f96c633>`_
- s/Old/Legacy/ `0a421598a <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/0a421598af975a919db297b57bfc90c4f3e0d15d>`_
- Merge pull request #139 from fedora-infra/feature/new_status_for_fas `fb61fa224 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/fb61fa2248fd2d95ab3546b992708ba8914b5577>`_
- Fix the copr owner/user disagreement. `3b079a3c5 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/3b079a3c566c9de690c209aa82f29e002ef47da0>`_
- Fix copr usernames() method. `a7458caf6 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/a7458caf650a4b7e634efe3080634277634a108b>`_
- Merge pull request #140 from fedora-infra/feature/copr-owner-fix `6a466ce96 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/6a466ce96e38919b7f088e377e7a0965b2d5e9b4>`_

0.2.9
-----

- Update to handle new nuancier messages. `285be6abd <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/285be6abd790ff6588e1cdab536024fbfb3c8999>`_
- Turns out that this field might not necessarily be a FAS username... `45e8f8ea0 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/45e8f8ea00bd69521936756dda091e7685e23757>`_
- Merge pull request #63 from fedora-infra/feature/nuancier-heavy `4229bb504 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/4229bb5047016b55d322ca949c5e5dac702f4c12>`_
- Legacy support - old bodhi messages don't have this field. `d5d3ed74f <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/d5d3ed74f34acc85183f9cb8ca1441e568c76e1e>`_
- Merge pull request #64 from fedora-infra/feature/bodhi-legacy `71b0d2a19 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/71b0d2a198df07d1de81fd4291ad7735ad154ca9>`_
- Add links for summershum messages. `4e6b83b14 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/4e6b83b14393afb70432d1fab7c76d2179a15c67>`_
- Merge pull request #65 from fedora-infra/feature/links-for-summershum `e370d3fa0 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/e370d3fa0c4ad7670bfcf8d5f4295097f16d8dab>`_
- Add support for upcoming jenkins messages `7f474516f <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/7f474516f0c9330e6625587dae22d7c893ad5745>`_
- Fix tests. Thanks @ralphbean! `0e824e73c <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/0e824e73cdd9ed314ccbd7761f9cfd7d0863ad69>`_
- correct copyright year `b21b42b00 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/b21b42b00446d5acb71b19d7ebc209392e498c53>`_
- Legacy support - old bodhi messages don't have this field. `8b9fce49a <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/8b9fce49a691b43d689b3d27bb87eb3bde8cb888>`_
- Add links for summershum messages. `e47ed6f3b <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/e47ed6f3ba2b9164d776baed254741acc0cf327e>`_
- Merge branch 'develop' of github.com:fedora-infra/fedmsg_meta_fedora_infrastructure into develop `f04722910 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/f047229101575d77c60e7ff59362c8820f128eb9>`_

0.2.8
-----

- Recover from failing to cache fas. `403838dd2 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/403838dd239d3aee659ae5c12459889b22f97975>`_
- Add summershum processor and tests. `ad2cb5ba3 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/ad2cb5ba3caddbcec93cc6dc3b469c10917ab030>`_
- Merge pull request #62 from fedora-infra/feature/summershum `8ff4d7f1a <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/8ff4d7f1a5e2223ca78d77d91264f870cb550f21>`_
- Merge pull request #61 from fedora-infra/feature/careful-with-the-fascache `0f7c1944c <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/0f7c1944cbb1af65391ef425cd8c0e9e783246d2>`_

0.2.7
-----

- Avoid modifying the original message in that last feature. `de02d9e1d <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/de02d9e1dabf5c9818b6b3505e5396f1363aaad8>`_

0.2.6
-----

- Add meta information and tests for the new messages added to fedocal `4f8a864dc <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/4f8a864dca3294aace306a4a95be6852bd7e0dd4>`_
- Update the pseudo messages to reflect changes to fedocal `544931a19 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/544931a19d3d943f92e93be173973ba86695fc6a>`_
- Merge pull request #55 from fedora-infra/fedocal `1479eb33b <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/1479eb33b19d5ed968d38286b27626651f31cb74>`_
- Use a new location for rawhide compose links.  Fixes #56. `4ca0a55a3 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/4ca0a55a39e12d340cd0d662fa8169310f9e28f0>`_
- Merge pull request #57 from fedora-infra/feature/new-compose-links `87bee86ec <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/87bee86ecd8615f1104938675ed20e20a7cee6f8>`_
- Handle cancelled scratch builds. `6fce5f96a <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/6fce5f96aedd2c05edfd0793646c9a8df433c711>`_
- Merge pull request #58 from fedora-infra/feature/cancelled-scratch-build `2f88e4026 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/2f88e40262b9812d370e8c2c13d1975e309a2e76>`_
- Add tests and processor stuff for new tagger usage messages. `c0c979b76 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/c0c979b763b60476508ca9e7c6cae622ed6b04a3>`_
- Handle anonymous users here. `7c0386c87 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/7c0386c8794ef50091e847f1181ec32a83b2e1ef>`_
- Merge pull request #59 from fedora-infra/feature/tagger-usage-toggle `e05fed039 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/e05fed039eb2e9d358da0389ee5eefa4ecafc72b>`_
- Adjust entry point name to match the topic modname. `981cacde2 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/981cacde25a2a4cdcd5d9fa57e2c63ca737b3ac1>`_
- Distinguish between the primary koji instance and the secondary ones. `733ba3f90 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/733ba3f90b9d942a9ff8d73ec655bb2f72b2b538>`_
- Merge pull request #60 from fedora-infra/feature/secondary-kojis `4bf8d14e9 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/4bf8d14e912c6b564e6518bb8b22cefe21d77dcb>`_

0.2.5
-----

- Fixed docstring for the bodhi multi-build update test `3db4e27c0 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/3db4e27c0dfd757ee2fbae4f5022f3b312574ae1>`_
- Tests for cnucnuweb messages. `8130a748c <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/8130a748c7be938304386934fa5965f7f285fa25>`_
- Test for new version messages. `c23c9d280 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/c23c9d2801b5f2eeb871da20041b84647d96bd1a>`_
- Add instructions to the README. `4d1c8efeb <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/4d1c8efeb41c172701d2a883b672da5c90ede980>`_
- cnucnu processor written to the tests. `3ef6caebf <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/3ef6caebfe6a9f5e5e20d1b6ee01dbff690a653a>`_
- Merge branch 'develop' of github.com:fedora-infra/fedmsg_meta_fedora_infrastructure into develop `8a013f5ca <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/8a013f5caae4f4ae781afe98fd60d87ca735f928>`_
- RFE: https://github.com/fedora-infra/fedmsg/issues/118 `f437dc51d <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/f437dc51dc79dfbb6c94fba1b1b45807e25a638c>`_
- Merge pull request #50 from fedora-infra/feature/cnucnuweb `5dc92b4ea <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/5dc92b4eaf9dd72f2ab19f09ee8bea01b3a7ef3f>`_
- Handle scratch builds. `1626fda81 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/1626fda81eb536684594f18514702ecdf68a2f2b>`_
- Support for epelbeta compose messages.  Fixes #52. `af8511171 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/af8511171a0315c6ddfce3734ab4c073f0935c60>`_
- Merge pull request #51 from fedora-infra/feature/scratch-builds `32154f6cb <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/32154f6cbb3e1dbff57c814f1a57365f80293a38>`_
- Merge pull request #53 from fedora-infra/feature/epelbeta `03ba3c8cd <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/03ba3c8cdf7cdecabc7b9e80010c40acfb7f5428>`_

0.2.4
-----

- disable avatar test `5845dae6c <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/5845dae6cf2f666397d0495b914abbd5431fd786>`_
- Handle the new badges message. `cd8973c74 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/cd8973c740bf23c2b09217342387e45a89b9ed40>`_
- For the very first time. `846f90774 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/846f90774515b5905a053b854ed22da665c2dd54>`_
- Merge pull request #42 from fedora-infra/feature/badges-login `770bb4b19 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/770bb4b199190464e95a594949b26e39a02dd14a>`_
- Add the __doc__ trick to the bottom of all the test modules. `5bee972ad <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/5bee972ad7703590c66daf0945dfa75e39df2956>`_
- Fix issue with import (kitchen) and refactoring the code. `7d66afb02 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/7d66afb02c4bc0e862d960c5820bca302c228ab2>`_
- Reorder to install requires `81f470470 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/81f470470cb09c6e441f97bb41111affbc4f4034>`_
- PEP8, refactoring `839979c56 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/839979c567042376446df4c2a00856124cb6cb80>`_
- Remove blank spaces in bodhi.py msg `f0fa59956 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/f0fa5995660481ccfb1ea0d92f94fafa8be14695>`_
- Change in setup.py, sys.version_info < (2, 7) `0df4fcd05 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/0df4fcd05fd066a10607fab7d9e0b29b0239fef7>`_
- PEP8 `7e2e3926c <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/7e2e3926c408dd3da58cb2627bffa3bec7ea6e3a>`_
- Move that docs trick into a function. `10389be00 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/10389be001dcfd4b4f27175a818a1834186b91ab>`_
- PEP8/cosmetic while I'm here. `d214ac277 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/d214ac277d8b3c4fa5d0c1d2dfc4e77b5e08a92a>`_
- Add forgotten file. `c10f0cd21 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/c10f0cd21d7ed4015ac332c162dffca424cde343>`_
- Merge pull request #43 from fedora-infra/feature/docs-fix `9ba32c187 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/9ba32c187e3c75076830d9bab3d69c725d5f921c>`_
- Update bodhi.py `13e07f110 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/13e07f110ee566fdff4146dbf7c01fde641c1a3d>`_
- Update setup.py `3b1eb842f <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/3b1eb842fa0643646a4dcd3915248619c7a6f838>`_
- Merge pull request #44 from yograterol/develop `d899914c1 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/d899914c173790766204e0110bc63bef5a56fa71>`_
- Replace string concatentation with literals `05005c6ad <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/05005c6adbe772ace3f56c652bb5a32f21eeba63>`_
- Merge pull request #45 from echevemaster/develop `a4fcc2fc8 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/a4fcc2fc8c5a8e7f29dd91344b7a16c51971f254>`_
- Make Git icons square `9be80070f <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/9be80070f5a4c392d1f4410065268f17d1a02f35>`_
- Fix tests for git logo change `459e51399 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/459e5139969875e1c08728d90501bb2c989ec100>`_
- whoops `5d60aa18a <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/5d60aa18afac298152c6659882a17befd35fe10d>`_
- Merge pull request #46 from fedora-infra/feature/square-git-logo `b909ef640 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/b909ef64086916d7adc126c5df42087c982fe22a>`_
- Handle old compose branches. `a783a995d <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/a783a995d17a348d1b0b177b300f9c47332392a4>`_
- Copr processor with accompanying tests. `57639b9ad <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/57639b9ad114c185a3665fc82dd7d77d747fd746>`_
- Merge pull request #47 from fedora-infra/feature/old-compose-branches `1f85a8b95 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/1f85a8b95e7efb33b521d70dad01ea40d3d4775f>`_
- Support copr.worker.create messages. `9f8fbccf9 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/9f8fbccf9c68a720b19cc11850b7c147f33dad12>`_
- Merge pull request #48 from fedora-infra/feature/coprs `fa5c09ec2 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/fa5c09ec229e2bd33839ea8cd43ecbd710d7e845>`_

0.2.3
-----

- Add message handlers for fedocal. `61310888c <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/61310888cfb1d827dfb87cf6ebf7016fd49bdc10>`_
- Update owner to point-of-contact for pkgdb2. `314985840 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/3149858404cb5324e040acbb6fab1ff47661e340>`_
- Handle new package.update message format. `87c0689fb <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/87c0689fb3c589c3c777eae55351abcb7c17f07e>`_
- Handle new branch start and complete messages. `503fb1550 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/503fb1550e23c6b847976b29bc0ce86e4e70a193>`_
- Handle messages for new pkgdb collections. `c0ad7c834 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/c0ad7c834f7e9c701ecca727307047ad77b560ad>`_
- Handle messages for updated pkgdb collections. `500937f9d <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/500937f9d45f4747b2c29c825bac22f54f5eb800>`_
- Support relative delta stuff for fedocal reminders. `7229b93d0 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/7229b93d0698a8becf5736240c9cd97d586c025c>`_
- Link directly to fedocal meetings. `87fd59bdc <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/87fd59bdcb1e0db3cde7396c7475deedffb77f3f>`_
- Merge branch 'feature/fedocal' into develop `add3992cf <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/add3992cf3b3cea646b15eda2d75f465da4fd30f>`_
- Keep formatting consistent. `4f90fd269 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/4f90fd2698d26954b3cb0ebf351787999e0b4861>`_
- Merge pull request #38 from fedora-infra/feature/packagedb2 `cc9d468f3 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/cc9d468f39c43ef89f6c4d89cb6830099379ce07>`_

0.2.2
-----

- Add message handlers for fedocal. `61310888c <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/61310888cfb1d827dfb87cf6ebf7016fd49bdc10>`_
- Update owner to point-of-contact for pkgdb2. `314985840 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/3149858404cb5324e040acbb6fab1ff47661e340>`_
- Handle new package.update message format. `87c0689fb <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/87c0689fb3c589c3c777eae55351abcb7c17f07e>`_
- Handle new branch start and complete messages. `503fb1550 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/503fb1550e23c6b847976b29bc0ce86e4e70a193>`_
- Handle messages for new pkgdb collections. `c0ad7c834 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/c0ad7c834f7e9c701ecca727307047ad77b560ad>`_
- Handle messages for updated pkgdb collections. `500937f9d <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/500937f9d45f4747b2c29c825bac22f54f5eb800>`_
- Support relative delta stuff for fedocal reminders. `7229b93d0 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/7229b93d0698a8becf5736240c9cd97d586c025c>`_
- Link directly to fedocal meetings. `87fd59bdc <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/87fd59bdcb1e0db3cde7396c7475deedffb77f3f>`_
- Merge branch 'feature/fedocal' into develop `add3992cf <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/add3992cf3b3cea646b15eda2d75f465da4fd30f>`_
- Keep formatting consistent. `4f90fd269 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/4f90fd2698d26954b3cb0ebf351787999e0b4861>`_
- Merge pull request #38 from fedora-infra/feature/packagedb2 `cc9d468f3 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/cc9d468f39c43ef89f6c4d89cb6830099379ce07>`_
- 0.2.3 `bab0c0018 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/bab0c00187b82b1143f5bd63f145ef4cba04e91a>`_
- disable avatar test `5845dae6c <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/5845dae6cf2f666397d0495b914abbd5431fd786>`_
- Handle the new badges message. `cd8973c74 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/cd8973c740bf23c2b09217342387e45a89b9ed40>`_
- For the very first time. `846f90774 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/846f90774515b5905a053b854ed22da665c2dd54>`_
- Merge pull request #42 from fedora-infra/feature/badges-login `770bb4b19 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/770bb4b199190464e95a594949b26e39a02dd14a>`_
- Add the __doc__ trick to the bottom of all the test modules. `5bee972ad <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/5bee972ad7703590c66daf0945dfa75e39df2956>`_
- Fix issue with import (kitchen) and refactoring the code. `7d66afb02 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/7d66afb02c4bc0e862d960c5820bca302c228ab2>`_
- Reorder to install requires `81f470470 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/81f470470cb09c6e441f97bb41111affbc4f4034>`_
- PEP8, refactoring `839979c56 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/839979c567042376446df4c2a00856124cb6cb80>`_
- Remove blank spaces in bodhi.py msg `f0fa59956 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/f0fa5995660481ccfb1ea0d92f94fafa8be14695>`_
- Change in setup.py, sys.version_info < (2, 7) `0df4fcd05 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/0df4fcd05fd066a10607fab7d9e0b29b0239fef7>`_
- PEP8 `7e2e3926c <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/7e2e3926c408dd3da58cb2627bffa3bec7ea6e3a>`_
- Move that docs trick into a function. `10389be00 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/10389be001dcfd4b4f27175a818a1834186b91ab>`_
- PEP8/cosmetic while I'm here. `d214ac277 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/d214ac277d8b3c4fa5d0c1d2dfc4e77b5e08a92a>`_
- Add forgotten file. `c10f0cd21 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/c10f0cd21d7ed4015ac332c162dffca424cde343>`_
- Merge pull request #43 from fedora-infra/feature/docs-fix `9ba32c187 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/9ba32c187e3c75076830d9bab3d69c725d5f921c>`_
- Update bodhi.py `13e07f110 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/13e07f110ee566fdff4146dbf7c01fde641c1a3d>`_
- Update setup.py `3b1eb842f <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/3b1eb842fa0643646a4dcd3915248619c7a6f838>`_
- Merge pull request #44 from yograterol/develop `d899914c1 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/d899914c173790766204e0110bc63bef5a56fa71>`_
- Replace string concatentation with literals `05005c6ad <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/05005c6adbe772ace3f56c652bb5a32f21eeba63>`_
- Merge pull request #45 from echevemaster/develop `a4fcc2fc8 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/a4fcc2fc8c5a8e7f29dd91344b7a16c51971f254>`_
- Make Git icons square `9be80070f <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/9be80070f5a4c392d1f4410065268f17d1a02f35>`_
- Fix tests for git logo change `459e51399 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/459e5139969875e1c08728d90501bb2c989ec100>`_
- whoops `5d60aa18a <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/5d60aa18afac298152c6659882a17befd35fe10d>`_
- Merge pull request #46 from fedora-infra/feature/square-git-logo `b909ef640 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/b909ef64086916d7adc126c5df42087c982fe22a>`_
- Handle old compose branches. `a783a995d <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/a783a995d17a348d1b0b177b300f9c47332392a4>`_
- Copr processor with accompanying tests. `57639b9ad <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/57639b9ad114c185a3665fc82dd7d77d747fd746>`_
- Merge pull request #47 from fedora-infra/feature/old-compose-branches `1f85a8b95 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/1f85a8b95e7efb33b521d70dad01ea40d3d4775f>`_
- Support copr.worker.create messages. `9f8fbccf9 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/9f8fbccf9c68a720b19cc11850b7c147f33dad12>`_
- Merge pull request #48 from fedora-infra/feature/coprs `fa5c09ec2 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/fa5c09ec229e2bd33839ea8cd43ecbd710d7e845>`_
- 0.2.4 `4462b341f <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/4462b341f36a8693fc3f739f38c96a4e2a554ddb>`_
- Fixed docstring for the bodhi multi-build update test `3db4e27c0 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/3db4e27c0dfd757ee2fbae4f5022f3b312574ae1>`_
- Tests for cnucnuweb messages. `8130a748c <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/8130a748c7be938304386934fa5965f7f285fa25>`_
- Test for new version messages. `c23c9d280 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/c23c9d2801b5f2eeb871da20041b84647d96bd1a>`_
- Add instructions to the README. `4d1c8efeb <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/4d1c8efeb41c172701d2a883b672da5c90ede980>`_
- cnucnu processor written to the tests. `3ef6caebf <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/3ef6caebfe6a9f5e5e20d1b6ee01dbff690a653a>`_
- Merge branch 'develop' of github.com:fedora-infra/fedmsg_meta_fedora_infrastructure into develop `8a013f5ca <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/8a013f5caae4f4ae781afe98fd60d87ca735f928>`_
- RFE: https://github.com/fedora-infra/fedmsg/issues/118 `f437dc51d <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/f437dc51dc79dfbb6c94fba1b1b45807e25a638c>`_
- Merge pull request #50 from fedora-infra/feature/cnucnuweb `5dc92b4ea <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/5dc92b4eaf9dd72f2ab19f09ee8bea01b3a7ef3f>`_
- Handle scratch builds. `1626fda81 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/1626fda81eb536684594f18514702ecdf68a2f2b>`_
- Support for epelbeta compose messages.  Fixes #52. `af8511171 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/af8511171a0315c6ddfce3734ab4c073f0935c60>`_
- Merge pull request #51 from fedora-infra/feature/scratch-builds `32154f6cb <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/32154f6cbb3e1dbff57c814f1a57365f80293a38>`_
- Merge pull request #53 from fedora-infra/feature/epelbeta `03ba3c8cd <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/03ba3c8cdf7cdecabc7b9e80010c40acfb7f5428>`_
- 0.2.5 `28bbb0a13 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/28bbb0a13d193d1d7da6c7f0f74232bb25ff442f>`_
- Add meta information and tests for the new messages added to fedocal `4f8a864dc <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/4f8a864dca3294aace306a4a95be6852bd7e0dd4>`_
- Update the pseudo messages to reflect changes to fedocal `544931a19 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/544931a19d3d943f92e93be173973ba86695fc6a>`_
- Merge pull request #55 from fedora-infra/fedocal `1479eb33b <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/1479eb33b19d5ed968d38286b27626651f31cb74>`_
- Use a new location for rawhide compose links.  Fixes #56. `4ca0a55a3 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/4ca0a55a39e12d340cd0d662fa8169310f9e28f0>`_
- Merge pull request #57 from fedora-infra/feature/new-compose-links `87bee86ec <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/87bee86ecd8615f1104938675ed20e20a7cee6f8>`_
- Handle cancelled scratch builds. `6fce5f96a <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/6fce5f96aedd2c05edfd0793646c9a8df433c711>`_
- Merge pull request #58 from fedora-infra/feature/cancelled-scratch-build `2f88e4026 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/2f88e40262b9812d370e8c2c13d1975e309a2e76>`_
- Add tests and processor stuff for new tagger usage messages. `c0c979b76 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/c0c979b763b60476508ca9e7c6cae622ed6b04a3>`_
- Handle anonymous users here. `7c0386c87 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/7c0386c8794ef50091e847f1181ec32a83b2e1ef>`_
- Merge pull request #59 from fedora-infra/feature/tagger-usage-toggle `e05fed039 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/e05fed039eb2e9d358da0389ee5eefa4ecafc72b>`_
- Adjust entry point name to match the topic modname. `981cacde2 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/981cacde25a2a4cdcd5d9fa57e2c63ca737b3ac1>`_
- Distinguish between the primary koji instance and the secondary ones. `733ba3f90 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/733ba3f90b9d942a9ff8d73ec655bb2f72b2b538>`_
- Merge pull request #60 from fedora-infra/feature/secondary-kojis `4bf8d14e9 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/4bf8d14e912c6b564e6518bb8b22cefe21d77dcb>`_
- 0.2.6 `cd4676bd5 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/cd4676bd56ba059eeedb84f2686f99a126d440fb>`_
- Avoid modifying the original message in that last feature. `de02d9e1d <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/de02d9e1dabf5c9818b6b3505e5396f1363aaad8>`_
- 0.2.7 `8ff643c84 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/8ff643c84c90b87eda06a15faed5175b1bff9ce2>`_
- Recover from failing to cache fas. `403838dd2 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/403838dd239d3aee659ae5c12459889b22f97975>`_
- Add summershum processor and tests. `ad2cb5ba3 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/ad2cb5ba3caddbcec93cc6dc3b469c10917ab030>`_
- Merge pull request #62 from fedora-infra/feature/summershum `8ff4d7f1a <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/8ff4d7f1a5e2223ca78d77d91264f870cb550f21>`_
- Merge pull request #61 from fedora-infra/feature/careful-with-the-fascache `0f7c1944c <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/0f7c1944cbb1af65391ef425cd8c0e9e783246d2>`_
- 0.2.8 `61e71be95 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/61e71be957e3c77fb7fb1102315c526f835874f0>`_
- Update to handle new nuancier messages. `285be6abd <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/285be6abd790ff6588e1cdab536024fbfb3c8999>`_
- Turns out that this field might not necessarily be a FAS username... `45e8f8ea0 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/45e8f8ea00bd69521936756dda091e7685e23757>`_
- Merge pull request #63 from fedora-infra/feature/nuancier-heavy `4229bb504 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/4229bb5047016b55d322ca949c5e5dac702f4c12>`_
- Legacy support - old bodhi messages don't have this field. `d5d3ed74f <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/d5d3ed74f34acc85183f9cb8ca1441e568c76e1e>`_
- Merge pull request #64 from fedora-infra/feature/bodhi-legacy `71b0d2a19 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/71b0d2a198df07d1de81fd4291ad7735ad154ca9>`_
- Add links for summershum messages. `4e6b83b14 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/4e6b83b14393afb70432d1fab7c76d2179a15c67>`_
- Merge pull request #65 from fedora-infra/feature/links-for-summershum `e370d3fa0 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/e370d3fa0c4ad7670bfcf8d5f4295097f16d8dab>`_
- Add support for upcoming jenkins messages `7f474516f <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/7f474516f0c9330e6625587dae22d7c893ad5745>`_
- Fix tests. Thanks @ralphbean! `0e824e73c <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/0e824e73cdd9ed314ccbd7761f9cfd7d0863ad69>`_
- correct copyright year `b21b42b00 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/b21b42b00446d5acb71b19d7ebc209392e498c53>`_
- Legacy support - old bodhi messages don't have this field. `8b9fce49a <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/8b9fce49a691b43d689b3d27bb87eb3bde8cb888>`_
- Add links for summershum messages. `e47ed6f3b <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/e47ed6f3ba2b9164d776baed254741acc0cf327e>`_
- Merge branch 'develop' of github.com:fedora-infra/fedmsg_meta_fedora_infrastructure into develop `f04722910 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/f047229101575d77c60e7ff59362c8820f128eb9>`_
- 0.2.9 `fff744d0a <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/fff744d0a481d6e6acb30357d4deba6be8c4135f>`_
- Koji messages should really have a secondary icon. `920935ecb <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/920935ecb4878aca2f6e5328362e19fd1ebf70a3>`_
- Planet gets an icon too. `7048681ad <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/7048681ad561eb349f8d5c620dfd5474d8ac90cd>`_
- Sort out the tagger icons. `a85d5dd6b <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/a85d5dd6b3e15c6ceb6e0e1c2e18accb24eae38a>`_
- Give askbot an icon, courtsey of @ryanlerch. `111ccfd30 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/111ccfd3056ec0f1d68c81a47c5be3d6209d8d76>`_
- Secondary icons for lookaside messages. `5070bc97e <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/5070bc97efca3f06ebb57cab35fdb115c5c0d0fc>`_
- Make the git fallback icon more consistent with the other categories. `59b07fe99 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/59b07fe9991ef4dd9055be443708f5743f25bd34>`_
- Include the package name in summershum message subtitles. `54ca99f52 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/54ca99f520a180d737b629b1c939aecb7123360b>`_
- Merge pull request #67 from fedora-infra/feature/icons `55bf4269a <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/55bf4269ac045ddea995646420644542aad4eeed>`_
- Merge pull request #68 from fedora-infra/feature/summershum-pkg `5bb493442 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/5bb493442979079e84cd31281e09840f9021becc>`_
- Ansible needs an icon, right? `8ad630df2 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/8ad630df2e34230fd6fc487870c132006d3a0dd7>`_
- And this one badge message could use an icon too. `11248bad1 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/11248bad10d2218483b4c5972c0b7e222cfc474f>`_
- Merge pull request #69 from fedora-infra/feature/more-icons `b8f592e59 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/b8f592e598c4a1741d11bf78d96b00ff304088e0>`_
- 0.2.10 `5864cf427 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/5864cf427080d2241ecb8c08ef32757a39b8fd9f>`_
- A processor for github2fedmsg. `11c95c4d2 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/11c95c4d2b9e2ab01a7f621171e07af13da3148a>`_
- Merge pull request #70 from fedora-infra/feature/github `365cf5365 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/365cf53657f3d1088a25514ba14a1fe6283b3370>`_
- Add tests and processor for the new ftp sync messages. `34bfa48aa <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/34bfa48aa5bf931f4b7d51a1bbe38ad69839fa9b>`_
- Merge pull request #71 from fedora-infra/feature/ftpsync `98e7e293a <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/98e7e293a12b155e93ee422ae8e1a524346bf7ce>`_
- The bytes field is actually 'human readable' `1496bbe72 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/1496bbe722cfeb38ec7a26b1b6834da7d9b4d12f>`_
- 0.2.11 `d5cd3bff5 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/d5cd3bff51d66c5fddebda4cac0bd79564472b16>`_
- Need to pass through the config here... `2ff1888a6 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/2ff1888a60fb9051d6e9a0575193ed4825a2f98b>`_
- BZ processor and a test. `3e7ce519f <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/3e7ce519fad93ee5f0ffedadac4881aa6bff62a3>`_
- Handle messages for "new bugs" `410baa648 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/410baa648361795ded8c915b7b96a68a944b8b76>`_
- Correct module doc. `e91840446 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/e918404463f885f9de89ccfae685419325c290bf>`_
- Merge pull request #72 from fedora-infra/feature/bugzilla `b7b94bcf2 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/b7b94bcf2e463413740d2535cc0f3e3fd4e5a577>`_
- Use https for copr-be. `fb4e6249f <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/fb4e6249f1cc560d089badff9166fa4b158d0dda>`_
- https for wiki links, please. `b26b8ca11 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/b26b8ca11e3554f33335cccc137ea5a3d4704c2a>`_
- https for meetbot, please. `f195772d8 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/f195772d89f333210e36a184c496d5f3ffae37bc>`_
- Merge pull request #73 from fedora-infra/feature/https `162d231a6 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/162d231a6bcc370f0503879a3558c8f92bfdb0ba>`_
- Clarify user role at endmeeting.  Fixes #29. `e74642892 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/e7464289233e0993c1d1366ef14a240ea80ead35>`_
- Merge pull request #74 from fedora-infra/feature/user-at-endmeeting `a8b5cff01 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/a8b5cff014d11de6a22cd49245180630739bddc5>`_
- Remove "slave" field from jenkins `fbf3fc841 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/fbf3fc8417dab72d2981545ffb48495a8cf3be9c>`_
- Merge pull request #75 from fedora-infra/jenkins-take2 `ac853fcee <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/ac853fcee2ace23cf08253dd37f9c4fd02016d6a>`_
- Test tagger rank change messages.  Fixes #14. `e0541cde8 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/e0541cde81c6e250e7349f31a3414501202f0a88>`_
- Merge pull request #76 from fedora-infra/feature/test-tagger-rank `413194c36 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/413194c369704c5ca666a821d12cdf4a70a1801c>`_
- First work on the ElectionsProcessor for fedora-elections `ae75f73e1 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/ae75f73e149b19274fa656790ecef3ad733e6123>`_
- Update the elections Processor now that the messages contain an agent `3b4990e72 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/3b4990e72e465bedb3904b8f7e7022fd02780296>`_
- Adjust the __link__ now that the elections is on apps `f602cfbcf <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/f602cfbcf155ba689c279c60c03412dab288fddc>`_
- Manage messages regarding elections' candidate (new, edit, delete) `dc00a61a8 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/dc00a61a83f6e2bd045c780ea63ea0f8f4a74640>`_
- Adjust the setup.py file to include the elections processor `3c6e15edc <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/3c6e15edc6eb6a9cd03153b8c5913706744223b7>`_
- Import the ElectionsProcessor from the right file `843f8cfde <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/843f8cfde54c792f783314ab04d9fe4eaba47aaa>`_
- Fix trailing slash in the link in the elections processor and make it valid python `3c731ac51 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/3c731ac514d80d66de5fab67eab90b65b4cbc21b>`_
- Fix the usernames method `540b48954 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/540b4895441297c52b450fe3b3d2bad8712cc38d>`_
- pep8 fixes to the fedocal tests `831958858 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/831958858577d313258e333ce709136d397f9dfb>`_
- Fix the name, messages from the elections are of type fedora_elections `1e6d8c61e <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/1e6d8c61e2c79dff8fd55310e30491df1a470115>`_
- Fix the topic for editing or deleting candidates (and not elections) `dd27ca13e <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/dd27ca13efdb07e7dc902ec238f418cf4499adf1>`_
- The messages are only broadcasting one candidate at a time, no list `f59ed4b3a <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/f59ed4b3a943f4f57398c979e6f3b0bd8e84cfcb>`_
- Add unit-tests for the fedora_elections messages `77ebbff64 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/77ebbff649639c3703446494787f5d2b61d8a57a>`_
- Link the unit-tests for fedora_elections into the main test suite `03887eaa1 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/03887eaa143a019500d2ec9f252cfaf090c650c6>`_
- pep8 fixes on the trac tests `90a3d0933 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/90a3d0933c65015eb09a1714e5c656851eea0055>`_
- pep8 fixes on the summershum tests `2080bdca7 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/2080bdca77d44c108e05491a0bc0b3e3c939611f>`_
- pep8 fixes on the mailman3 tests `0b0f1a69b <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/0b0f1a69bf756b2a801767462af8e838386d93d1>`_
- pep8 fixes on the pkgdb tests `7e914cc87 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/7e914cc87a1d3d71734fdb6303b8bdb6571fb8da>`_
- pep8 fixes on the jenkins tests `05d3ddb25 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/05d3ddb2569d713532ed6a0adc2850a996d53d64>`_
- pep8 fixes on the github tests `a4e11b75a <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/a4e11b75a9a32b7abdf3db39070cecd50f3d2459>`_
- pep8 fixes on the askbot tests `723536331 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/7235363314355638a55c5c3e80313da08bc4e939>`_
- pep8 fixes on the ansible tests `29d4de8e7 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/29d4de8e76c5161b37e8bcf2a8f8f19dca22cafc>`_
- pep8 fixes on the pkgdb meta file `9ddcabbee <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/9ddcabbee4dd2b8af6e4300ad0d4ffed7f384df6>`_
- pep8 fixes on the jenkins meta file `5da6fcd04 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/5da6fcd04c68ad387949f3b7c411f1f38bf00863>`_
- pep8 fixes on the fasshim meta file `c090e4281 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/c090e42812cb82b379c4f4f1b729337163ed5d30>`_
- pep8 fixes on the cnucnuweb meta file `cbcd846f9 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/cbcd846f9048088ed35966dc475e822117ed056b>`_
- pep8 fixes on fedmsg.d/base.py `8232320fa <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/8232320fa1bb1583919823337c8f143866aecfe3>`_
- pep8 fixes on the setup.py file `363058da5 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/363058da5b6db9e0a001a75afa2c7725536889a8>`_
- Merge pull request #77 from fedora-infra/elections `7dd0715b4 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/7dd0715b4f1b35363223788689fa6384b982f667>`_
- Merge pull request #78 from fedora-infra/pep8 `b787911bf <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/b787911bf1cc638a660558b7d592b116744cfd67>`_
- Be careful with copr messages here. `5a6fbd0c4 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/5a6fbd0c406db5f935b19f927933332bf3ccee43>`_
- Use the new copr frontend url. `7c0830cfc <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/7c0830cfc9cd235b0e3be872423c30d5da80f235>`_
- Merge pull request #80 from fedora-infra/feature/take-care-with-copr `cf64f50d1 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/cf64f50d1c352b25ff0ac81f9f6c11e619abee01>`_
- Retire this one bodhi masher message. `043dbad9b <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/043dbad9b9f63b7f41cb12591490ff52224dfcba>`_
- Merge pull request #82 from fedora-infra/feature/retire-masher-message `e395dd421 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/e395dd42192265c0ccee92d6d188f5218b0ca5e3>`_
- Give fedmsg.meta its own doc infrastructure. `0b866c2c3 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/0b866c2c364e546cfd26e7fd2ec8460e3da27258>`_
- Merge pull request #83 from fedora-infra/feature/doc-split `7181bf8d6 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/7181bf8d6b089033eb6dd5d830cbc860b2117b6f>`_
- Adjust the URL to point to the right pkgdb2 page `c4249c393 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/c4249c3933e22f3f109baa9ed78242f7052cfaf0>`_
- Adjust the unit-tests to use the correct URL for pkgdb2 `91b941e4f <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/91b941e4f89e3b925e3772713d0ba1bfbe08ffc1>`_
- small pep8 fix to make pep8bot happy `e9f5d285a <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/e9f5d285a4eb5dfdf75493df65d9587fc4ccb361>`_
- Merge pull request #84 from fedora-infra/pkgdb2_url `5136e3434 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/5136e343476edc3271ca1ab3cd70ec10bf512aa8>`_
- Copr icon. `a1d296828 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/a1d296828022853ee88e6b9a45fc587d858df68c>`_
- Test that icon, too. `27d0552cd <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/27d0552cdeec1162a81690c32dfa2d080a94c1e7>`_
- Icons for meetbot. `9e733ea93 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/9e733ea93d33238a01cd0f469db5ea0dcd23c76f>`_
- Just to be sure. `e0c087f96 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/e0c087f961caefa974ac7cbad679db62fbf9eb29>`_
- More being sure. `44ab1f881 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/44ab1f88149818bea1e75e2a63bdfaeb239b8644>`_
- Ignore the topics .rst doc.  It is auto generated. `b884d5b6f <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/b884d5b6fd5caba540f45d8dcbfda7084c656d7c>`_
- Update koji examples. `dc1611712 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/dc1611712652219aa5aa5b5d09ce75c498a004c7>`_
- Merge pull request #87 from fedora-infra/feature/update-koji-examples `5822fe792 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/5822fe792c4bfef104067d9a89f742482083c2d5>`_
- Merge pull request #86 from fedora-infra/feature/meetbot-icon `672917fe3 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/672917fe32cb8ad32de5355bc152fa39c5282dc8>`_
- Merge pull request #85 from fedora-infra/feature/copr-icon `bba920ec1 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/bba920ec1ac21e82551186dad1ff9e3a87f9c77e>`_
- Fix meetbot topic changes. `903861a4e <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/903861a4eb9838c35dec31fe1681f09bb8f33aee>`_
- 0.2.12 `02f169e06 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/02f169e06e923cc74316827ded14b9ea7544a951>`_
- Processor and tests for FMN messages. `f8aa9b47f <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/f8aa9b47f9c678599a846d0c2c558f7ba31edcd0>`_
- Merge pull request #88 from fedora-infra/feature/fmn `9d693257b <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/9d693257b58d9696ddda3795a1c307a9d88072b5>`_
- Actually add the code for this. `9bce4b293 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/9bce4b293e6ec07a7416c63f62f88a3ed3cbb0bd>`_
- Merge branch 'feature/fmn' into develop `2521946b3 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/2521946b36cc08ed6d42de3ca79e50d610597d96>`_
- Pkgdb: Avoid redirects to URL with trailing slash `de99f5914 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/de99f59142fca006260ea74b2ee0a8ef2c06b243>`_
- Merge pull request #92 from tyll/avoid-redirects `4d9387fc8 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/4d9387fc85f1e984769e5b7426bc31f393f31f98>`_
- Pkgdb: Make package retirement messages explicit `42d30bda3 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/42d30bda3ef9464b0a7917f5b19f927cce4a41a3>`_
- Merge pull request #91 from tyll/develop `80fc3d9ea <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/80fc3d9eaeb067fe3a4f098b65e3225497bcb784>`_
- 0.2.13 `4a838f948 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/4a838f9480912806872e902f941a6a28d89acab3>`_
- Fix .rst syntax. `ff4853a39 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/ff4853a390171e944655b9d564f9ee4ebe41a763>`_
- compose: remove unused import `93ff47576 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/93ff47576d37fc49497f7eac43272c2a76d1a503>`_
- Use https where currently possible `62a9c6cbf <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/62a9c6cbf4ab61cf6e489f9c33c798e4721a5e36>`_
- Allow mentions in bodhi comments.  /cc @codeblock. `ffe34c428 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/ffe34c428ba5c6483c0eb76d428c495f0250645d>`_
- Merge pull request #94 from fedora-infra/feature/mentions `56a3b4270 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/56a3b42705cec5e1c821c93096039c1a99adceb7>`_
- Initial go at a fedmsg meta config for the new fedimg service. `b47fa4205 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/b47fa4205c2d3bc616696cac39a20c2a4dc14624>`_
- Typofix `f4a928d1e <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/f4a928d1e6b8ccae65345d964f967860f9ee18a5>`_
- Add marked up text and tests for bodhi messages. `bc68050a5 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/bc68050a55584ae13763c9375f2b2ee239cb307c>`_
- Merge pull request #98 from fedora-infra/feature/marked-up-bodhi `f8b840b96 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/f8b840b966d89e709f9ba18731d42ff1917a75fd>`_
- Merge pull request #93 from tyll/https `7e364d43f <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/7e364d43f2caeb360dfa2cf65613efe33a597e08>`_
- Allow the FAS url to be configurable. `dfab75e91 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/dfab75e91edc6832e79dfc1f4b8e097f95d66dff>`_
- Use a nuancier icon. `e309fb85d <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/e309fb85d03d540d9d9156f4a9dd107db68323ba>`_
- Cook our own avatar links. `84ba908dd <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/84ba908dd4173e35e93b5094abb0160a8f61a5fb>`_
- Use libravatar. `07a3e0a20 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/07a3e0a20c24c3bb7e12d9fc95864074a53fef0b>`_
- Update the tests to expect libravatar. `de7a296da <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/de7a296da74c612712bb8641c7093584dd08af1d>`_
- Merge pull request #100 from fedora-infra/feature/nuancier-icon `880a12c82 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/880a12c828dee94c30f103a20beb972690241f04>`_
- Show icons in docs. `0a02161f4 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/0a02161f4e33e4e7fd1c9d91d5ca1a68eec73528>`_
- Merge pull request #102 from fedora-infra/feature/show-icons-in-docs `25c003e03 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/25c003e030ffe731c9337bf6cb7b512cb06d05ca>`_
- Merge pull request #99 from fedora-infra/feature/configurable-fas-url `403b005f0 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/403b005f019eadaa41214dd64d2b0e528bc4f9c0>`_
- Merge pull request #101 from fedora-infra/feature/libravatar `78d057b2e <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/78d057b2e949588662cbb864a2396eca59ffaf65>`_
- Remove some stuff we don't need. `9fb656b2a <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/9fb656b2af6646355809ef743a06cafb57821fef>`_
- Make successful status 'completed' instead of 'succeeded' `f75a7711a <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/f75a7711ac6f60bcefd84ebd5c7e9318e64744b5>`_
- Tweaks as per @threebean's comments. `40fd23e49 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/40fd23e49903511bf5a3d85209760a84238bee95>`_
- Author --> Authors to match other files. `e6b19ba0b <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/e6b19ba0b3f01fe6f2217bd61f75052efd5e46c4>`_
- Start writing a test for Fedimg fedmsgs. `bb8590a21 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/bb8590a21cec481d262f3ffb71a90f4f22440799>`_
- Looks like this fedimg test passes `5d6e69df5 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/5d6e69df50b03f0ab959f731b4b55bb9d7826c8a>`_
- Typofix `d282bff37 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/d282bff37a3283e3957da7de4096864880c7700a>`_
- PEP 8 `675bfcc7f <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/675bfcc7fdb7ddb034e709f7944610a32a9317b6>`_
- These things aren't sets. `f69d1742f <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/f69d1742fced458564f66343e735b4f6c38a0ded>`_
- Crucial - declare the FedimgProcessor. `7bd2ce597 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/7bd2ce59746ed4b38e2150f8cbd9bd4d0d42c703>`_
- Run fedimg tests as part of the big suite. `7f3bebc6b <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/7f3bebc6b41386dc8832eeff5b9a555eab364804>`_
- Handle github.status messages. `7b3bad3bb <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/7b3bad3bbfcb86ed9c589ac0e6610585d642cee2>`_
- Handle github.delete messages. `4222b6491 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/4222b649189a20efc3fc7efb6131dc90ff768ad5>`_
- Handle pull request review comments. `72ada211c <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/72ada211c98aa4667be0a226013361822a14f051>`_
- Reorganize the way msg2objects works for github so that it makes more sense. `b118d4e1b <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/b118d4e1b8f8f291b283ddefc946785b5ae4bede>`_
- Fix key name. `b742848e2 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/b742848e2f44f49eebeca755a4dbe3c2e15c3627>`_
- py2.6 doesn't support str.format() without indexes `4d112edca <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/4d112edcacfdf203ff9889f67d02c1b5b090756e>`_
- This should be the image name, not the URL. `ca6b47006 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/ca6b47006b471c952e90a32ced32dc1c5c2dc731>`_
- Support commit comments. `a91f1a75b <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/a91f1a75b4648d394268b5ecb42e92d0d9c50b00>`_
- Merge pull request #103 from fedora-infra/feature/fedimg-meta `90379f404 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/90379f404f95757e8b05f04e1b57ce504cfa42f4>`_
- Merge pull request #104 from fedora-infra/feature/more-github-stuff `329d97cd8 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/329d97cd85a08fe3d4bd917bda2e190efcd1827b>`_
- 0.2.14 `9b4e0e58a <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/9b4e0e58aede0a0da96c44503d0c4d2318d85eb1>`_
- Add secondary icons for some cvsadmin and releng stuff. `fc4d4759e <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/fc4d4759e064e22279f7b8d1ddc66ac832dac8a5>`_
- Merge pull request #105 from fedora-infra/feature/some-secondary-icons `4ca3d5e97 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/4ca3d5e9776accc0c70182b0b55197b8e3e46ba8>`_
- Sometimes, these can exist, but be None. `fa432bff7 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/fa432bff7e9b6712d5dbfd1e93af5f9ebaf06959>`_
- Use short hashes here. `8598913ae <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/8598913aec0cfa58563aaa58bbfd5bd00d821cd7>`_
- Merge pull request #106 from fedora-infra/feature/short-hash `f50709d99 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/f50709d99a863412386e2bed523c0681b573a2a2>`_
- Kerneltest message handler and tests. `8d1b08b83 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/8d1b08b837778aa162321157ca53a05df12de7c8>`_
- Merge pull request #108 from fedora-infra/feature/kerneltest `4be76c72d <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/4be76c72df16430cd6570aa700d7359dc6af7f3b>`_
- Remove trailing slash that are no longer is use with elections2 `6201fe737 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/6201fe7371288c7ecdaf9904d9708cece790d4c9>`_
- Adjust the unit-tests to remove the trailing slash `7a38c4c62 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/7a38c4c62586e93495e4534601070729b5c7736a>`_
- Merge pull request #113 from fedora-infra/fix_elections `87f91f142 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/87f91f142d7237a482a99c3255c1de49b0e14a96>`_
- Indicate success of copr builds. `47e4e4e0b <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/47e4e4e0b24a74de7b08d9724ac3eca5968924af>`_
- Handle case where this can be None. `6415d246c <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/6415d246c189635bb93633a30a77ca709420b12b>`_
- Fix bug in subtitle for pkgdb.branch.start `015d6efd1 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/015d6efd11ec67a51babaa98875d565e33904d72>`_
- Merge pull request #114 from fedora-infra/feature/fixups `7abaad2a2 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/7abaad2a2b371ab9da761524806ca17747074c02>`_
- 0.2.15 `cac2991d1 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/cac2991d1acb6c81cb2d2baf237c99b30dc5725e>`_
- Handle an edge case with github messages. `895dab10a <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/895dab10ab8d1881c75cb53d52cab30afb22603e>`_
- Merge pull request #115 from fedora-infra/feature/github-edge-case `a74c6e9cf <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/a74c6e9cfca33b2e2b084eb6ecdaa9bff8adcd35>`_
- Add meta code for fedimg.image.test topic `bb65093d6 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/bb65093d607cd4be6174412fae0b664cafbf0ac0>`_
- Merge pull request #116 from fedora-infra/feature/fedimg-test-messages `89cf61d20 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/89cf61d20a71dea0cc53fc69dc5645f9a228fa13>`_
- Include the chroot in the description of finished builds on copr `3dcb851e9 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/3dcb851e931a6701da069f43a31509d64097fc9c>`_
- Adjust the unit-test for copr messages to reflect the addition of the chroot on the finished build message `5ba200ff9 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/5ba200ff9b6bfb8e03763f7367294f79febbcf91>`_
- Merge pull request #118 from fedora-infra/endbuild_chroot `f513436a2 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/f513436a2bee9b2be883ece084c8693182b45907>`_
- Hide old pkgdb1 retirement messages from the docs. `7d9c23a1b <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/7d9c23a1ba3066cc0d2aae36e7b172dc8ce68441>`_
- Merge pull request #119 from fedora-infra/feature/legacy-retirement `fc257d074 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/fc257d0743793d04e28392ea17b613b0f0298533>`_
- Add support for github.watch messages. `74fd4f45b <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/74fd4f45bd6ecbb06a6f8510464367c94a4d8649>`_
- Handle both starts and stops. `9fbfe371f <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/9fbfe371feab18a85398f535e1956a647a406b98>`_
- Merge pull request #120 from fedora-infra/feature/github-watch `b65ad6ab2 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/b65ad6ab275bba61f4177980d531d0c70c69a503>`_
- Added Class and Test `ccfea0d56 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/ccfea0d56453babd29e490bfbdad5936eaf6e2a0>`_
- added class for fedora college `c140ff8ba <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/c140ff8bac230a57d3ac5613dd5d5cef633070b4>`_
- Minor changes in file description `12329eeda <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/12329eeda662f78eabd2a64fdf6b5bad5c19f038>`_
- Merge pull request #121 from hammadhaleem/develop `ab6154c59 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/ab6154c59eeba5f3d2bff22434b513253a18019b>`_
- The topic packag.update.status is not package.update `9e852081d <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/9e852081d27a47f2569d1d0a2faa831c6ed9d13c>`_
- Handle the pkgdb.package.update messages `24022da8b <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/24022da8b5664e5ab0755ebd943674548fc75207>`_
- Adjust the unit-test name for PackageUpdateStatus `222f977bf <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/222f977bf16adeda8de14ce2b330fc2533ca615f>`_
- Add unit-tests for the package.update topic `a681f1b1f <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/a681f1b1fea2d5d581b63929c35de63f75b1620f>`_
- Merge pull request #122 from fedora-infra/fix_pkgdb `698c279f9 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/698c279f9d9f601540cdd8ea335849d12040fd70>`_
- Get the tests passing again. `b241d815e <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/b241d815ed951ad49abca8e4144d683dbad96c40>`_
- 0.2.16 `1a8d00b18 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/1a8d00b18ce287e6b1a685611df17630fbaa7300>`_
- add several jenkins statuses `2b7f67a68 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/2b7f67a689413978a2b431382f9c4b8582850a2c>`_
- Merge pull request #124 from fedora-infra/jenkins-try-again `de9a741a4 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/de9a741a4530870eb9377a8ac9891a69992c90fc>`_
- 0.2.17 `edd3fe59e <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/edd3fe59ec84ab9c38248a71aa86e5ceeca1b247>`_
- Fix tests. `3643db6e1 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/3643db6e189965561aea38b6ff286e87fcf4faf7>`_
- 0.2.18 `b46069572 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/b46069572f66b9c9ab8d2661b4fa2d38095e07ab>`_
- Comment out time-sensitive test. `1a8fe7b89 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/1a8fe7b89f6f4f7193740f6bb146f67fb2835c73>`_
- Debug missing topic. `b51dcb708 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/b51dcb7087484c8f6256c76beb9c80cb861f6a4e>`_
- Add missing topic. `6a1bd32d2 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/6a1bd32d2a4d8b228de4d1d910820561e2b1ca60>`_
- Merge pull request #126 from fedora-infra/feature/more-jenkins-fixes `22175af34 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/22175af34a7bd05a43356022c86fbb290ee5424a>`_
- Handle pkgdb.package.delete. `eb73eaf92 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/eb73eaf92d1b43dc1eef57245310fa98b09cfb2a>`_
- pkgdb.package.branch.delete and pkgdb.acl.delete `0df5e488d <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/0df5e488d0624548584c19e7f1d48ab17ae7d125>`_
- Merge pull request #128 from fedora-infra/feature/those-other-pkgdb-messages `c9ab3f9ed <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/c9ab3f9ed679144cf75519ced04d469e06d08d66>`_
- Handle the new pkgdb fedmsg messages `7fa96b37c <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/7fa96b37c8cc2c02e94a3d003cfa19e8f6f3e550>`_
- Adjust the unit-tests to test for these new messages `4dbf902f9 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/4dbf902f9977f8be3b94a11a2031c23a44990b93>`_
- Merge pull request #129 from fedora-infra/new_pkgdb `2b1a61c55 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/2b1a61c5557f55efea04db46efd68763ba6a39e0>`_
- There are case where the `action` dict is not there and case where it is `f9b10d582 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/f9b10d582224e2ef903ba25f6b5aabb1e649d514>`_
- Merge pull request #130 from fedora-infra/new_pkgdb `282e8fff2 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/282e8fff213a24bf57b18998f45f863994382dd3>`_
- Handle pkgdb critpath change messages. `5cb94cdb6 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/5cb94cdb6d80453404004edb28056bbb70093e74>`_
- Merge pull request #131 from fedora-infra/feature/critpath-messages `e273a0c1d <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/e273a0c1d3185b017918c74db1dea0ee03c1f590>`_

0.2.19
------

- Comment out time-sensitive test. `1a8fe7b89 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/1a8fe7b89f6f4f7193740f6bb146f67fb2835c73>`_
- Debug missing topic. `b51dcb708 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/b51dcb7087484c8f6256c76beb9c80cb861f6a4e>`_
- Add missing topic. `6a1bd32d2 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/6a1bd32d2a4d8b228de4d1d910820561e2b1ca60>`_
- Merge pull request #126 from fedora-infra/feature/more-jenkins-fixes `22175af34 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/22175af34a7bd05a43356022c86fbb290ee5424a>`_
- Handle pkgdb.package.delete. `eb73eaf92 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/eb73eaf92d1b43dc1eef57245310fa98b09cfb2a>`_
- pkgdb.package.branch.delete and pkgdb.acl.delete `0df5e488d <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/0df5e488d0624548584c19e7f1d48ab17ae7d125>`_
- Merge pull request #128 from fedora-infra/feature/those-other-pkgdb-messages `c9ab3f9ed <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/c9ab3f9ed679144cf75519ced04d469e06d08d66>`_
- Handle the new pkgdb fedmsg messages `7fa96b37c <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/7fa96b37c8cc2c02e94a3d003cfa19e8f6f3e550>`_
- Adjust the unit-tests to test for these new messages `4dbf902f9 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/4dbf902f9977f8be3b94a11a2031c23a44990b93>`_
- Merge pull request #129 from fedora-infra/new_pkgdb `2b1a61c55 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/2b1a61c5557f55efea04db46efd68763ba6a39e0>`_
- There are case where the `action` dict is not there and case where it is `f9b10d582 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/f9b10d582224e2ef903ba25f6b5aabb1e649d514>`_
- Merge pull request #130 from fedora-infra/new_pkgdb `282e8fff2 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/282e8fff213a24bf57b18998f45f863994382dd3>`_
- Handle pkgdb critpath change messages. `5cb94cdb6 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/5cb94cdb6d80453404004edb28056bbb70093e74>`_
- Merge pull request #131 from fedora-infra/feature/critpath-messages `e273a0c1d <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/e273a0c1d3185b017918c74db1dea0ee03c1f590>`_

0.2.18
------

- Fix tests. `3643db6e1 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/3643db6e189965561aea38b6ff286e87fcf4faf7>`_

0.2.17
------

- add several jenkins statuses `2b7f67a68 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/2b7f67a689413978a2b431382f9c4b8582850a2c>`_
- Merge pull request #124 from fedora-infra/jenkins-try-again `de9a741a4 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/de9a741a4530870eb9377a8ac9891a69992c90fc>`_

0.2.16
------

- Handle an edge case with github messages. `895dab10a <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/895dab10ab8d1881c75cb53d52cab30afb22603e>`_
- Merge pull request #115 from fedora-infra/feature/github-edge-case `a74c6e9cf <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/a74c6e9cfca33b2e2b084eb6ecdaa9bff8adcd35>`_
- Add meta code for fedimg.image.test topic `bb65093d6 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/bb65093d607cd4be6174412fae0b664cafbf0ac0>`_
- Merge pull request #116 from fedora-infra/feature/fedimg-test-messages `89cf61d20 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/89cf61d20a71dea0cc53fc69dc5645f9a228fa13>`_
- Include the chroot in the description of finished builds on copr `3dcb851e9 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/3dcb851e931a6701da069f43a31509d64097fc9c>`_
- Adjust the unit-test for copr messages to reflect the addition of the chroot on the finished build message `5ba200ff9 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/5ba200ff9b6bfb8e03763f7367294f79febbcf91>`_
- Merge pull request #118 from fedora-infra/endbuild_chroot `f513436a2 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/f513436a2bee9b2be883ece084c8693182b45907>`_
- Hide old pkgdb1 retirement messages from the docs. `7d9c23a1b <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/7d9c23a1ba3066cc0d2aae36e7b172dc8ce68441>`_
- Merge pull request #119 from fedora-infra/feature/legacy-retirement `fc257d074 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/fc257d0743793d04e28392ea17b613b0f0298533>`_
- Add support for github.watch messages. `74fd4f45b <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/74fd4f45bd6ecbb06a6f8510464367c94a4d8649>`_
- Handle both starts and stops. `9fbfe371f <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/9fbfe371feab18a85398f535e1956a647a406b98>`_
- Merge pull request #120 from fedora-infra/feature/github-watch `b65ad6ab2 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/b65ad6ab275bba61f4177980d531d0c70c69a503>`_
- Added Class and Test `ccfea0d56 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/ccfea0d56453babd29e490bfbdad5936eaf6e2a0>`_
- added class for fedora college `c140ff8ba <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/c140ff8bac230a57d3ac5613dd5d5cef633070b4>`_
- Minor changes in file description `12329eeda <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/12329eeda662f78eabd2a64fdf6b5bad5c19f038>`_
- Merge pull request #121 from hammadhaleem/develop `ab6154c59 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/ab6154c59eeba5f3d2bff22434b513253a18019b>`_
- The topic packag.update.status is not package.update `9e852081d <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/9e852081d27a47f2569d1d0a2faa831c6ed9d13c>`_
- Handle the pkgdb.package.update messages `24022da8b <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/24022da8b5664e5ab0755ebd943674548fc75207>`_
- Adjust the unit-test name for PackageUpdateStatus `222f977bf <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/222f977bf16adeda8de14ce2b330fc2533ca615f>`_
- Add unit-tests for the package.update topic `a681f1b1f <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/a681f1b1fea2d5d581b63929c35de63f75b1620f>`_
- Merge pull request #122 from fedora-infra/fix_pkgdb `698c279f9 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/698c279f9d9f601540cdd8ea335849d12040fd70>`_
- Get the tests passing again. `b241d815e <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/b241d815ed951ad49abca8e4144d683dbad96c40>`_

0.2.15
------

- Add secondary icons for some cvsadmin and releng stuff. `fc4d4759e <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/fc4d4759e064e22279f7b8d1ddc66ac832dac8a5>`_
- Merge pull request #105 from fedora-infra/feature/some-secondary-icons `4ca3d5e97 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/4ca3d5e9776accc0c70182b0b55197b8e3e46ba8>`_
- Sometimes, these can exist, but be None. `fa432bff7 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/fa432bff7e9b6712d5dbfd1e93af5f9ebaf06959>`_
- Use short hashes here. `8598913ae <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/8598913aec0cfa58563aaa58bbfd5bd00d821cd7>`_
- Merge pull request #106 from fedora-infra/feature/short-hash `f50709d99 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/f50709d99a863412386e2bed523c0681b573a2a2>`_
- Kerneltest message handler and tests. `8d1b08b83 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/8d1b08b837778aa162321157ca53a05df12de7c8>`_
- Merge pull request #108 from fedora-infra/feature/kerneltest `4be76c72d <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/4be76c72df16430cd6570aa700d7359dc6af7f3b>`_
- Remove trailing slash that are no longer is use with elections2 `6201fe737 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/6201fe7371288c7ecdaf9904d9708cece790d4c9>`_
- Adjust the unit-tests to remove the trailing slash `7a38c4c62 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/7a38c4c62586e93495e4534601070729b5c7736a>`_
- Merge pull request #113 from fedora-infra/fix_elections `87f91f142 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/87f91f142d7237a482a99c3255c1de49b0e14a96>`_
- Indicate success of copr builds. `47e4e4e0b <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/47e4e4e0b24a74de7b08d9724ac3eca5968924af>`_
- Handle case where this can be None. `6415d246c <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/6415d246c189635bb93633a30a77ca709420b12b>`_
- Fix bug in subtitle for pkgdb.branch.start `015d6efd1 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/015d6efd11ec67a51babaa98875d565e33904d72>`_
- Merge pull request #114 from fedora-infra/feature/fixups `7abaad2a2 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/7abaad2a2b371ab9da761524806ca17747074c02>`_

0.2.14
------

- Fix .rst syntax. `ff4853a39 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/ff4853a390171e944655b9d564f9ee4ebe41a763>`_
- compose: remove unused import `93ff47576 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/93ff47576d37fc49497f7eac43272c2a76d1a503>`_
- Use https where currently possible `62a9c6cbf <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/62a9c6cbf4ab61cf6e489f9c33c798e4721a5e36>`_
- Allow mentions in bodhi comments.  /cc @codeblock. `ffe34c428 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/ffe34c428ba5c6483c0eb76d428c495f0250645d>`_
- Merge pull request #94 from fedora-infra/feature/mentions `56a3b4270 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/56a3b42705cec5e1c821c93096039c1a99adceb7>`_
- Initial go at a fedmsg meta config for the new fedimg service. `b47fa4205 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/b47fa4205c2d3bc616696cac39a20c2a4dc14624>`_
- Typofix `f4a928d1e <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/f4a928d1e6b8ccae65345d964f967860f9ee18a5>`_
- Add marked up text and tests for bodhi messages. `bc68050a5 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/bc68050a55584ae13763c9375f2b2ee239cb307c>`_
- Merge pull request #98 from fedora-infra/feature/marked-up-bodhi `f8b840b96 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/f8b840b966d89e709f9ba18731d42ff1917a75fd>`_
- Merge pull request #93 from tyll/https `7e364d43f <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/7e364d43f2caeb360dfa2cf65613efe33a597e08>`_
- Allow the FAS url to be configurable. `dfab75e91 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/dfab75e91edc6832e79dfc1f4b8e097f95d66dff>`_
- Use a nuancier icon. `e309fb85d <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/e309fb85d03d540d9d9156f4a9dd107db68323ba>`_
- Cook our own avatar links. `84ba908dd <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/84ba908dd4173e35e93b5094abb0160a8f61a5fb>`_
- Use libravatar. `07a3e0a20 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/07a3e0a20c24c3bb7e12d9fc95864074a53fef0b>`_
- Update the tests to expect libravatar. `de7a296da <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/de7a296da74c612712bb8641c7093584dd08af1d>`_
- Merge pull request #100 from fedora-infra/feature/nuancier-icon `880a12c82 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/880a12c828dee94c30f103a20beb972690241f04>`_
- Show icons in docs. `0a02161f4 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/0a02161f4e33e4e7fd1c9d91d5ca1a68eec73528>`_
- Merge pull request #102 from fedora-infra/feature/show-icons-in-docs `25c003e03 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/25c003e030ffe731c9337bf6cb7b512cb06d05ca>`_
- Merge pull request #99 from fedora-infra/feature/configurable-fas-url `403b005f0 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/403b005f019eadaa41214dd64d2b0e528bc4f9c0>`_
- Merge pull request #101 from fedora-infra/feature/libravatar `78d057b2e <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/78d057b2e949588662cbb864a2396eca59ffaf65>`_
- Remove some stuff we don't need. `9fb656b2a <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/9fb656b2af6646355809ef743a06cafb57821fef>`_
- Make successful status 'completed' instead of 'succeeded' `f75a7711a <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/f75a7711ac6f60bcefd84ebd5c7e9318e64744b5>`_
- Tweaks as per @threebean's comments. `40fd23e49 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/40fd23e49903511bf5a3d85209760a84238bee95>`_
- Author --> Authors to match other files. `e6b19ba0b <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/e6b19ba0b3f01fe6f2217bd61f75052efd5e46c4>`_
- Start writing a test for Fedimg fedmsgs. `bb8590a21 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/bb8590a21cec481d262f3ffb71a90f4f22440799>`_
- Looks like this fedimg test passes `5d6e69df5 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/5d6e69df50b03f0ab959f731b4b55bb9d7826c8a>`_
- Typofix `d282bff37 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/d282bff37a3283e3957da7de4096864880c7700a>`_
- PEP 8 `675bfcc7f <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/675bfcc7fdb7ddb034e709f7944610a32a9317b6>`_
- These things aren't sets. `f69d1742f <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/f69d1742fced458564f66343e735b4f6c38a0ded>`_
- Crucial - declare the FedimgProcessor. `7bd2ce597 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/7bd2ce59746ed4b38e2150f8cbd9bd4d0d42c703>`_
- Run fedimg tests as part of the big suite. `7f3bebc6b <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/7f3bebc6b41386dc8832eeff5b9a555eab364804>`_
- Handle github.status messages. `7b3bad3bb <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/7b3bad3bbfcb86ed9c589ac0e6610585d642cee2>`_
- Handle github.delete messages. `4222b6491 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/4222b649189a20efc3fc7efb6131dc90ff768ad5>`_
- Handle pull request review comments. `72ada211c <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/72ada211c98aa4667be0a226013361822a14f051>`_
- Reorganize the way msg2objects works for github so that it makes more sense. `b118d4e1b <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/b118d4e1b8f8f291b283ddefc946785b5ae4bede>`_
- Fix key name. `b742848e2 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/b742848e2f44f49eebeca755a4dbe3c2e15c3627>`_
- py2.6 doesn't support str.format() without indexes `4d112edca <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/4d112edcacfdf203ff9889f67d02c1b5b090756e>`_
- This should be the image name, not the URL. `ca6b47006 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/ca6b47006b471c952e90a32ced32dc1c5c2dc731>`_
- Support commit comments. `a91f1a75b <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/a91f1a75b4648d394268b5ecb42e92d0d9c50b00>`_
- Merge pull request #103 from fedora-infra/feature/fedimg-meta `90379f404 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/90379f404f95757e8b05f04e1b57ce504cfa42f4>`_
- Merge pull request #104 from fedora-infra/feature/more-github-stuff `329d97cd8 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/329d97cd85a08fe3d4bd917bda2e190efcd1827b>`_

0.2.13
------

- Processor and tests for FMN messages. `f8aa9b47f <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/f8aa9b47f9c678599a846d0c2c558f7ba31edcd0>`_
- Merge pull request #88 from fedora-infra/feature/fmn `9d693257b <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/9d693257b58d9696ddda3795a1c307a9d88072b5>`_
- Actually add the code for this. `9bce4b293 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/9bce4b293e6ec07a7416c63f62f88a3ed3cbb0bd>`_
- Merge branch 'feature/fmn' into develop `2521946b3 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/2521946b36cc08ed6d42de3ca79e50d610597d96>`_
- Pkgdb: Avoid redirects to URL with trailing slash `de99f5914 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/de99f59142fca006260ea74b2ee0a8ef2c06b243>`_
- Merge pull request #92 from tyll/avoid-redirects `4d9387fc8 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/4d9387fc85f1e984769e5b7426bc31f393f31f98>`_
- Pkgdb: Make package retirement messages explicit `42d30bda3 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/42d30bda3ef9464b0a7917f5b19f927cce4a41a3>`_
- Merge pull request #91 from tyll/develop `80fc3d9ea <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/80fc3d9eaeb067fe3a4f098b65e3225497bcb784>`_

0.2.12
------

- Need to pass through the config here... `2ff1888a6 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/2ff1888a60fb9051d6e9a0575193ed4825a2f98b>`_
- BZ processor and a test. `3e7ce519f <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/3e7ce519fad93ee5f0ffedadac4881aa6bff62a3>`_
- Handle messages for "new bugs" `410baa648 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/410baa648361795ded8c915b7b96a68a944b8b76>`_
- Correct module doc. `e91840446 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/e918404463f885f9de89ccfae685419325c290bf>`_
- Merge pull request #72 from fedora-infra/feature/bugzilla `b7b94bcf2 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/b7b94bcf2e463413740d2535cc0f3e3fd4e5a577>`_
- Use https for copr-be. `fb4e6249f <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/fb4e6249f1cc560d089badff9166fa4b158d0dda>`_
- https for wiki links, please. `b26b8ca11 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/b26b8ca11e3554f33335cccc137ea5a3d4704c2a>`_
- https for meetbot, please. `f195772d8 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/f195772d89f333210e36a184c496d5f3ffae37bc>`_
- Merge pull request #73 from fedora-infra/feature/https `162d231a6 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/162d231a6bcc370f0503879a3558c8f92bfdb0ba>`_
- Clarify user role at endmeeting.  Fixes #29. `e74642892 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/e7464289233e0993c1d1366ef14a240ea80ead35>`_
- Merge pull request #74 from fedora-infra/feature/user-at-endmeeting `a8b5cff01 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/a8b5cff014d11de6a22cd49245180630739bddc5>`_
- Remove "slave" field from jenkins `fbf3fc841 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/fbf3fc8417dab72d2981545ffb48495a8cf3be9c>`_
- Merge pull request #75 from fedora-infra/jenkins-take2 `ac853fcee <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/ac853fcee2ace23cf08253dd37f9c4fd02016d6a>`_
- Test tagger rank change messages.  Fixes #14. `e0541cde8 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/e0541cde81c6e250e7349f31a3414501202f0a88>`_
- Merge pull request #76 from fedora-infra/feature/test-tagger-rank `413194c36 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/413194c369704c5ca666a821d12cdf4a70a1801c>`_
- First work on the ElectionsProcessor for fedora-elections `ae75f73e1 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/ae75f73e149b19274fa656790ecef3ad733e6123>`_
- Update the elections Processor now that the messages contain an agent `3b4990e72 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/3b4990e72e465bedb3904b8f7e7022fd02780296>`_
- Adjust the __link__ now that the elections is on apps `f602cfbcf <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/f602cfbcf155ba689c279c60c03412dab288fddc>`_
- Manage messages regarding elections' candidate (new, edit, delete) `dc00a61a8 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/dc00a61a83f6e2bd045c780ea63ea0f8f4a74640>`_
- Adjust the setup.py file to include the elections processor `3c6e15edc <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/3c6e15edc6eb6a9cd03153b8c5913706744223b7>`_
- Import the ElectionsProcessor from the right file `843f8cfde <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/843f8cfde54c792f783314ab04d9fe4eaba47aaa>`_
- Fix trailing slash in the link in the elections processor and make it valid python `3c731ac51 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/3c731ac514d80d66de5fab67eab90b65b4cbc21b>`_
- Fix the usernames method `540b48954 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/540b4895441297c52b450fe3b3d2bad8712cc38d>`_
- pep8 fixes to the fedocal tests `831958858 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/831958858577d313258e333ce709136d397f9dfb>`_
- Fix the name, messages from the elections are of type fedora_elections `1e6d8c61e <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/1e6d8c61e2c79dff8fd55310e30491df1a470115>`_
- Fix the topic for editing or deleting candidates (and not elections) `dd27ca13e <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/dd27ca13efdb07e7dc902ec238f418cf4499adf1>`_
- The messages are only broadcasting one candidate at a time, no list `f59ed4b3a <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/f59ed4b3a943f4f57398c979e6f3b0bd8e84cfcb>`_
- Add unit-tests for the fedora_elections messages `77ebbff64 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/77ebbff649639c3703446494787f5d2b61d8a57a>`_
- Link the unit-tests for fedora_elections into the main test suite `03887eaa1 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/03887eaa143a019500d2ec9f252cfaf090c650c6>`_
- pep8 fixes on the trac tests `90a3d0933 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/90a3d0933c65015eb09a1714e5c656851eea0055>`_
- pep8 fixes on the summershum tests `2080bdca7 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/2080bdca77d44c108e05491a0bc0b3e3c939611f>`_
- pep8 fixes on the mailman3 tests `0b0f1a69b <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/0b0f1a69bf756b2a801767462af8e838386d93d1>`_
- pep8 fixes on the pkgdb tests `7e914cc87 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/7e914cc87a1d3d71734fdb6303b8bdb6571fb8da>`_
- pep8 fixes on the jenkins tests `05d3ddb25 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/05d3ddb2569d713532ed6a0adc2850a996d53d64>`_
- pep8 fixes on the github tests `a4e11b75a <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/a4e11b75a9a32b7abdf3db39070cecd50f3d2459>`_
- pep8 fixes on the askbot tests `723536331 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/7235363314355638a55c5c3e80313da08bc4e939>`_
- pep8 fixes on the ansible tests `29d4de8e7 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/29d4de8e76c5161b37e8bcf2a8f8f19dca22cafc>`_
- pep8 fixes on the pkgdb meta file `9ddcabbee <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/9ddcabbee4dd2b8af6e4300ad0d4ffed7f384df6>`_
- pep8 fixes on the jenkins meta file `5da6fcd04 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/5da6fcd04c68ad387949f3b7c411f1f38bf00863>`_
- pep8 fixes on the fasshim meta file `c090e4281 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/c090e42812cb82b379c4f4f1b729337163ed5d30>`_
- pep8 fixes on the cnucnuweb meta file `cbcd846f9 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/cbcd846f9048088ed35966dc475e822117ed056b>`_
- pep8 fixes on fedmsg.d/base.py `8232320fa <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/8232320fa1bb1583919823337c8f143866aecfe3>`_
- pep8 fixes on the setup.py file `363058da5 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/363058da5b6db9e0a001a75afa2c7725536889a8>`_
- Merge pull request #77 from fedora-infra/elections `7dd0715b4 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/7dd0715b4f1b35363223788689fa6384b982f667>`_
- Merge pull request #78 from fedora-infra/pep8 `b787911bf <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/b787911bf1cc638a660558b7d592b116744cfd67>`_
- Be careful with copr messages here. `5a6fbd0c4 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/5a6fbd0c406db5f935b19f927933332bf3ccee43>`_
- Use the new copr frontend url. `7c0830cfc <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/7c0830cfc9cd235b0e3be872423c30d5da80f235>`_
- Merge pull request #80 from fedora-infra/feature/take-care-with-copr `cf64f50d1 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/cf64f50d1c352b25ff0ac81f9f6c11e619abee01>`_
- Retire this one bodhi masher message. `043dbad9b <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/043dbad9b9f63b7f41cb12591490ff52224dfcba>`_
- Merge pull request #82 from fedora-infra/feature/retire-masher-message `e395dd421 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/e395dd42192265c0ccee92d6d188f5218b0ca5e3>`_
- Give fedmsg.meta its own doc infrastructure. `0b866c2c3 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/0b866c2c364e546cfd26e7fd2ec8460e3da27258>`_
- Merge pull request #83 from fedora-infra/feature/doc-split `7181bf8d6 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/7181bf8d6b089033eb6dd5d830cbc860b2117b6f>`_
- Adjust the URL to point to the right pkgdb2 page `c4249c393 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/c4249c3933e22f3f109baa9ed78242f7052cfaf0>`_
- Adjust the unit-tests to use the correct URL for pkgdb2 `91b941e4f <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/91b941e4f89e3b925e3772713d0ba1bfbe08ffc1>`_
- small pep8 fix to make pep8bot happy `e9f5d285a <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/e9f5d285a4eb5dfdf75493df65d9587fc4ccb361>`_
- Merge pull request #84 from fedora-infra/pkgdb2_url `5136e3434 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/5136e343476edc3271ca1ab3cd70ec10bf512aa8>`_
- Copr icon. `a1d296828 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/a1d296828022853ee88e6b9a45fc587d858df68c>`_
- Test that icon, too. `27d0552cd <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/27d0552cdeec1162a81690c32dfa2d080a94c1e7>`_
- Icons for meetbot. `9e733ea93 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/9e733ea93d33238a01cd0f469db5ea0dcd23c76f>`_
- Just to be sure. `e0c087f96 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/e0c087f961caefa974ac7cbad679db62fbf9eb29>`_
- More being sure. `44ab1f881 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/44ab1f88149818bea1e75e2a63bdfaeb239b8644>`_
- Ignore the topics .rst doc.  It is auto generated. `b884d5b6f <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/b884d5b6fd5caba540f45d8dcbfda7084c656d7c>`_
- Update koji examples. `dc1611712 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/dc1611712652219aa5aa5b5d09ce75c498a004c7>`_
- Merge pull request #87 from fedora-infra/feature/update-koji-examples `5822fe792 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/5822fe792c4bfef104067d9a89f742482083c2d5>`_
- Merge pull request #86 from fedora-infra/feature/meetbot-icon `672917fe3 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/672917fe32cb8ad32de5355bc152fa39c5282dc8>`_
- Merge pull request #85 from fedora-infra/feature/copr-icon `bba920ec1 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/bba920ec1ac21e82551186dad1ff9e3a87f9c77e>`_
- Fix meetbot topic changes. `903861a4e <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/903861a4eb9838c35dec31fe1681f09bb8f33aee>`_

0.2.11
------

- A processor for github2fedmsg. `11c95c4d2 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/11c95c4d2b9e2ab01a7f621171e07af13da3148a>`_
- Merge pull request #70 from fedora-infra/feature/github `365cf5365 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/365cf53657f3d1088a25514ba14a1fe6283b3370>`_
- Add tests and processor for the new ftp sync messages. `34bfa48aa <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/34bfa48aa5bf931f4b7d51a1bbe38ad69839fa9b>`_
- Merge pull request #71 from fedora-infra/feature/ftpsync `98e7e293a <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/98e7e293a12b155e93ee422ae8e1a524346bf7ce>`_
- The bytes field is actually 'human readable' `1496bbe72 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/1496bbe722cfeb38ec7a26b1b6834da7d9b4d12f>`_

0.2.10
------

- Fix another one of these that we missed. `916ca7582 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/916ca75821944d564bcfd5ccc4ded5d200cf057c>`_
- Handle impossibly unlikely datanommer events. `760d9f3b6 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/760d9f3b692dc1af1ba86d310e61eec621fc51bf>`_
- Only return meetbot links when the meeting is actually over. `9bb73693c <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/9bb73693c7005952860f09fda37288762c3fab7f>`_
- Merge pull request #36 from fedora-infra/feature/wat `605950b3d <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/605950b3d8f7f3bf941c36de18015c872a572fbb>`_
- Merge pull request #37 from fedora-infra/feature/no-link-at-start `98ab1adac <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/98ab1adac0318c57a21791f9517554ec936d0094>`_
- Add message handlers for fedocal. `61310888c <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/61310888cfb1d827dfb87cf6ebf7016fd49bdc10>`_
- Update owner to point-of-contact for pkgdb2. `314985840 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/3149858404cb5324e040acbb6fab1ff47661e340>`_
- Handle new package.update message format. `87c0689fb <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/87c0689fb3c589c3c777eae55351abcb7c17f07e>`_
- Handle new branch start and complete messages. `503fb1550 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/503fb1550e23c6b847976b29bc0ce86e4e70a193>`_
- Handle messages for new pkgdb collections. `c0ad7c834 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/c0ad7c834f7e9c701ecca727307047ad77b560ad>`_
- Handle messages for updated pkgdb collections. `500937f9d <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/500937f9d45f4747b2c29c825bac22f54f5eb800>`_
- Support relative delta stuff for fedocal reminders. `7229b93d0 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/7229b93d0698a8becf5736240c9cd97d586c025c>`_
- Link directly to fedocal meetings. `87fd59bdc <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/87fd59bdcb1e0db3cde7396c7475deedffb77f3f>`_
- Nuancier stuff. `31a309ca9 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/31a309ca9b57b1ac64bd66e9c37c232def66a2a8>`_
- Merge pull request #40 from fedora-infra/feature/nuancier `52381965d <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/52381965db4f8637974fde6eb788826ac3f3307e>`_
- 0.2.2 `5dc6e3cf1 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/5dc6e3cf195f3e992e0dcb058d71a2b47f04732e>`_
- Merge branch 'feature/fedocal' into develop `add3992cf <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/add3992cf3b3cea646b15eda2d75f465da4fd30f>`_
- Keep formatting consistent. `4f90fd269 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/4f90fd2698d26954b3cb0ebf351787999e0b4861>`_
- Merge pull request #38 from fedora-infra/feature/packagedb2 `cc9d468f3 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/cc9d468f39c43ef89f6c4d89cb6830099379ce07>`_
- 0.2.3 `bab0c0018 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/bab0c00187b82b1143f5bd63f145ef4cba04e91a>`_
- disable avatar test `5845dae6c <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/5845dae6cf2f666397d0495b914abbd5431fd786>`_
- Handle the new badges message. `cd8973c74 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/cd8973c740bf23c2b09217342387e45a89b9ed40>`_
- For the very first time. `846f90774 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/846f90774515b5905a053b854ed22da665c2dd54>`_
- Merge pull request #42 from fedora-infra/feature/badges-login `770bb4b19 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/770bb4b199190464e95a594949b26e39a02dd14a>`_
- Add the __doc__ trick to the bottom of all the test modules. `5bee972ad <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/5bee972ad7703590c66daf0945dfa75e39df2956>`_
- Fix issue with import (kitchen) and refactoring the code. `7d66afb02 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/7d66afb02c4bc0e862d960c5820bca302c228ab2>`_
- Reorder to install requires `81f470470 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/81f470470cb09c6e441f97bb41111affbc4f4034>`_
- PEP8, refactoring `839979c56 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/839979c567042376446df4c2a00856124cb6cb80>`_
- Remove blank spaces in bodhi.py msg `f0fa59956 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/f0fa5995660481ccfb1ea0d92f94fafa8be14695>`_
- Change in setup.py, sys.version_info < (2, 7) `0df4fcd05 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/0df4fcd05fd066a10607fab7d9e0b29b0239fef7>`_
- PEP8 `7e2e3926c <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/7e2e3926c408dd3da58cb2627bffa3bec7ea6e3a>`_
- Move that docs trick into a function. `10389be00 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/10389be001dcfd4b4f27175a818a1834186b91ab>`_
- PEP8/cosmetic while I'm here. `d214ac277 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/d214ac277d8b3c4fa5d0c1d2dfc4e77b5e08a92a>`_
- Add forgotten file. `c10f0cd21 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/c10f0cd21d7ed4015ac332c162dffca424cde343>`_
- Merge pull request #43 from fedora-infra/feature/docs-fix `9ba32c187 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/9ba32c187e3c75076830d9bab3d69c725d5f921c>`_
- Update bodhi.py `13e07f110 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/13e07f110ee566fdff4146dbf7c01fde641c1a3d>`_
- Update setup.py `3b1eb842f <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/3b1eb842fa0643646a4dcd3915248619c7a6f838>`_
- Merge pull request #44 from yograterol/develop `d899914c1 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/d899914c173790766204e0110bc63bef5a56fa71>`_
- Replace string concatentation with literals `05005c6ad <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/05005c6adbe772ace3f56c652bb5a32f21eeba63>`_
- Merge pull request #45 from echevemaster/develop `a4fcc2fc8 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/a4fcc2fc8c5a8e7f29dd91344b7a16c51971f254>`_
- Make Git icons square `9be80070f <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/9be80070f5a4c392d1f4410065268f17d1a02f35>`_
- Fix tests for git logo change `459e51399 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/459e5139969875e1c08728d90501bb2c989ec100>`_
- whoops `5d60aa18a <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/5d60aa18afac298152c6659882a17befd35fe10d>`_
- Merge pull request #46 from fedora-infra/feature/square-git-logo `b909ef640 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/b909ef64086916d7adc126c5df42087c982fe22a>`_
- Handle old compose branches. `a783a995d <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/a783a995d17a348d1b0b177b300f9c47332392a4>`_
- Copr processor with accompanying tests. `57639b9ad <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/57639b9ad114c185a3665fc82dd7d77d747fd746>`_
- Merge pull request #47 from fedora-infra/feature/old-compose-branches `1f85a8b95 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/1f85a8b95e7efb33b521d70dad01ea40d3d4775f>`_
- Support copr.worker.create messages. `9f8fbccf9 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/9f8fbccf9c68a720b19cc11850b7c147f33dad12>`_
- Merge pull request #48 from fedora-infra/feature/coprs `fa5c09ec2 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/fa5c09ec229e2bd33839ea8cd43ecbd710d7e845>`_
- 0.2.4 `4462b341f <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/4462b341f36a8693fc3f739f38c96a4e2a554ddb>`_
- Fixed docstring for the bodhi multi-build update test `3db4e27c0 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/3db4e27c0dfd757ee2fbae4f5022f3b312574ae1>`_
- Tests for cnucnuweb messages. `8130a748c <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/8130a748c7be938304386934fa5965f7f285fa25>`_
- Test for new version messages. `c23c9d280 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/c23c9d2801b5f2eeb871da20041b84647d96bd1a>`_
- Add instructions to the README. `4d1c8efeb <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/4d1c8efeb41c172701d2a883b672da5c90ede980>`_
- cnucnu processor written to the tests. `3ef6caebf <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/3ef6caebfe6a9f5e5e20d1b6ee01dbff690a653a>`_
- Merge branch 'develop' of github.com:fedora-infra/fedmsg_meta_fedora_infrastructure into develop `8a013f5ca <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/8a013f5caae4f4ae781afe98fd60d87ca735f928>`_
- RFE: https://github.com/fedora-infra/fedmsg/issues/118 `f437dc51d <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/f437dc51dc79dfbb6c94fba1b1b45807e25a638c>`_
- Merge pull request #50 from fedora-infra/feature/cnucnuweb `5dc92b4ea <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/5dc92b4eaf9dd72f2ab19f09ee8bea01b3a7ef3f>`_
- Handle scratch builds. `1626fda81 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/1626fda81eb536684594f18514702ecdf68a2f2b>`_
- Support for epelbeta compose messages.  Fixes #52. `af8511171 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/af8511171a0315c6ddfce3734ab4c073f0935c60>`_
- Merge pull request #51 from fedora-infra/feature/scratch-builds `32154f6cb <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/32154f6cbb3e1dbff57c814f1a57365f80293a38>`_
- Merge pull request #53 from fedora-infra/feature/epelbeta `03ba3c8cd <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/03ba3c8cdf7cdecabc7b9e80010c40acfb7f5428>`_
- 0.2.5 `28bbb0a13 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/28bbb0a13d193d1d7da6c7f0f74232bb25ff442f>`_
- Add meta information and tests for the new messages added to fedocal `4f8a864dc <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/4f8a864dca3294aace306a4a95be6852bd7e0dd4>`_
- Update the pseudo messages to reflect changes to fedocal `544931a19 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/544931a19d3d943f92e93be173973ba86695fc6a>`_
- Merge pull request #55 from fedora-infra/fedocal `1479eb33b <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/1479eb33b19d5ed968d38286b27626651f31cb74>`_
- Use a new location for rawhide compose links.  Fixes #56. `4ca0a55a3 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/4ca0a55a39e12d340cd0d662fa8169310f9e28f0>`_
- Merge pull request #57 from fedora-infra/feature/new-compose-links `87bee86ec <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/87bee86ecd8615f1104938675ed20e20a7cee6f8>`_
- Handle cancelled scratch builds. `6fce5f96a <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/6fce5f96aedd2c05edfd0793646c9a8df433c711>`_
- Merge pull request #58 from fedora-infra/feature/cancelled-scratch-build `2f88e4026 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/2f88e40262b9812d370e8c2c13d1975e309a2e76>`_
- Add tests and processor stuff for new tagger usage messages. `c0c979b76 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/c0c979b763b60476508ca9e7c6cae622ed6b04a3>`_
- Handle anonymous users here. `7c0386c87 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/7c0386c8794ef50091e847f1181ec32a83b2e1ef>`_
- Merge pull request #59 from fedora-infra/feature/tagger-usage-toggle `e05fed039 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/e05fed039eb2e9d358da0389ee5eefa4ecafc72b>`_
- Adjust entry point name to match the topic modname. `981cacde2 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/981cacde25a2a4cdcd5d9fa57e2c63ca737b3ac1>`_
- Distinguish between the primary koji instance and the secondary ones. `733ba3f90 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/733ba3f90b9d942a9ff8d73ec655bb2f72b2b538>`_
- Merge pull request #60 from fedora-infra/feature/secondary-kojis `4bf8d14e9 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/4bf8d14e912c6b564e6518bb8b22cefe21d77dcb>`_
- 0.2.6 `cd4676bd5 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/cd4676bd56ba059eeedb84f2686f99a126d440fb>`_
- Avoid modifying the original message in that last feature. `de02d9e1d <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/de02d9e1dabf5c9818b6b3505e5396f1363aaad8>`_
- 0.2.7 `8ff643c84 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/8ff643c84c90b87eda06a15faed5175b1bff9ce2>`_
- Recover from failing to cache fas. `403838dd2 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/403838dd239d3aee659ae5c12459889b22f97975>`_
- Add summershum processor and tests. `ad2cb5ba3 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/ad2cb5ba3caddbcec93cc6dc3b469c10917ab030>`_
- Merge pull request #62 from fedora-infra/feature/summershum `8ff4d7f1a <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/8ff4d7f1a5e2223ca78d77d91264f870cb550f21>`_
- Merge pull request #61 from fedora-infra/feature/careful-with-the-fascache `0f7c1944c <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/0f7c1944cbb1af65391ef425cd8c0e9e783246d2>`_
- 0.2.8 `61e71be95 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/61e71be957e3c77fb7fb1102315c526f835874f0>`_
- Update to handle new nuancier messages. `285be6abd <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/285be6abd790ff6588e1cdab536024fbfb3c8999>`_
- Turns out that this field might not necessarily be a FAS username... `45e8f8ea0 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/45e8f8ea00bd69521936756dda091e7685e23757>`_
- Merge pull request #63 from fedora-infra/feature/nuancier-heavy `4229bb504 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/4229bb5047016b55d322ca949c5e5dac702f4c12>`_
- Legacy support - old bodhi messages don't have this field. `d5d3ed74f <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/d5d3ed74f34acc85183f9cb8ca1441e568c76e1e>`_
- Merge pull request #64 from fedora-infra/feature/bodhi-legacy `71b0d2a19 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/71b0d2a198df07d1de81fd4291ad7735ad154ca9>`_
- Add links for summershum messages. `4e6b83b14 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/4e6b83b14393afb70432d1fab7c76d2179a15c67>`_
- Merge pull request #65 from fedora-infra/feature/links-for-summershum `e370d3fa0 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/e370d3fa0c4ad7670bfcf8d5f4295097f16d8dab>`_
- Add support for upcoming jenkins messages `7f474516f <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/7f474516f0c9330e6625587dae22d7c893ad5745>`_
- Fix tests. Thanks @ralphbean! `0e824e73c <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/0e824e73cdd9ed314ccbd7761f9cfd7d0863ad69>`_
- correct copyright year `b21b42b00 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/b21b42b00446d5acb71b19d7ebc209392e498c53>`_
- Legacy support - old bodhi messages don't have this field. `8b9fce49a <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/8b9fce49a691b43d689b3d27bb87eb3bde8cb888>`_
- Add links for summershum messages. `e47ed6f3b <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/e47ed6f3ba2b9164d776baed254741acc0cf327e>`_
- Merge branch 'develop' of github.com:fedora-infra/fedmsg_meta_fedora_infrastructure into develop `f04722910 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/f047229101575d77c60e7ff59362c8820f128eb9>`_
- 0.2.9 `fff744d0a <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/fff744d0a481d6e6acb30357d4deba6be8c4135f>`_
- Koji messages should really have a secondary icon. `920935ecb <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/920935ecb4878aca2f6e5328362e19fd1ebf70a3>`_
- Planet gets an icon too. `7048681ad <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/7048681ad561eb349f8d5c620dfd5474d8ac90cd>`_
- Sort out the tagger icons. `a85d5dd6b <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/a85d5dd6b3e15c6ceb6e0e1c2e18accb24eae38a>`_
- Give askbot an icon, courtsey of @ryanlerch. `111ccfd30 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/111ccfd3056ec0f1d68c81a47c5be3d6209d8d76>`_
- Secondary icons for lookaside messages. `5070bc97e <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/5070bc97efca3f06ebb57cab35fdb115c5c0d0fc>`_
- Make the git fallback icon more consistent with the other categories. `59b07fe99 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/59b07fe9991ef4dd9055be443708f5743f25bd34>`_
- Include the package name in summershum message subtitles. `54ca99f52 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/54ca99f520a180d737b629b1c939aecb7123360b>`_
- Merge pull request #67 from fedora-infra/feature/icons `55bf4269a <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/55bf4269ac045ddea995646420644542aad4eeed>`_
- Merge pull request #68 from fedora-infra/feature/summershum-pkg `5bb493442 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/5bb493442979079e84cd31281e09840f9021becc>`_
- Ansible needs an icon, right? `8ad630df2 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/8ad630df2e34230fd6fc487870c132006d3a0dd7>`_
- And this one badge message could use an icon too. `11248bad1 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/11248bad10d2218483b4c5972c0b7e222cfc474f>`_
- Merge pull request #69 from fedora-infra/feature/more-icons `b8f592e59 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/b8f592e598c4a1741d11bf78d96b00ff304088e0>`_

0.2.1
-----

- Bugfix to ansible relative playbook.  You can run not-checked-in playbooks, btw. `46c82a191 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/46c82a191db5d5e974fdf3ed55645ccae7ce1b0c>`_
- Support rank.advance messages from the badges world. `6f757311f <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/6f757311f2dec5f449f391a852fb3c9aa5b9a167>`_
- Add a test showing that this never worked. `ddcaf59c0 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/ddcaf59c046d54ecea680e1613ff861e0928d881>`_
- Fix the ansible relative playbook stuff to make sense and match the test. `5a5541783 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/5a55417836a6efa3037fb208abd43f66b6c47714>`_
- [scm] fix subtitle for older messages without username specified `ad5e2c7c2 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/ad5e2c7c2ecb62ce8496cb8af7fe94e78e4aff2d>`_
- Merge branch 'develop' into feature/scm-old-message-bugfix `9f41909b9 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/9f41909b91d16a236061b5d326086e9e611680c2>`_
- Merge branch 'develop' into feature/ansible-relative-playbook-bugfix `946ca3bab <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/946ca3bab2298c853ef62db8edf45ecf82fabdd5>`_
- Merge branch 'develop' into feature/badges-rank `66d0156e9 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/66d0156e9e5a3108e158a42fbcdfa1a8bda845d3>`_
- Catch up to the latest from the develop branch. `b3619e38a <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/b3619e38a19f6ed06fa0cecef6ab4bb7a3bddf28>`_
- Merge branch 'develop' of github.com:fedora-infra/fedmsg_meta_fedora_infrastructure into feature/scm-old-message-bugfix `6aad75e8c <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/6aad75e8c871bd96459c5d257d1a293feee1006a>`_
- Add test suite to cover older SCM messages without username specified `8c01e50eb <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/8c01e50eb0bbcddb0d54d1034fed616162d41b1c>`_
- Merge pull request #34 from fedora-infra/feature/scm-old-message-bugfix `a2f793b62 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/a2f793b62567c4805dff9c9a90e35bb219e7b9bf>`_
- Merge pull request #28 from fedora-infra/feature/ansible-relative-playbook-bugfix `045742bb2 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/045742bb2e1cdcb5bd216f1344281265270fa481>`_
- Check the contents in _get_user. `32b6ce7ab <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/32b6ce7ab95a3ce5a45bf697e05227a78d432a87>`_
- Merge pull request #32 from fedora-infra/feature/badges-rank `77a03320c <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/77a03320c2cf1e503539f2de1ad4bc1e282290c2>`_
- Merge branch 'develop' of github.com:fedora-infra/fedmsg_meta_fedora_infrastructure into develop `ddca35716 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/ddca35716872884d8e6973ce398b4f27edf333dd>`_

0.2.0
-----

- Bugfix to ansible relative playbook.  You can run not-checked-in playbooks, btw. `46c82a191 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/46c82a191db5d5e974fdf3ed55645ccae7ce1b0c>`_
- Support rank.advance messages from the badges world. `6f757311f <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/6f757311f2dec5f449f391a852fb3c9aa5b9a167>`_
- Add a test showing that this never worked. `ddcaf59c0 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/ddcaf59c046d54ecea680e1613ff861e0928d881>`_
- Fix the ansible relative playbook stuff to make sense and match the test. `5a5541783 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/5a55417836a6efa3037fb208abd43f66b6c47714>`_
- [scm] fix subtitle for older messages without username specified `ad5e2c7c2 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/ad5e2c7c2ecb62ce8496cb8af7fe94e78e4aff2d>`_
- Merge branch 'develop' into feature/scm-old-message-bugfix `9f41909b9 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/9f41909b91d16a236061b5d326086e9e611680c2>`_
- Merge branch 'develop' into feature/ansible-relative-playbook-bugfix `946ca3bab <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/946ca3bab2298c853ef62db8edf45ecf82fabdd5>`_
- Merge branch 'develop' into feature/badges-rank `66d0156e9 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/66d0156e9e5a3108e158a42fbcdfa1a8bda845d3>`_
- Catch up to the latest from the develop branch. `b3619e38a <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/b3619e38a19f6ed06fa0cecef6ab4bb7a3bddf28>`_
- Merge branch 'develop' of github.com:fedora-infra/fedmsg_meta_fedora_infrastructure into feature/scm-old-message-bugfix `6aad75e8c <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/6aad75e8c871bd96459c5d257d1a293feee1006a>`_
- Add test suite to cover older SCM messages without username specified `8c01e50eb <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/8c01e50eb0bbcddb0d54d1034fed616162d41b1c>`_
- Merge pull request #34 from fedora-infra/feature/scm-old-message-bugfix `a2f793b62 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/a2f793b62567c4805dff9c9a90e35bb219e7b9bf>`_
- Merge pull request #28 from fedora-infra/feature/ansible-relative-playbook-bugfix `045742bb2 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/045742bb2e1cdcb5bd216f1344281265270fa481>`_
- Check the contents in _get_user. `32b6ce7ab <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/32b6ce7ab95a3ce5a45bf697e05227a78d432a87>`_
- Merge pull request #32 from fedora-infra/feature/badges-rank `77a03320c <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/77a03320c2cf1e503539f2de1ad4bc1e282290c2>`_
- Merge branch 'develop' of github.com:fedora-infra/fedmsg_meta_fedora_infrastructure into develop `ddca35716 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/ddca35716872884d8e6973ce398b4f27edf333dd>`_
- 0.2.1 `2cbc327b9 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/2cbc327b90db28e80e3b4ebde6f746ad1d15c2bb>`_
- Fix another one of these that we missed. `916ca7582 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/916ca75821944d564bcfd5ccc4ded5d200cf057c>`_
- Handle impossibly unlikely datanommer events. `760d9f3b6 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/760d9f3b692dc1af1ba86d310e61eec621fc51bf>`_
- Only return meetbot links when the meeting is actually over. `9bb73693c <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/9bb73693c7005952860f09fda37288762c3fab7f>`_
- Merge pull request #36 from fedora-infra/feature/wat `605950b3d <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/605950b3d8f7f3bf941c36de18015c872a572fbb>`_
- Merge pull request #37 from fedora-infra/feature/no-link-at-start `98ab1adac <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/98ab1adac0318c57a21791f9517554ec936d0094>`_
- Add message handlers for fedocal. `61310888c <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/61310888cfb1d827dfb87cf6ebf7016fd49bdc10>`_
- Update owner to point-of-contact for pkgdb2. `314985840 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/3149858404cb5324e040acbb6fab1ff47661e340>`_
- Handle new package.update message format. `87c0689fb <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/87c0689fb3c589c3c777eae55351abcb7c17f07e>`_
- Handle new branch start and complete messages. `503fb1550 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/503fb1550e23c6b847976b29bc0ce86e4e70a193>`_
- Handle messages for new pkgdb collections. `c0ad7c834 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/c0ad7c834f7e9c701ecca727307047ad77b560ad>`_
- Handle messages for updated pkgdb collections. `500937f9d <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/500937f9d45f4747b2c29c825bac22f54f5eb800>`_
- Support relative delta stuff for fedocal reminders. `7229b93d0 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/7229b93d0698a8becf5736240c9cd97d586c025c>`_
- Link directly to fedocal meetings. `87fd59bdc <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/87fd59bdcb1e0db3cde7396c7475deedffb77f3f>`_
- Nuancier stuff. `31a309ca9 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/31a309ca9b57b1ac64bd66e9c37c232def66a2a8>`_
- Merge pull request #40 from fedora-infra/feature/nuancier `52381965d <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/52381965db4f8637974fde6eb788826ac3f3307e>`_
- 0.2.2 `5dc6e3cf1 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/5dc6e3cf195f3e992e0dcb058d71a2b47f04732e>`_
- Merge branch 'feature/fedocal' into develop `add3992cf <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/add3992cf3b3cea646b15eda2d75f465da4fd30f>`_
- Keep formatting consistent. `4f90fd269 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/4f90fd2698d26954b3cb0ebf351787999e0b4861>`_
- Merge pull request #38 from fedora-infra/feature/packagedb2 `cc9d468f3 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/cc9d468f39c43ef89f6c4d89cb6830099379ce07>`_
- 0.2.3 `bab0c0018 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/bab0c00187b82b1143f5bd63f145ef4cba04e91a>`_
- disable avatar test `5845dae6c <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/5845dae6cf2f666397d0495b914abbd5431fd786>`_
- Handle the new badges message. `cd8973c74 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/cd8973c740bf23c2b09217342387e45a89b9ed40>`_
- For the very first time. `846f90774 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/846f90774515b5905a053b854ed22da665c2dd54>`_
- Merge pull request #42 from fedora-infra/feature/badges-login `770bb4b19 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/770bb4b199190464e95a594949b26e39a02dd14a>`_
- Add the __doc__ trick to the bottom of all the test modules. `5bee972ad <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/5bee972ad7703590c66daf0945dfa75e39df2956>`_
- Fix issue with import (kitchen) and refactoring the code. `7d66afb02 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/7d66afb02c4bc0e862d960c5820bca302c228ab2>`_
- Reorder to install requires `81f470470 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/81f470470cb09c6e441f97bb41111affbc4f4034>`_
- PEP8, refactoring `839979c56 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/839979c567042376446df4c2a00856124cb6cb80>`_
- Remove blank spaces in bodhi.py msg `f0fa59956 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/f0fa5995660481ccfb1ea0d92f94fafa8be14695>`_
- Change in setup.py, sys.version_info < (2, 7) `0df4fcd05 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/0df4fcd05fd066a10607fab7d9e0b29b0239fef7>`_
- PEP8 `7e2e3926c <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/7e2e3926c408dd3da58cb2627bffa3bec7ea6e3a>`_
- Move that docs trick into a function. `10389be00 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/10389be001dcfd4b4f27175a818a1834186b91ab>`_
- PEP8/cosmetic while I'm here. `d214ac277 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/d214ac277d8b3c4fa5d0c1d2dfc4e77b5e08a92a>`_
- Add forgotten file. `c10f0cd21 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/c10f0cd21d7ed4015ac332c162dffca424cde343>`_
- Merge pull request #43 from fedora-infra/feature/docs-fix `9ba32c187 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/9ba32c187e3c75076830d9bab3d69c725d5f921c>`_
- Update bodhi.py `13e07f110 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/13e07f110ee566fdff4146dbf7c01fde641c1a3d>`_
- Update setup.py `3b1eb842f <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/3b1eb842fa0643646a4dcd3915248619c7a6f838>`_
- Merge pull request #44 from yograterol/develop `d899914c1 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/d899914c173790766204e0110bc63bef5a56fa71>`_
- Replace string concatentation with literals `05005c6ad <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/05005c6adbe772ace3f56c652bb5a32f21eeba63>`_
- Merge pull request #45 from echevemaster/develop `a4fcc2fc8 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/a4fcc2fc8c5a8e7f29dd91344b7a16c51971f254>`_
- Make Git icons square `9be80070f <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/9be80070f5a4c392d1f4410065268f17d1a02f35>`_
- Fix tests for git logo change `459e51399 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/459e5139969875e1c08728d90501bb2c989ec100>`_
- whoops `5d60aa18a <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/5d60aa18afac298152c6659882a17befd35fe10d>`_
- Merge pull request #46 from fedora-infra/feature/square-git-logo `b909ef640 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/b909ef64086916d7adc126c5df42087c982fe22a>`_
- Handle old compose branches. `a783a995d <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/a783a995d17a348d1b0b177b300f9c47332392a4>`_
- Copr processor with accompanying tests. `57639b9ad <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/57639b9ad114c185a3665fc82dd7d77d747fd746>`_
- Merge pull request #47 from fedora-infra/feature/old-compose-branches `1f85a8b95 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/1f85a8b95e7efb33b521d70dad01ea40d3d4775f>`_
- Support copr.worker.create messages. `9f8fbccf9 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/9f8fbccf9c68a720b19cc11850b7c147f33dad12>`_
- Merge pull request #48 from fedora-infra/feature/coprs `fa5c09ec2 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/fa5c09ec229e2bd33839ea8cd43ecbd710d7e845>`_
- 0.2.4 `4462b341f <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/4462b341f36a8693fc3f739f38c96a4e2a554ddb>`_
- Fixed docstring for the bodhi multi-build update test `3db4e27c0 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/3db4e27c0dfd757ee2fbae4f5022f3b312574ae1>`_
- Tests for cnucnuweb messages. `8130a748c <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/8130a748c7be938304386934fa5965f7f285fa25>`_
- Test for new version messages. `c23c9d280 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/c23c9d2801b5f2eeb871da20041b84647d96bd1a>`_
- Add instructions to the README. `4d1c8efeb <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/4d1c8efeb41c172701d2a883b672da5c90ede980>`_
- cnucnu processor written to the tests. `3ef6caebf <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/3ef6caebfe6a9f5e5e20d1b6ee01dbff690a653a>`_
- Merge branch 'develop' of github.com:fedora-infra/fedmsg_meta_fedora_infrastructure into develop `8a013f5ca <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/8a013f5caae4f4ae781afe98fd60d87ca735f928>`_
- RFE: https://github.com/fedora-infra/fedmsg/issues/118 `f437dc51d <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/f437dc51dc79dfbb6c94fba1b1b45807e25a638c>`_
- Merge pull request #50 from fedora-infra/feature/cnucnuweb `5dc92b4ea <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/5dc92b4eaf9dd72f2ab19f09ee8bea01b3a7ef3f>`_
- Handle scratch builds. `1626fda81 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/1626fda81eb536684594f18514702ecdf68a2f2b>`_
- Support for epelbeta compose messages.  Fixes #52. `af8511171 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/af8511171a0315c6ddfce3734ab4c073f0935c60>`_
- Merge pull request #51 from fedora-infra/feature/scratch-builds `32154f6cb <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/32154f6cbb3e1dbff57c814f1a57365f80293a38>`_
- Merge pull request #53 from fedora-infra/feature/epelbeta `03ba3c8cd <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/03ba3c8cdf7cdecabc7b9e80010c40acfb7f5428>`_
- 0.2.5 `28bbb0a13 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/28bbb0a13d193d1d7da6c7f0f74232bb25ff442f>`_
- Add meta information and tests for the new messages added to fedocal `4f8a864dc <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/4f8a864dca3294aace306a4a95be6852bd7e0dd4>`_
- Update the pseudo messages to reflect changes to fedocal `544931a19 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/544931a19d3d943f92e93be173973ba86695fc6a>`_
- Merge pull request #55 from fedora-infra/fedocal `1479eb33b <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/1479eb33b19d5ed968d38286b27626651f31cb74>`_
- Use a new location for rawhide compose links.  Fixes #56. `4ca0a55a3 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/4ca0a55a39e12d340cd0d662fa8169310f9e28f0>`_
- Merge pull request #57 from fedora-infra/feature/new-compose-links `87bee86ec <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/87bee86ecd8615f1104938675ed20e20a7cee6f8>`_
- Handle cancelled scratch builds. `6fce5f96a <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/6fce5f96aedd2c05edfd0793646c9a8df433c711>`_
- Merge pull request #58 from fedora-infra/feature/cancelled-scratch-build `2f88e4026 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/2f88e40262b9812d370e8c2c13d1975e309a2e76>`_
- Add tests and processor stuff for new tagger usage messages. `c0c979b76 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/c0c979b763b60476508ca9e7c6cae622ed6b04a3>`_
- Handle anonymous users here. `7c0386c87 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/7c0386c8794ef50091e847f1181ec32a83b2e1ef>`_
- Merge pull request #59 from fedora-infra/feature/tagger-usage-toggle `e05fed039 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/e05fed039eb2e9d358da0389ee5eefa4ecafc72b>`_
- Adjust entry point name to match the topic modname. `981cacde2 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/981cacde25a2a4cdcd5d9fa57e2c63ca737b3ac1>`_
- Distinguish between the primary koji instance and the secondary ones. `733ba3f90 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/733ba3f90b9d942a9ff8d73ec655bb2f72b2b538>`_
- Merge pull request #60 from fedora-infra/feature/secondary-kojis `4bf8d14e9 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/4bf8d14e912c6b564e6518bb8b22cefe21d77dcb>`_
- 0.2.6 `cd4676bd5 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/cd4676bd56ba059eeedb84f2686f99a126d440fb>`_
- Avoid modifying the original message in that last feature. `de02d9e1d <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/de02d9e1dabf5c9818b6b3505e5396f1363aaad8>`_
- 0.2.7 `8ff643c84 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/8ff643c84c90b87eda06a15faed5175b1bff9ce2>`_
- Recover from failing to cache fas. `403838dd2 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/403838dd239d3aee659ae5c12459889b22f97975>`_
- Add summershum processor and tests. `ad2cb5ba3 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/ad2cb5ba3caddbcec93cc6dc3b469c10917ab030>`_
- Merge pull request #62 from fedora-infra/feature/summershum `8ff4d7f1a <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/8ff4d7f1a5e2223ca78d77d91264f870cb550f21>`_
- Merge pull request #61 from fedora-infra/feature/careful-with-the-fascache `0f7c1944c <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/0f7c1944cbb1af65391ef425cd8c0e9e783246d2>`_
- 0.2.8 `61e71be95 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/61e71be957e3c77fb7fb1102315c526f835874f0>`_
- Update to handle new nuancier messages. `285be6abd <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/285be6abd790ff6588e1cdab536024fbfb3c8999>`_
- Turns out that this field might not necessarily be a FAS username... `45e8f8ea0 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/45e8f8ea00bd69521936756dda091e7685e23757>`_
- Merge pull request #63 from fedora-infra/feature/nuancier-heavy `4229bb504 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/4229bb5047016b55d322ca949c5e5dac702f4c12>`_
- Legacy support - old bodhi messages don't have this field. `d5d3ed74f <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/d5d3ed74f34acc85183f9cb8ca1441e568c76e1e>`_
- Merge pull request #64 from fedora-infra/feature/bodhi-legacy `71b0d2a19 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/71b0d2a198df07d1de81fd4291ad7735ad154ca9>`_
- Add links for summershum messages. `4e6b83b14 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/4e6b83b14393afb70432d1fab7c76d2179a15c67>`_
- Merge pull request #65 from fedora-infra/feature/links-for-summershum `e370d3fa0 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/e370d3fa0c4ad7670bfcf8d5f4295097f16d8dab>`_
- Add support for upcoming jenkins messages `7f474516f <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/7f474516f0c9330e6625587dae22d7c893ad5745>`_
- Fix tests. Thanks @ralphbean! `0e824e73c <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/0e824e73cdd9ed314ccbd7761f9cfd7d0863ad69>`_
- correct copyright year `b21b42b00 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/b21b42b00446d5acb71b19d7ebc209392e498c53>`_
- Legacy support - old bodhi messages don't have this field. `8b9fce49a <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/8b9fce49a691b43d689b3d27bb87eb3bde8cb888>`_
- Add links for summershum messages. `e47ed6f3b <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/e47ed6f3ba2b9164d776baed254741acc0cf327e>`_
- Merge branch 'develop' of github.com:fedora-infra/fedmsg_meta_fedora_infrastructure into develop `f04722910 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/f047229101575d77c60e7ff59362c8820f128eb9>`_
- 0.2.9 `fff744d0a <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/fff744d0a481d6e6acb30357d4deba6be8c4135f>`_
- Koji messages should really have a secondary icon. `920935ecb <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/920935ecb4878aca2f6e5328362e19fd1ebf70a3>`_
- Planet gets an icon too. `7048681ad <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/7048681ad561eb349f8d5c620dfd5474d8ac90cd>`_
- Sort out the tagger icons. `a85d5dd6b <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/a85d5dd6b3e15c6ceb6e0e1c2e18accb24eae38a>`_
- Give askbot an icon, courtsey of @ryanlerch. `111ccfd30 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/111ccfd3056ec0f1d68c81a47c5be3d6209d8d76>`_
- Secondary icons for lookaside messages. `5070bc97e <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/5070bc97efca3f06ebb57cab35fdb115c5c0d0fc>`_
- Make the git fallback icon more consistent with the other categories. `59b07fe99 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/59b07fe9991ef4dd9055be443708f5743f25bd34>`_
- Include the package name in summershum message subtitles. `54ca99f52 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/54ca99f520a180d737b629b1c939aecb7123360b>`_
- Merge pull request #67 from fedora-infra/feature/icons `55bf4269a <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/55bf4269ac045ddea995646420644542aad4eeed>`_
- Merge pull request #68 from fedora-infra/feature/summershum-pkg `5bb493442 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/5bb493442979079e84cd31281e09840f9021becc>`_
- Ansible needs an icon, right? `8ad630df2 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/8ad630df2e34230fd6fc487870c132006d3a0dd7>`_
- And this one badge message could use an icon too. `11248bad1 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/11248bad10d2218483b4c5972c0b7e222cfc474f>`_
- Merge pull request #69 from fedora-infra/feature/more-icons `b8f592e59 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/b8f592e598c4a1741d11bf78d96b00ff304088e0>`_
- 0.2.10 `5864cf427 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/5864cf427080d2241ecb8c08ef32757a39b8fd9f>`_
- A processor for github2fedmsg. `11c95c4d2 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/11c95c4d2b9e2ab01a7f621171e07af13da3148a>`_
- Merge pull request #70 from fedora-infra/feature/github `365cf5365 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/365cf53657f3d1088a25514ba14a1fe6283b3370>`_
- Add tests and processor for the new ftp sync messages. `34bfa48aa <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/34bfa48aa5bf931f4b7d51a1bbe38ad69839fa9b>`_
- Merge pull request #71 from fedora-infra/feature/ftpsync `98e7e293a <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/98e7e293a12b155e93ee422ae8e1a524346bf7ce>`_
- The bytes field is actually 'human readable' `1496bbe72 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/1496bbe722cfeb38ec7a26b1b6834da7d9b4d12f>`_
- 0.2.11 `d5cd3bff5 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/d5cd3bff51d66c5fddebda4cac0bd79564472b16>`_
- Need to pass through the config here... `2ff1888a6 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/2ff1888a60fb9051d6e9a0575193ed4825a2f98b>`_
- BZ processor and a test. `3e7ce519f <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/3e7ce519fad93ee5f0ffedadac4881aa6bff62a3>`_
- Handle messages for "new bugs" `410baa648 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/410baa648361795ded8c915b7b96a68a944b8b76>`_
- Correct module doc. `e91840446 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/e918404463f885f9de89ccfae685419325c290bf>`_
- Merge pull request #72 from fedora-infra/feature/bugzilla `b7b94bcf2 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/b7b94bcf2e463413740d2535cc0f3e3fd4e5a577>`_
- Use https for copr-be. `fb4e6249f <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/fb4e6249f1cc560d089badff9166fa4b158d0dda>`_
- https for wiki links, please. `b26b8ca11 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/b26b8ca11e3554f33335cccc137ea5a3d4704c2a>`_
- https for meetbot, please. `f195772d8 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/f195772d89f333210e36a184c496d5f3ffae37bc>`_
- Merge pull request #73 from fedora-infra/feature/https `162d231a6 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/162d231a6bcc370f0503879a3558c8f92bfdb0ba>`_
- Clarify user role at endmeeting.  Fixes #29. `e74642892 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/e7464289233e0993c1d1366ef14a240ea80ead35>`_
- Merge pull request #74 from fedora-infra/feature/user-at-endmeeting `a8b5cff01 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/a8b5cff014d11de6a22cd49245180630739bddc5>`_
- Remove "slave" field from jenkins `fbf3fc841 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/fbf3fc8417dab72d2981545ffb48495a8cf3be9c>`_
- Merge pull request #75 from fedora-infra/jenkins-take2 `ac853fcee <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/ac853fcee2ace23cf08253dd37f9c4fd02016d6a>`_
- Test tagger rank change messages.  Fixes #14. `e0541cde8 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/e0541cde81c6e250e7349f31a3414501202f0a88>`_
- Merge pull request #76 from fedora-infra/feature/test-tagger-rank `413194c36 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/413194c369704c5ca666a821d12cdf4a70a1801c>`_
- First work on the ElectionsProcessor for fedora-elections `ae75f73e1 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/ae75f73e149b19274fa656790ecef3ad733e6123>`_
- Update the elections Processor now that the messages contain an agent `3b4990e72 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/3b4990e72e465bedb3904b8f7e7022fd02780296>`_
- Adjust the __link__ now that the elections is on apps `f602cfbcf <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/f602cfbcf155ba689c279c60c03412dab288fddc>`_
- Manage messages regarding elections' candidate (new, edit, delete) `dc00a61a8 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/dc00a61a83f6e2bd045c780ea63ea0f8f4a74640>`_
- Adjust the setup.py file to include the elections processor `3c6e15edc <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/3c6e15edc6eb6a9cd03153b8c5913706744223b7>`_
- Import the ElectionsProcessor from the right file `843f8cfde <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/843f8cfde54c792f783314ab04d9fe4eaba47aaa>`_
- Fix trailing slash in the link in the elections processor and make it valid python `3c731ac51 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/3c731ac514d80d66de5fab67eab90b65b4cbc21b>`_
- Fix the usernames method `540b48954 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/540b4895441297c52b450fe3b3d2bad8712cc38d>`_
- pep8 fixes to the fedocal tests `831958858 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/831958858577d313258e333ce709136d397f9dfb>`_
- Fix the name, messages from the elections are of type fedora_elections `1e6d8c61e <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/1e6d8c61e2c79dff8fd55310e30491df1a470115>`_
- Fix the topic for editing or deleting candidates (and not elections) `dd27ca13e <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/dd27ca13efdb07e7dc902ec238f418cf4499adf1>`_
- The messages are only broadcasting one candidate at a time, no list `f59ed4b3a <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/f59ed4b3a943f4f57398c979e6f3b0bd8e84cfcb>`_
- Add unit-tests for the fedora_elections messages `77ebbff64 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/77ebbff649639c3703446494787f5d2b61d8a57a>`_
- Link the unit-tests for fedora_elections into the main test suite `03887eaa1 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/03887eaa143a019500d2ec9f252cfaf090c650c6>`_
- pep8 fixes on the trac tests `90a3d0933 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/90a3d0933c65015eb09a1714e5c656851eea0055>`_
- pep8 fixes on the summershum tests `2080bdca7 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/2080bdca77d44c108e05491a0bc0b3e3c939611f>`_
- pep8 fixes on the mailman3 tests `0b0f1a69b <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/0b0f1a69bf756b2a801767462af8e838386d93d1>`_
- pep8 fixes on the pkgdb tests `7e914cc87 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/7e914cc87a1d3d71734fdb6303b8bdb6571fb8da>`_
- pep8 fixes on the jenkins tests `05d3ddb25 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/05d3ddb2569d713532ed6a0adc2850a996d53d64>`_
- pep8 fixes on the github tests `a4e11b75a <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/a4e11b75a9a32b7abdf3db39070cecd50f3d2459>`_
- pep8 fixes on the askbot tests `723536331 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/7235363314355638a55c5c3e80313da08bc4e939>`_
- pep8 fixes on the ansible tests `29d4de8e7 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/29d4de8e76c5161b37e8bcf2a8f8f19dca22cafc>`_
- pep8 fixes on the pkgdb meta file `9ddcabbee <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/9ddcabbee4dd2b8af6e4300ad0d4ffed7f384df6>`_
- pep8 fixes on the jenkins meta file `5da6fcd04 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/5da6fcd04c68ad387949f3b7c411f1f38bf00863>`_
- pep8 fixes on the fasshim meta file `c090e4281 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/c090e42812cb82b379c4f4f1b729337163ed5d30>`_
- pep8 fixes on the cnucnuweb meta file `cbcd846f9 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/cbcd846f9048088ed35966dc475e822117ed056b>`_
- pep8 fixes on fedmsg.d/base.py `8232320fa <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/8232320fa1bb1583919823337c8f143866aecfe3>`_
- pep8 fixes on the setup.py file `363058da5 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/363058da5b6db9e0a001a75afa2c7725536889a8>`_
- Merge pull request #77 from fedora-infra/elections `7dd0715b4 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/7dd0715b4f1b35363223788689fa6384b982f667>`_
- Merge pull request #78 from fedora-infra/pep8 `b787911bf <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/b787911bf1cc638a660558b7d592b116744cfd67>`_
- Be careful with copr messages here. `5a6fbd0c4 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/5a6fbd0c406db5f935b19f927933332bf3ccee43>`_
- Use the new copr frontend url. `7c0830cfc <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/7c0830cfc9cd235b0e3be872423c30d5da80f235>`_
- Merge pull request #80 from fedora-infra/feature/take-care-with-copr `cf64f50d1 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/cf64f50d1c352b25ff0ac81f9f6c11e619abee01>`_
- Retire this one bodhi masher message. `043dbad9b <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/043dbad9b9f63b7f41cb12591490ff52224dfcba>`_
- Merge pull request #82 from fedora-infra/feature/retire-masher-message `e395dd421 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/e395dd42192265c0ccee92d6d188f5218b0ca5e3>`_
- Give fedmsg.meta its own doc infrastructure. `0b866c2c3 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/0b866c2c364e546cfd26e7fd2ec8460e3da27258>`_
- Merge pull request #83 from fedora-infra/feature/doc-split `7181bf8d6 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/7181bf8d6b089033eb6dd5d830cbc860b2117b6f>`_
- Adjust the URL to point to the right pkgdb2 page `c4249c393 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/c4249c3933e22f3f109baa9ed78242f7052cfaf0>`_
- Adjust the unit-tests to use the correct URL for pkgdb2 `91b941e4f <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/91b941e4f89e3b925e3772713d0ba1bfbe08ffc1>`_
- small pep8 fix to make pep8bot happy `e9f5d285a <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/e9f5d285a4eb5dfdf75493df65d9587fc4ccb361>`_
- Merge pull request #84 from fedora-infra/pkgdb2_url `5136e3434 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/5136e343476edc3271ca1ab3cd70ec10bf512aa8>`_
- Copr icon. `a1d296828 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/a1d296828022853ee88e6b9a45fc587d858df68c>`_
- Test that icon, too. `27d0552cd <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/27d0552cdeec1162a81690c32dfa2d080a94c1e7>`_
- Icons for meetbot. `9e733ea93 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/9e733ea93d33238a01cd0f469db5ea0dcd23c76f>`_
- Just to be sure. `e0c087f96 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/e0c087f961caefa974ac7cbad679db62fbf9eb29>`_
- More being sure. `44ab1f881 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/44ab1f88149818bea1e75e2a63bdfaeb239b8644>`_
- Ignore the topics .rst doc.  It is auto generated. `b884d5b6f <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/b884d5b6fd5caba540f45d8dcbfda7084c656d7c>`_
- Update koji examples. `dc1611712 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/dc1611712652219aa5aa5b5d09ce75c498a004c7>`_
- Merge pull request #87 from fedora-infra/feature/update-koji-examples `5822fe792 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/5822fe792c4bfef104067d9a89f742482083c2d5>`_
- Merge pull request #86 from fedora-infra/feature/meetbot-icon `672917fe3 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/672917fe32cb8ad32de5355bc152fa39c5282dc8>`_
- Merge pull request #85 from fedora-infra/feature/copr-icon `bba920ec1 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/bba920ec1ac21e82551186dad1ff9e3a87f9c77e>`_
- Fix meetbot topic changes. `903861a4e <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/903861a4eb9838c35dec31fe1681f09bb8f33aee>`_
- 0.2.12 `02f169e06 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/02f169e06e923cc74316827ded14b9ea7544a951>`_
- Processor and tests for FMN messages. `f8aa9b47f <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/f8aa9b47f9c678599a846d0c2c558f7ba31edcd0>`_
- Merge pull request #88 from fedora-infra/feature/fmn `9d693257b <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/9d693257b58d9696ddda3795a1c307a9d88072b5>`_
- Actually add the code for this. `9bce4b293 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/9bce4b293e6ec07a7416c63f62f88a3ed3cbb0bd>`_
- Merge branch 'feature/fmn' into develop `2521946b3 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/2521946b36cc08ed6d42de3ca79e50d610597d96>`_
- Pkgdb: Avoid redirects to URL with trailing slash `de99f5914 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/de99f59142fca006260ea74b2ee0a8ef2c06b243>`_
- Merge pull request #92 from tyll/avoid-redirects `4d9387fc8 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/4d9387fc85f1e984769e5b7426bc31f393f31f98>`_
- Pkgdb: Make package retirement messages explicit `42d30bda3 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/42d30bda3ef9464b0a7917f5b19f927cce4a41a3>`_
- Merge pull request #91 from tyll/develop `80fc3d9ea <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/80fc3d9eaeb067fe3a4f098b65e3225497bcb784>`_
- 0.2.13 `4a838f948 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/4a838f9480912806872e902f941a6a28d89acab3>`_
- Fix .rst syntax. `ff4853a39 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/ff4853a390171e944655b9d564f9ee4ebe41a763>`_
- compose: remove unused import `93ff47576 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/93ff47576d37fc49497f7eac43272c2a76d1a503>`_
- Use https where currently possible `62a9c6cbf <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/62a9c6cbf4ab61cf6e489f9c33c798e4721a5e36>`_
- Allow mentions in bodhi comments.  /cc @codeblock. `ffe34c428 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/ffe34c428ba5c6483c0eb76d428c495f0250645d>`_
- Merge pull request #94 from fedora-infra/feature/mentions `56a3b4270 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/56a3b42705cec5e1c821c93096039c1a99adceb7>`_
- Initial go at a fedmsg meta config for the new fedimg service. `b47fa4205 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/b47fa4205c2d3bc616696cac39a20c2a4dc14624>`_
- Typofix `f4a928d1e <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/f4a928d1e6b8ccae65345d964f967860f9ee18a5>`_
- Add marked up text and tests for bodhi messages. `bc68050a5 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/bc68050a55584ae13763c9375f2b2ee239cb307c>`_
- Merge pull request #98 from fedora-infra/feature/marked-up-bodhi `f8b840b96 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/f8b840b966d89e709f9ba18731d42ff1917a75fd>`_
- Merge pull request #93 from tyll/https `7e364d43f <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/7e364d43f2caeb360dfa2cf65613efe33a597e08>`_
- Allow the FAS url to be configurable. `dfab75e91 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/dfab75e91edc6832e79dfc1f4b8e097f95d66dff>`_
- Use a nuancier icon. `e309fb85d <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/e309fb85d03d540d9d9156f4a9dd107db68323ba>`_
- Cook our own avatar links. `84ba908dd <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/84ba908dd4173e35e93b5094abb0160a8f61a5fb>`_
- Use libravatar. `07a3e0a20 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/07a3e0a20c24c3bb7e12d9fc95864074a53fef0b>`_
- Update the tests to expect libravatar. `de7a296da <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/de7a296da74c612712bb8641c7093584dd08af1d>`_
- Merge pull request #100 from fedora-infra/feature/nuancier-icon `880a12c82 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/880a12c828dee94c30f103a20beb972690241f04>`_
- Show icons in docs. `0a02161f4 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/0a02161f4e33e4e7fd1c9d91d5ca1a68eec73528>`_
- Merge pull request #102 from fedora-infra/feature/show-icons-in-docs `25c003e03 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/25c003e030ffe731c9337bf6cb7b512cb06d05ca>`_
- Merge pull request #99 from fedora-infra/feature/configurable-fas-url `403b005f0 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/403b005f019eadaa41214dd64d2b0e528bc4f9c0>`_
- Merge pull request #101 from fedora-infra/feature/libravatar `78d057b2e <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/78d057b2e949588662cbb864a2396eca59ffaf65>`_
- Remove some stuff we don't need. `9fb656b2a <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/9fb656b2af6646355809ef743a06cafb57821fef>`_
- Make successful status 'completed' instead of 'succeeded' `f75a7711a <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/f75a7711ac6f60bcefd84ebd5c7e9318e64744b5>`_
- Tweaks as per @threebean's comments. `40fd23e49 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/40fd23e49903511bf5a3d85209760a84238bee95>`_
- Author --> Authors to match other files. `e6b19ba0b <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/e6b19ba0b3f01fe6f2217bd61f75052efd5e46c4>`_
- Start writing a test for Fedimg fedmsgs. `bb8590a21 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/bb8590a21cec481d262f3ffb71a90f4f22440799>`_
- Looks like this fedimg test passes `5d6e69df5 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/5d6e69df50b03f0ab959f731b4b55bb9d7826c8a>`_
- Typofix `d282bff37 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/d282bff37a3283e3957da7de4096864880c7700a>`_
- PEP 8 `675bfcc7f <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/675bfcc7fdb7ddb034e709f7944610a32a9317b6>`_
- These things aren't sets. `f69d1742f <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/f69d1742fced458564f66343e735b4f6c38a0ded>`_
- Crucial - declare the FedimgProcessor. `7bd2ce597 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/7bd2ce59746ed4b38e2150f8cbd9bd4d0d42c703>`_
- Run fedimg tests as part of the big suite. `7f3bebc6b <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/7f3bebc6b41386dc8832eeff5b9a555eab364804>`_
- Handle github.status messages. `7b3bad3bb <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/7b3bad3bbfcb86ed9c589ac0e6610585d642cee2>`_
- Handle github.delete messages. `4222b6491 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/4222b649189a20efc3fc7efb6131dc90ff768ad5>`_
- Handle pull request review comments. `72ada211c <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/72ada211c98aa4667be0a226013361822a14f051>`_
- Reorganize the way msg2objects works for github so that it makes more sense. `b118d4e1b <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/b118d4e1b8f8f291b283ddefc946785b5ae4bede>`_
- Fix key name. `b742848e2 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/b742848e2f44f49eebeca755a4dbe3c2e15c3627>`_
- py2.6 doesn't support str.format() without indexes `4d112edca <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/4d112edcacfdf203ff9889f67d02c1b5b090756e>`_
- This should be the image name, not the URL. `ca6b47006 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/ca6b47006b471c952e90a32ced32dc1c5c2dc731>`_
- Support commit comments. `a91f1a75b <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/a91f1a75b4648d394268b5ecb42e92d0d9c50b00>`_
- Merge pull request #103 from fedora-infra/feature/fedimg-meta `90379f404 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/90379f404f95757e8b05f04e1b57ce504cfa42f4>`_
- Merge pull request #104 from fedora-infra/feature/more-github-stuff `329d97cd8 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/329d97cd85a08fe3d4bd917bda2e190efcd1827b>`_
- 0.2.14 `9b4e0e58a <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/9b4e0e58aede0a0da96c44503d0c4d2318d85eb1>`_
- Add secondary icons for some cvsadmin and releng stuff. `fc4d4759e <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/fc4d4759e064e22279f7b8d1ddc66ac832dac8a5>`_
- Merge pull request #105 from fedora-infra/feature/some-secondary-icons `4ca3d5e97 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/4ca3d5e9776accc0c70182b0b55197b8e3e46ba8>`_
- Sometimes, these can exist, but be None. `fa432bff7 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/fa432bff7e9b6712d5dbfd1e93af5f9ebaf06959>`_
- Use short hashes here. `8598913ae <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/8598913aec0cfa58563aaa58bbfd5bd00d821cd7>`_
- Merge pull request #106 from fedora-infra/feature/short-hash `f50709d99 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/f50709d99a863412386e2bed523c0681b573a2a2>`_
- Kerneltest message handler and tests. `8d1b08b83 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/8d1b08b837778aa162321157ca53a05df12de7c8>`_
- Merge pull request #108 from fedora-infra/feature/kerneltest `4be76c72d <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/4be76c72df16430cd6570aa700d7359dc6af7f3b>`_
- Remove trailing slash that are no longer is use with elections2 `6201fe737 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/6201fe7371288c7ecdaf9904d9708cece790d4c9>`_
- Adjust the unit-tests to remove the trailing slash `7a38c4c62 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/7a38c4c62586e93495e4534601070729b5c7736a>`_
- Merge pull request #113 from fedora-infra/fix_elections `87f91f142 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/87f91f142d7237a482a99c3255c1de49b0e14a96>`_
- Indicate success of copr builds. `47e4e4e0b <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/47e4e4e0b24a74de7b08d9724ac3eca5968924af>`_
- Handle case where this can be None. `6415d246c <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/6415d246c189635bb93633a30a77ca709420b12b>`_
- Fix bug in subtitle for pkgdb.branch.start `015d6efd1 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/015d6efd11ec67a51babaa98875d565e33904d72>`_
- Merge pull request #114 from fedora-infra/feature/fixups `7abaad2a2 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/7abaad2a2b371ab9da761524806ca17747074c02>`_
- 0.2.15 `cac2991d1 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/cac2991d1acb6c81cb2d2baf237c99b30dc5725e>`_
- Handle an edge case with github messages. `895dab10a <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/895dab10ab8d1881c75cb53d52cab30afb22603e>`_
- Merge pull request #115 from fedora-infra/feature/github-edge-case `a74c6e9cf <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/a74c6e9cfca33b2e2b084eb6ecdaa9bff8adcd35>`_
- Add meta code for fedimg.image.test topic `bb65093d6 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/bb65093d607cd4be6174412fae0b664cafbf0ac0>`_
- Merge pull request #116 from fedora-infra/feature/fedimg-test-messages `89cf61d20 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/89cf61d20a71dea0cc53fc69dc5645f9a228fa13>`_
- Include the chroot in the description of finished builds on copr `3dcb851e9 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/3dcb851e931a6701da069f43a31509d64097fc9c>`_
- Adjust the unit-test for copr messages to reflect the addition of the chroot on the finished build message `5ba200ff9 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/5ba200ff9b6bfb8e03763f7367294f79febbcf91>`_
- Merge pull request #118 from fedora-infra/endbuild_chroot `f513436a2 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/f513436a2bee9b2be883ece084c8693182b45907>`_
- Hide old pkgdb1 retirement messages from the docs. `7d9c23a1b <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/7d9c23a1ba3066cc0d2aae36e7b172dc8ce68441>`_
- Merge pull request #119 from fedora-infra/feature/legacy-retirement `fc257d074 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/fc257d0743793d04e28392ea17b613b0f0298533>`_
- Add support for github.watch messages. `74fd4f45b <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/74fd4f45bd6ecbb06a6f8510464367c94a4d8649>`_
- Handle both starts and stops. `9fbfe371f <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/9fbfe371feab18a85398f535e1956a647a406b98>`_
- Merge pull request #120 from fedora-infra/feature/github-watch `b65ad6ab2 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/b65ad6ab275bba61f4177980d531d0c70c69a503>`_
- Added Class and Test `ccfea0d56 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/ccfea0d56453babd29e490bfbdad5936eaf6e2a0>`_
- added class for fedora college `c140ff8ba <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/c140ff8bac230a57d3ac5613dd5d5cef633070b4>`_
- Minor changes in file description `12329eeda <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/12329eeda662f78eabd2a64fdf6b5bad5c19f038>`_
- Merge pull request #121 from hammadhaleem/develop `ab6154c59 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/ab6154c59eeba5f3d2bff22434b513253a18019b>`_
- The topic packag.update.status is not package.update `9e852081d <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/9e852081d27a47f2569d1d0a2faa831c6ed9d13c>`_
- Handle the pkgdb.package.update messages `24022da8b <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/24022da8b5664e5ab0755ebd943674548fc75207>`_
- Adjust the unit-test name for PackageUpdateStatus `222f977bf <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/222f977bf16adeda8de14ce2b330fc2533ca615f>`_
- Add unit-tests for the package.update topic `a681f1b1f <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/a681f1b1fea2d5d581b63929c35de63f75b1620f>`_
- Merge pull request #122 from fedora-infra/fix_pkgdb `698c279f9 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/698c279f9d9f601540cdd8ea335849d12040fd70>`_
- Get the tests passing again. `b241d815e <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/b241d815ed951ad49abca8e4144d683dbad96c40>`_
- 0.2.16 `1a8d00b18 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/1a8d00b18ce287e6b1a685611df17630fbaa7300>`_
- add several jenkins statuses `2b7f67a68 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/2b7f67a689413978a2b431382f9c4b8582850a2c>`_
- Merge pull request #124 from fedora-infra/jenkins-try-again `de9a741a4 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/de9a741a4530870eb9377a8ac9891a69992c90fc>`_
- 0.2.17 `edd3fe59e <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/edd3fe59ec84ab9c38248a71aa86e5ceeca1b247>`_
- Fix tests. `3643db6e1 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/3643db6e189965561aea38b6ff286e87fcf4faf7>`_
- 0.2.18 `b46069572 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/b46069572f66b9c9ab8d2661b4fa2d38095e07ab>`_
- Comment out time-sensitive test. `1a8fe7b89 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/1a8fe7b89f6f4f7193740f6bb146f67fb2835c73>`_
- Debug missing topic. `b51dcb708 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/b51dcb7087484c8f6256c76beb9c80cb861f6a4e>`_
- Add missing topic. `6a1bd32d2 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/6a1bd32d2a4d8b228de4d1d910820561e2b1ca60>`_
- Merge pull request #126 from fedora-infra/feature/more-jenkins-fixes `22175af34 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/22175af34a7bd05a43356022c86fbb290ee5424a>`_
- Handle pkgdb.package.delete. `eb73eaf92 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/eb73eaf92d1b43dc1eef57245310fa98b09cfb2a>`_
- pkgdb.package.branch.delete and pkgdb.acl.delete `0df5e488d <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/0df5e488d0624548584c19e7f1d48ab17ae7d125>`_
- Merge pull request #128 from fedora-infra/feature/those-other-pkgdb-messages `c9ab3f9ed <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/c9ab3f9ed679144cf75519ced04d469e06d08d66>`_
- Handle the new pkgdb fedmsg messages `7fa96b37c <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/7fa96b37c8cc2c02e94a3d003cfa19e8f6f3e550>`_
- Adjust the unit-tests to test for these new messages `4dbf902f9 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/4dbf902f9977f8be3b94a11a2031c23a44990b93>`_
- Merge pull request #129 from fedora-infra/new_pkgdb `2b1a61c55 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/2b1a61c5557f55efea04db46efd68763ba6a39e0>`_
- There are case where the `action` dict is not there and case where it is `f9b10d582 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/f9b10d582224e2ef903ba25f6b5aabb1e649d514>`_
- Merge pull request #130 from fedora-infra/new_pkgdb `282e8fff2 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/282e8fff213a24bf57b18998f45f863994382dd3>`_
- Handle pkgdb critpath change messages. `5cb94cdb6 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/5cb94cdb6d80453404004edb28056bbb70093e74>`_
- Merge pull request #131 from fedora-infra/feature/critpath-messages `e273a0c1d <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/e273a0c1d3185b017918c74db1dea0ee03c1f590>`_
- 0.2.19 `53205342c <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/53205342c1de9e9b8e36006dcbe178dc173e2ef6>`_
- Throw a threading lock around the fas cache. `f920b11f4 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/f920b11f4a70832888101ad78757bf8e10540935>`_
- Merge pull request #132 from fedora-infra/feature/lock-around-fas-cache `8578931c4 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/8578931c449f37326145bd9ced4b045fee768040>`_
- First bodhi conglomerator. `179b922d5 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/179b922d553e6a3494e42a757378962814e063bc>`_
- Bugfix. `3ff8ebb5a <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/3ff8ebb5a7bc408eba99abc4e1e839177280cb9e>`_
- Unnecessary.  self.produce_template(..) actually includes this. `82e84ec37 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/82e84ec37e0ae2f1ba0e43145f7dad5f4ea6ea17>`_
- Link directly to copr builds. `19229d94a <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/19229d94aa04dc0cebbac61585d2fc19920eabfc>`_
- Merge pull request #134 from fedora-infra/feature/copr-builds `c616a8a9b <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/c616a8a9b0e5dd4a86c627e858cf20fbb0c32979>`_
- Merge pull request #133 from fedora-infra/feature/first-bodhi-conglomerator `0409486e8 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/0409486e80cdffab570d4fec0f769050fc6ba64a>`_
- Hardcode topic_prefix_re. `dd68205b1 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/dd68205b15586b0969e0269c7ccafac86adfe380>`_
- Merge pull request #136 from fedora-infra/feature/topic-prefix-hardcode `6a918f896 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/6a918f896ec08e4fe373dd2a50a1708c9e724821>`_
- Split that one into two different ones: for testing and stable. `e903f7af4 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/e903f7af404245d2180ebc21d0b57ba9a7418ffe>`_
- Add two new bodhi conglomerators. `8e7ae9ddb <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/8e7ae9ddbe8515f7952edc5dac57f828a0344675>`_
- Re-namespace stuff into a submodule.  There's going to be a lot of these... `247bd9a14 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/247bd9a14b868a0289efd174e65eadd6ba5acc02>`_
- Bodhi conglomerators for comments on updates. `6802ced0f <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/6802ced0f36677ee41abd8666532b50c37625cf1>`_
- Update docstrings as per review. `a3be25dbe <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/a3be25dbee4b272d5f5e364915e2a00c1697b205>`_
- Add meta information for the new pkgdb.package.branch.new messages of pkgdb2 `188e77354 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/188e77354274d2c88317794bb415937978e39c36>`_
- Add unit-tests for the pkgdb.package.branch.new messages `5a292463f <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/5a292463f020e5b8c6149071278aa8e9de65ee96>`_
- Show the new status attribute. `b798cf243 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/b798cf2435f32c49b80d73f7d30d3e0ecd0483da>`_
- Handle messages without status gracefully `f57035f5a <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/f57035f5aa69815cde9c498f3dfcccf7db257eec>`_
- Merge pull request #137 from fedora-infra/feature/more-bodhi-conglomerators `04afd1391 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/04afd139185c6876a30925f2a81f629b20ac0a89>`_
- Merge pull request #138 from fedora-infra/new_pkgdb `9c61d3bd6 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/9c61d3bd675d7b3ef2edf961ac77a7d66f96c633>`_
- s/Old/Legacy/ `0a421598a <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/0a421598af975a919db297b57bfc90c4f3e0d15d>`_
- Merge pull request #139 from fedora-infra/feature/new_status_for_fas `fb61fa224 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/fb61fa2248fd2d95ab3546b992708ba8914b5577>`_
- Fix the copr owner/user disagreement. `3b079a3c5 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/3b079a3c566c9de690c209aa82f29e002ef47da0>`_
- Fix copr usernames() method. `a7458caf6 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/a7458caf650a4b7e634efe3080634277634a108b>`_
- Merge pull request #140 from fedora-infra/feature/copr-owner-fix `6a466ce96 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/6a466ce96e38919b7f088e377e7a0965b2d5e9b4>`_
- 0.3.0 `c8c980bc9 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/c8c980bc96479943bab02a5f2e81028b17503aeb>`_
- Catch new subpackages. `19d315a48 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/19d315a48587c1e9798f3271e5b4865cd1b09814>`_
- 0.3.1 `c297cfb4a <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/c297cfb4ab918464baf9df704917b116440e4669>`_
- Add basic documentation on how to get started with fedmsg_meta_fedora_infrastructure `44bcf7c11 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/44bcf7c113dc8d188c4b1197bffa8caa6cb66c39>`_
- Embed the start documentation in the main documentation `2956dff6c <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/2956dff6c60aa62e3ba39d7dfe8d22b4f8b33fb9>`_
- Merge pull request #142 from fedora-infra/start_doc `d18f5e8ce <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/d18f5e8ceda77732e490cd54a74bf62a8bdcf495>`_
- Handle ancient ansible messages with no userid. `8305e290b <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/8305e290bd8d896fbd10fc598e5f46c6d14e289c>`_
- Merge pull request #144 from fedora-infra/feature/legacy-ansible `c2ae68bb0 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/c2ae68bb068db5571fdfd15e525232630384d418>`_
- Handle other kinds of pkgdb status updates. `5b8c5345b <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/5b8c5345b1b365ded1ac583d768a2f753c7e3454>`_
- Mark these pkgdb examples as Legacy `dbb15f79e <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/dbb15f79efc9fcea6468f60c74c1b268c53db355>`_
- Handle ancient koji messages that do not have tag info. `c71f146fd <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/c71f146fd13ae77083f4401a77e7f6a1a01e38db>`_
- Return the full patch for scm long_form. `7f93e7174 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/7f93e71743c8f1c07abf993fb8bf7324432e7589>`_
- Remove errant print statement. `e1aef8055 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/e1aef8055fd3b9a92ff0d0908356d0a87eb30853>`_
- Fix fedorahosted repo links that do not end with '.git' `135eaa4fc <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/135eaa4fc4367cd16176a310126fead81268b222>`_
- Merge pull request #149 from fedora-infra/feature/hosted-git-fixlist `9f518717b <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/9f518717b432d617044b12cd7d34b6b019bcc853>`_
- Merge pull request #145 from fedora-infra/feature/more-pkgdb `75338058d <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/75338058d8431dce292402bba9dddd1ecdeb4a47>`_
- Merge pull request #148 from fedora-infra/feature/patch-long-form `50d2e38d5 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/50d2e38d54cde33bc32015845aa914ba05676947>`_
- Merge pull request #147 from fedora-infra/feature/legacy-tagless `4a05f88a9 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/4a05f88a9295309c1e1ed0336ad576d076f12755>`_
- Revert these at @pypingou's suggestion. `13661ec89 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/13661ec8988d9d82a238883c968897aa02cd93ef>`_
- Merge pull request #146 from fedora-infra/feature/pkgdb-legacy `d2a61a143 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/d2a61a1439d9067d3c61d5315f01aba14e0d20c0>`_
- Handle enhanced bugzilla messages. `d0896ec55 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/d0896ec55c7cb775c924d3c79e943f418f634ea3>`_
- Merge pull request #151 from fedora-infra/feature/enhanced-bugzilla `30436b137 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/30436b137e47229a5a399db432cdf2d75119ad5d>`_
- 0.3.2 `154b44808 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/154b448087765d9d7291fd572ed1c8cc019fa309>`_
- Fix doc building. `216283439 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/216283439b2084c472b7474d997fc3d745760892>`_
- Merge pull request #152 from fedora-infra/feature/doc-fix `3a27bd980 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/3a27bd980b0595ca79ca396fd65e0a0c66e3e480>`_
- Adjust the cnucnuweb processor and rename it to anitya processor `f56f91a31 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/f56f91a31d88e70d97dca1262224abdcd57ee97d>`_
- Rename the cnucnuweb processor to anitya processor `b7b75444a <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/b7b75444a8abad43f32a2049cc204c83c7fa4345>`_
- Adjust the cnucnuweb unit-tests for anitya `9a8c23cfb <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/9a8c23cfb82d186e5d8c4ce512080a5645c7d0df>`_
- Rename the cnucnuweb unit-tests to anitya `cc2d84ec4 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/cc2d84ec428aea8b110836c89202c9b85d322494>`_
- Run the anitya unit-tests `3694ba826 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/3694ba8261fcdbdd0316254dd691f1f5f1c79ac7>`_
- Use the anitya processor instead of the cnucnuweb one `3e4e8fd30 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/3e4e8fd303186bfaf787dc8a58f9d1cd5e864443>`_
- Merge pull request #153 from fedora-infra/anitya `c8cee4658 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/c8cee46584fd613b58e5a26860c8a2428794360e>`_
- Add processor for Koschei messages `5ce91f4ef <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/5ce91f4ef9ec4cc5dc095289504c255a4d4b49ef>`_
- Test for KoscheiProcessor `01c04bd53 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/01c04bd53c9fc2d819662118bcf6fb17ec750fcd>`_
- Fix out-of-sync docstring `336fd4665 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/336fd46656c8a45b5055a5c641166f8f56de96d9>`_
- Adjust the anitya.project.map.update to reflect how it looks in reality `e116f64bf <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/e116f64bfc17a71fbd0f5841d39a9277407f4f8d>`_
- Adjust the anitya unit-tests so that the example messages fit the reality `036ac065b <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/036ac065b8ea608bfacf1ab8d8cdd44a2eac1544>`_
- Add logic to support removal of project mapping in anitya `bbeabe08f <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/bbeabe08fbe1fe00e515fab895b96e89807cfaae>`_
- Add unit-tests for the removal of project mapping in anitya `2457e6f44 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/2457e6f44a2cfaba6f5e6c703736762fc542a375>`_
- Adjust the unit-tests for the anitya.project.remove messages to reflect the reality `0db4a3cc5 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/0db4a3cc574c7bd6f13a40a0508e0d59b080ac65>`_
- Remove build_task_id and repo_id fields from the message `3eb169c07 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/3eb169c07815f9d1c0cfe4bd88b3e848adbe8736>`_
- Add subtitle for transition from ignored `61283c5d6 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/61283c5d6cde3711327b2bb64c83ee9a299d429b>`_
- Include repo and koji instance in subtitle `e45546a5e <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/e45546a5e24da7160c151f5a89075f5088d43e77>`_
- Merge pull request #155 from msimacek/feature/koschei `129c4bf2b <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/129c4bf2b74ccab93dd99dde4a9dd72afec6fc69>`_
- Set the right topic prefix for anitya. `7cc7f8d07 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/7cc7f8d0725f358355cd160d4ce0bceac0840eab>`_
- Change the example topics. `af991d628 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/af991d628638458be0e32b6bcb83162a917614ae>`_
- Get fedoraproject emails without having to query fas.  Fix libravatars. `fc39cf40c <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/fc39cf40ceb9ae850a470ffa07cf6e831abeb01b>`_
- PEP8. `12ccf915a <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/12ccf915a14ffcd59ab4bde2cb54ba45059f6ea4>`_
- Add a non-fedora user to get avatars and usernames right. `bdead3c90 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/bdead3c9091506bfdc771b8d50790c85ad4a329d>`_
- Merge pull request #154 from fedora-infra/anitya `0e94efcd2 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/0e94efcd20c408e225c487e1020a987310568bc0>`_
- 0.3.3 `fc0d4ddc9 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/fc0d4ddc99ecb3489977ee3442cc318e0e981bcd>`_
- Require a particularly modern fedmsg for building the docs. `4cff9aee1 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/4cff9aee1b735480b9d8e887bbf4f24bbba9a8ab>`_
- Fix doc_utilities. `39d76afce <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/39d76afce8fbedde2fa9dc8353160b208d961a9f>`_
- Merge pull request #157 from fedora-infra/feature/fix-doc-utilities `e44639b5a <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/e44639b5ab80fa9c89111d6957f4a9028c021bf9>`_
- Add groups field to koschei.package.state.change `bd803dd63 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/bd803dd63a4c4175c5dd8ed25b2ad4bbca311122>`_
- Merge pull request #158 from msimacek/feature/koschei `77b94ee68 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/77b94ee6809464db47523cb7a2912be1569cbbf4>`_
- Update the unit-tests for anitya's update message `16e9eda19 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/16e9eda1994c7e2a171f8f4d6a089a54b0a9ae3f>`_
- Fix the anitya processor for the update message `faaee82d6 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/faaee82d68f45cce264e7d869985e914601ae2e8>`_
- Fix the message sent by anitya and adjust the expectations as well `69d060e26 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/69d060e26e5e4c81c9c66473cdc446b16dd28897>`_
- Fix subtitle for anitya, inverted old and new releases `e8664961c <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/e8664961c4d1542457b5d9b9236c9753660e4959>`_
- Add failing test case for #160. `3f92641c0 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/3f92641c047cbabd150e6c7a79584024b68d73de>`_
- Fix #160. `1efc6d618 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/1efc6d6184808c8fe5bfc5d3920f68d0e2e20d7f>`_
- Add unit-tests for a message of update having no "old" version being updated `672d66c9b <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/672d66c9bdc70bc90f76dc0e97717558453fbefd>`_
- Adjust the anitya processor for message having no "old" version being updated `3452e6733 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/3452e6733dadcadd6fb004b45468b2194253c163>`_
- Merge pull request #161 from fedora-infra/feature/more-pkgdb-fixes `41b24ef89 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/41b24ef899d426bf1779aa2471bc8de276d7bfda>`_
- Merge pull request #159 from fedora-infra/fix_anitya `2b6bc5fe0 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/2b6bc5fe0222f83ff709cfd29291db5c9a78af33>`_
- Have anitya re-use pkgdb's icon for now. `e3be0f1d5 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/e3be0f1d581e13e4b9b8f80148c1ab669671c15b>`_
- Merge pull request #162 from fedora-infra/feature/anitya-metadata `82d007fb9 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/82d007fb964127070a3c972fc8d6d7175a7174c5>`_
- 0.3.4 `62897a2d7 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/62897a2d786d35c8c091836fa578a47b299a2ea3>`_
- Handle legacy anitya messages. `d052cb001 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/d052cb001dea8a7ec8766221ebcf27420b2de0d8>`_
- Merge pull request #163 from fedora-infra/feature/anitya-fixes `e117278ed <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/e117278ed8c4df2f3382c579cd3c10e216457b6f>`_
- 0.3.5 `e1378fc0e <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/e1378fc0e8e6ce5c58ce1780491e419002da702c>`_
- Apparently we're not guaranteed to have this value. `3720084c7 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/3720084c7280772a34dff80cff996bce4e6c49d6>`_
- Merge pull request #164 from fedora-infra/feature/yet-another-anitya-fix `4d0486963 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/4d04869639fea1fe106ddd737a2666c6d388a8e5>`_
- Add unit-test for pkgdb's message about monitor status change `92e377a87 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/92e377a87ed20ca9d156a0a59555882bc16c433f>`_
- Adjust the pkgdb processor to handle the change in monitoring status `6d0f58fed <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/6d0f58fed357f528daa6a68356d1fe1eb5ade4ce>`_
- Remove trailing slash on pkgdb objects both in the logic and the tests `13a363f40 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/13a363f40aa5d18ace71cf6f2f1ffe1501186e31>`_
- Merge pull request #166 from fedora-infra/pkgdb `cc8274752 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/cc82747520f05ee08abc8329b3421be5ea4ad1d4>`_
- Handle mailman links with and without prefixes. `3f5d6b15e <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/3f5d6b15edbf63f0bdcbcd9d06c761113b839b5f>`_
- mailman:  convert emails to fas usernames where we can. `ce35a7abb <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/ce35a7abbf810b1e88bfab0221da81f9ce557410>`_
- mailman:  No longer chop up emails into usernames. `146235413 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/14623541345dd598785b9271b89b539c6d54d0ab>`_
- Merge pull request #167 from fedora-infra/feature/mailman-fixes `2328588fe <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/2328588fe93f14c161eda76c360d52bb6e849204>`_
- Move fas tests out into their own file. `d77079aa5 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/d77079aa538c0e2da40356fe74ba30e1c3c763c8>`_
- Add fas tests that actually cover current messages. `85c2d7e4f <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/85c2d7e4fa33a0a8fe8a405b1a18879f9d2ce9fa>`_
- Merge pull request #169 from fedora-infra/feature/fas-fixes `50e9715d0 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/50e9715d0188acb933f18de03eb404323383a68d>`_
- lookaside: Dehardcode some assumptions `9391abfee <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/9391abfee6bd02fa499c81dd4a14cde8e18915f2>`_
- Merge pull request #170 from bochecha/feature/lookasidemsgs `526d28373 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/526d2837387265ee82dc430ae2cce233d4dfbdcd>`_
- Handle anitya's fedmsg message when an admin removes a version of a project `df274699d <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/df274699d5ab967e81157b8fb2ce4521be07f496>`_
- Merge pull request #171 from fedora-infra/drop_version_anitya `130ee11e0 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/130ee11e071bcfbfa3ff2f4b97647f8e654c4649>`_
- Clarify the purpose of the anitya.project.add.tried message. `8e9fef33a <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/8e9fef33ae422534fe07d921331d29a97835c232>`_
- Fix test failures for conglomerator ordering. `690d1182b <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/690d1182b0a6b8c273b0c06faa4af07dfc8d24ce>`_
- Merge pull request #173 from fedora-infra/feature/conglom-ordering `66a923908 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/66a923908cd2f26b8bc2e0b72a97d20fa12cdb32>`_
- Merge pull request #172 from fedora-infra/feature/anitya-try `0385f486f <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/0385f486fda27f7f8f1073796dc5be090f6cbb5c>`_
- Remove a bunch of the wiki upload messages. `25f6fa69e <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/25f6fa69e40ae5813b7550eef15dc03acb402cf0>`_
- Merge pull request #174 from fedora-infra/feature/new-wiki-upload `681f485e0 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/681f485e04b281e3e607da4a71525bf69069407a>`_
- A BySubject pkgdb conglomerator. `4921a5dfa <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/4921a5dfa49112861a70cfc5e585290dcad40aee>`_
- Reorganize and add two more ACL conglomerators. `af26e8ad8 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/af26e8ad80a549be645bb48eeef2af149bcf7174>`_
- Switch order here. `bcc7f56ba <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/bcc7f56ba5378aae63f8b4f3650a07799bcc5046>`_
- The New Hotness `b50f491d9 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/b50f491d9bc499ac5110c06a3f6671dd57ff8df8>`_
- Possessive nouns. `b6b9a9d59 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/b6b9a9d596c555db9994371934358dad14dc2400>`_
- Add forgotten koji task states. `d7eb88edd <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/d7eb88eddbb12257b34a309937933ea1f3d9279e>`_
- Merge pull request #176 from fedora-infra/feature/hotness `b05104234 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/b051042347fdb61ff59add69fc73cbd462a8239c>`_
- Merge pull request #177 from fedora-infra/feature/pkgdb-conglom `9a56d0d69 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/9a56d0d69ddb5c46cfecf9cf50d922a4fe068c25>`_
- 0.3.6 `4257c1a44 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/4257c1a44e6706a0cb0b1539f096077e333a99e5>`_
- Distinguish between these two anitya examples. `728f1e3b5 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/728f1e3b58aad49d66b19728ff4585f65b212f77>`_
- Typofix. `0d15c4c83 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/0d15c4c83f1dab6dd21c6910419d1a10a37d5be7>`_
- Merge pull request #178 from fedora-infra/feature/anitya-de-duplicate `001d0a503 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/001d0a5038f14f665506e9d6512f8586aea2ca71>`_
- anitya is behind ssl now. `0b7bfd039 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/0b7bfd0393a40cbe38f341620b0c420f16045904>`_
- Whoops!  Include hotness tests in the main battery. `1b38710bf <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/1b38710bfbc0e959104421be0d1626c355c20a72>`_
- Point hotness messages at partner-bz if they are from the staging environment. `a6fd536a7 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/a6fd536a7064a472c2d6a98b3197871354d26e7e>`_
- Point stg koji messages at the stg koji hub. `8984cbca7 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/8984cbca7b8287d3eb3db420fe2fc589a94f3c4c>`_
- Merge pull request #179 from fedora-infra/feature/links `ca4f3f678 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/ca4f3f678c5695f7b7efc8631ff35911a1dadadd>`_
- First pass at mirrormanager message handling. `232b817d0 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/232b817d016872996251ea7feb4459110f9ec401>`_
- netblocks messages. `2308e08f2 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/2308e08f27a9388fd956bdd1d260f7ee6ff09594>`_
- Fix string comparison in the fedimg proc. `2988d50cd <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/2988d50cdef4a2c617f20817911826f2f7863f0e>`_
- Merge pull request #181 from fedora-infra/feature/fedimg-comparison `d936eb60f <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/d936eb60f8eb83a9e03ee7bdc7d795fabb74d43a>`_
- Merge pull request #180 from fedora-infra/feature/mm2 `9bdc8293a <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/9bdc8293adb7928cf91fb80dcecd621c259cc57e>`_
- 0.3.7 `7b06763ec <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/7b06763ec4f1526c6b2ce96430864fa289cfb36d>`_
- Add support for the messages sent by anitya when the admins delete a distribution `0f1a7f1d1 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/0f1a7f1d1863939760f81f21d4af5c458d376355>`_
- Fix up topic in anitya's tests `fd54958e4 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/fd54958e4484248f8f08f63bec571b6b26305d52>`_
- One more adjustement in the anitya's tests `4de012eb2 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/4de012eb25dd574e99671fd8daf80ebf032072b4>`_
- Fix topic for the anitya tests `f8f4e5295 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/f8f4e5295670748e4c14627d9bb5afbb78b681a5>`_
- Fix anitya's unit-tests `f1e55074c <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/f1e55074c4f56dfc664da4443b25177accb6d6a1>`_
- Merge pull request #182 from fedora-infra/delete_distro `34bed947b <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/34bed947b591bdb6c646ff9fbd9ae04b9a2d9b97>`_
- 0.3.8 `5e2791f74 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/5e2791f74b3ef0b9dad193cc39c4e5422cc33289>`_
- Add and test the second kind of hotness followup message. `2dd8a3029 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/2dd8a30291c2eda3ab8e6290daae0c5d537a1d34>`_
- Mark a test as Legacy that should have been marked so a while ago. `4319119b4 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/4319119b49138590d505a1b32a022083769076af>`_
- No longer stuff package owners in msg2usernames for pkgdb. `1389de4f2 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/1389de4f295823cae23d60227e32d1f75b3e58f6>`_
- Merge pull request #184 from fedora-infra/feature/hotness-followup2 `cac1a95e5 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/cac1a95e5ef3da2edcb2e1fe3bd6420730dd11f4>`_
- Merge pull request #185 from fedora-infra/feature/pkgdb-usernames-kludge-removal `53443d205 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/53443d205f064269adae20db6c74b96f97f31b3e>`_
- 0.3.9 `f4ded79be <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/f4ded79be7b568d1e1b12778b28563e0af63c584>`_
- Handle Fedora Atomic ftpsync links. `882c623bd <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/882c623bd98f9572612899c85bcbbabb91e5f879>`_
- Merge pull request #189 from fedora-infra/feature/atomic-links `5f4357368 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/5f4357368d8009ee3c45fb8e3625378fa8ca627b>`_
- The summershum icon moved. `77f01db46 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/77f01db4623d2b894b28cbfc4243eb07cbeadfa9>`_
- PEP8. `14008cf14 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/14008cf1440133e7999538302e90b8b082d37d94>`_
- Handle hotness.project.map messages. `916876f53 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/916876f53d5601b2dd202eb31172018b3331bd03>`_
- Merge pull request #191 from fedora-infra/feature/hotness-mapping `7c767a849 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/7c767a849f1763d2a044eb4ed017c383cee45889>`_
- Merge pull request #190 from fedora-infra/feature/summershum-icon-change `78b6f5e2a <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/78b6f5e2ae3757191ef8c51597fb1a95ec154c38>`_
- Find out the package concerned when processing admin.action.status.updpte `69613068c <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/69613068cc12341ff832ee1386c6f4d67d82d361>`_
- When returning the list of packages, cover the new branch request messages `68b3caf71 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/68b3caf71d410a85a3f25ddbeba94201b1a3dee8>`_
- Add the explanatory message in the human readable format `536153367 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/536153367bacf54083cb43aed4b1962aa66dc487>`_
- Add a new test: an update message for a new branch request that is denied `e13a84d5a <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/e13a84d5a3f90aada480cc730b91fbba48225164>`_
- Merge pull request #192 from fedora-infra/fix_pkgdb_for_admin_actions `0b4327faf <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/0b4327faf081c862c4ee6418df72224e4f7d3de7>`_
- 0.3.10 `036ee5bbb <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/036ee5bbb6aafcf2808b563df7fa19878b98d8a6>`_
- Create test to elicit the error from #193. `2fa9cb4e1 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/2fa9cb4e1670475cac0eab0e3fed99511b5bf1e8>`_
- Fix #193. `65270ecd1 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/65270ecd1d6a8c4b68778711746561fbf36b0621>`_
- Merge pull request #194 from fedora-infra/feature/fix-pkgdb-messages `15d0a6c7a <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/15d0a6c7ad9bb0efb316898b619b82ed7a721543>`_
- 0.3.11 `ace76a125 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/ace76a125718fe28d0e2e95d39bd768ead5190fc>`_
- Move bodhi tests to their own module. `6ff109049 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/6ff1090492c0923e351bced438f7837fa7b2e616>`_
- Handle bodhi.stack.save messages. `fba701bba <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/fba701bbaf070f96b496ff1898b11b94cb6c4ee4>`_
- Handle bodhi.stack.delete messages. `529620de6 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/529620de620c58678c0b40906c976cc7dcd3e01a>`_
- Handle bodhi.update.edit messages. `bb945a037 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/bb945a037d621fa7685f2ce64ed2b43622229818>`_
- Handle new sigul messages (via koji). `442be7de2 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/442be7de22adef9cd8121bab21e4a0d042d2d0c4>`_
- Merge pull request #196 from fedora-infra/feature/sigul `6b7f2cec2 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/6b7f2cec2b23b84097ed0f31219909c4efcfaf5d>`_
- 0.3.12 `2cf84d830 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/2cf84d830016ea9f44830468a678ec786809a4a7>`_
- Handle bodhi1 and bodhi2 buildroot override messages. `1e4e9ded7 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/1e4e9ded73afed97b4b19756d5b30812fd966aeb>`_
- Handle mashtask and update.complete.* messages. `d67d0bb9d <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/d67d0bb9d80e79fc1602988421a13afc6923fafe>`_
- Handle bodhi.update.eject messages from the mash process. `52cd572a1 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/52cd572a104bbaf05de4be4e14b8f858d11faa52>`_
- Mention the sigkey in the rpm.sign subtitle. `82797fb70 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/82797fb701a80ada5ab902779a05b25e97695fa7>`_
- Merge pull request #197 from fedora-infra/feature/sigkey `08e02b792 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/08e02b79265767b5055b9b00297794490b82fdd6>`_
- Merge pull request #195 from fedora-infra/feature/bodhi2 `4780ce209 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/4780ce209043ac2d4fa98a47e58711689350fc94>`_
- Fix tests. `aa2753037 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/aa275303744c3b06029a0008b78290244547959d>`_
- Merge pull request #198 from fedora-infra/feature/more-grouped-attrs `9804090f2 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/9804090f24f7187fa1ffe9b1ab867f6b8f92ffbc>`_
- Demote this error message. `39531fd41 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/39531fd4198cd65053e0fe3208784cec106a1210>`_
- Merge pull request #199 from fedora-infra/feature/demote-error-message `88353d4cf <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/88353d4cfc3527e004bd6957e0f61f95255f92f3>`_
- 0.4.0 `6d9b2b801 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/6d9b2b801b25e1baebcbf1eb4f9ee6159516078c>`_
- Handle None at the end of mass branch... ;p `e197b8cfd <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/e197b8cfd08d83c28c6fd0323d09c3f36058431d>`_
- Create long-form output for github events. `aace64d95 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/aace64d95af6270e68e561018a3d55c8beba3208>`_
- Include full irc logs in meetbot long_form repr. `7baa7c9fd <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/7baa7c9fdcdc3093596496a60d354ef96071ac49>`_
- Merge pull request #200 from fedora-infra/feature/more-long-form `57c239cb2 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/57c239cb28c0be043450f1f3aa858bba001317e2>`_
- Modernize these fas examples. `9b66461b4 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/9b66461b49e29d40b58e8047d539456af6828c3d>`_
- Convert one FAS example into a legacy test. `3610f5373 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/3610f5373a7440b523c6ad6fe5d3805c14e2f3ea>`_
- Merge pull request #201 from fedora-infra/feature/legacy-fas `08b066f71 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/08b066f71cfa84571b0da93ecf5c6a525de0914f>`_
- Add some debugging around the fas cache lock. `dceb30b96 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/dceb30b96b2eb53f24ea69b9591f48b204dc9773>`_
- Merge pull request #202 from fedora-infra/feature/debugging `adb030de1 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/adb030de10d6a1d2ba47317de625c235812b4419>`_
- Handle "release" messages from github. `b5de46eaa <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/b5de46eaaac5b193a01fc810d60d074f2c7123db>`_
- Merge pull request #203 from fedora-infra/feature/github-releases `68b366138 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/68b36613875cde28d44472c34a0de7f714e278cd>`_
- Pkgdb dropped the from_branch information when requesting a new branch `fd8dba4bb <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/fd8dba4bb183e88ed80f2b0d0b20306dc47580d1>`_
- Adjust the unit-tests to reflect the changes on the messages sent by pkgdb `aa5dc85c0 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/aa5dc85c08c291fe5f6cd24069aa4ef4a12d5c4c>`_
- Merge pull request #204 from fedora-infra/pkgdb_drop_from_branch `c272313de <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/c272313de337ee7763a2b0986631cbe0466be4ee>`_
- Fix elections messages. `3fec1f459 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/3fec1f459b682ed2b75278c94110b1780ad2d1db>`_
- Convert github.watch messages to github.star. `fbdf5fe1c <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/fbdf5fe1c8d47c13064c4ae9b3e036bcc6a9c656>`_
- Associate usernames and packages with the hotness followup messages. `1e5d95ca7 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/1e5d95ca76f14763a9d38b11b2785e979d5134c4>`_
- Merge pull request #206 from fedora-infra/feature/more-github-fixes `3f31862e3 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/3f31862e3ad71584736649aee8a544c7d0d73876>`_
- Merge pull request #207 from fedora-infra/feature/hotness-users `2dc580447 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/2dc5804477f112c6bf623c1980aec058c361e163>`_
- Merge pull request #205 from fedora-infra/feature/elections-fix `5dad82741 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/5dad82741471a050af66b612b5acf8a6ff346624>`_
- 0.4.1 `bfce43e2f <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/bfce43e2f15c7190ea0ca7d9b8fd8adfdd1cc5b7>`_
- Add a long_form field for message about uploading files to the lookaside cache `86432850d <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/86432850d2a6f631817672a9ac10e7c5526d9eb5>`_
- Fix getting the current folder so that we can call that file directly `e73fe2b97 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/e73fe2b971e543a85b6487b457228f86d10c435d>`_
- Adjust the example patch for the change in cgit version `05e6f1f46 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/05e6f1f468ed481bbf49e06628fa6b445012a704>`_
- Add unit-tests for the long_form format of uploading to the lookaside cache `f980ec535 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/f980ec535d8e8eb348e296b4d87ec4dae14b193b>`_
- Merge pull request #209 from fedora-infra/long_form_lookaside `a37198d07 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/a37198d07a701cab168238ee0f8e9158f4984e16>`_
- Update this test to use a real build from somewhere. `0199f78c1 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/0199f78c1c1c13fa6ea1adea8cf74e0d57e000e2>`_
- Implement a long-form value for koji builds. `3bc8b1cc4 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/3bc8b1cc406c03a53e15e68c231c04c78d72e0f1>`_
- Add a way to disable these ourselves in koji and travis-ci. `aa6808eea <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/aa6808eea64e5a80aedcdd81d2691bd7978fcfaf>`_
- Add long-form values for trac tickets. `e1ec60be1 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/e1ec60be1f562f9faf31f7224ac5ed369ce88559>`_
- (anitya) Substitute Fedora package name for project name if available. `c99580a13 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/c99580a13a8268853b51f73193effd40ee3de5bd>`_
- Be on the safe side. `e964f8a9c <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/e964f8a9cf884486e64786748ea527bdc032ebad>`_
- Merge pull request #212 from fedora-infra/feature/anitya-sub-in-package-name `97573944f <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/97573944f7e9e69fcefdebb243b18b6352ee3b65>`_
- Merge pull request #211 from fedora-infra/feature/trac-longform `94a38f832 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/94a38f83291f794b6c1fb8e3abd065829b9af6ff>`_
- Also test longform for failed builds. `67c5fbab0 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/67c5fbab0335e822b670e4b379f0a7a020977ed4>`_
- Also test longform for cancelled builds. `9bab7ad7f <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/9bab7ad7f25863d84d3c2b686e2a7e4f7b706b6f>`_
- Merge pull request #210 from fedora-infra/feature/koji-longform `c60343c09 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/c60343c091d221cfbdef64d3b47e793f53bd2fed>`_
- 0.4.2 `900b4a596 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/900b4a596867d7c09b6fecd85353b40d010290ed>`_
- Comment out the buildsys cancel long form test. `f50eda651 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/f50eda6519a76f8eacf8e681e2b41e831c7ff7b6>`_
- Be more careful with these timestamps. `64f6116cf <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/64f6116cf59a0eda0fab1ff1a709ae8fe804cb7a>`_
- 0.4.3 `4bbd5b245 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/4bbd5b245314d6705cab494d68598eaf152db2d9>`_
- Make github longform tests conditional. `4f46090dd <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/4f46090ddb15c676b51b5b8537220612349b6a68>`_
- Move zodbot tests to their own file, and make the long_form part conditional like the others. `0a99a6226 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/0a99a6226856c77ec35eb18a9e12eda7fa0d69b0>`_
- Merge pull request #213 from fedora-infra/feature/more-longform-conditionals `b030cf966 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/b030cf96603fd6117874814c2f04dab31dcb0b6f>`_
- Don't return prematurely if parent task is still open. `1f80bf7c2 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/1f80bf7c2e666378f23ebe5c83d5e1222142c3c7>`_
- Merge pull request #214 from fedora-infra/feature/koji-longform-fix `fd9cea78a <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/fd9cea78a2eeb68ffc91791ef224d254fa414e1e>`_
- Handle case where result never gets defined. `727bbe1c7 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/727bbe1c7085bd0a7e32ae2afdb75461328307e9>`_
- Add new copr fields to the docs. `d7cb97119 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/d7cb97119ec87d6e2576779f0ad9cd8f17b63fb0>`_
- Adjust copr.end subtitle to indicate the version of the build. `186811dac <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/186811dacbf3b268240b31d927236d58716df024>`_
- Add a long_form representation for copr build completions. `7488a49e9 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/7488a49e9d1df4c5f5c73a53bd6daa77228ab16a>`_
- Add a build failure test just to make sure we have all the bases covered. `b4eb0807f <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/b4eb0807f6855a14028606669c344ff890f4bce3>`_
- There is more info here now... `d8f8e3713 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/d8f8e3713a7ba091d2e2374d39d17732cb0839f8>`_
- Add a link to more useful logs at @danvratil's suggestion. `0a46fdd69 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/0a46fdd69e86884aa4ac00de06eae58adf54151d>`_
- Also link to root.log. `dd1c085a8 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/dd1c085a8698e19b9ff5da3b43f6c8ea5e234a49>`_
- Oh, and of course, https please. `4a15d69c5 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/4a15d69c51a808fb4ad9973bf9e7c5b600731961>`_
- Merge pull request #215 from fedora-infra/feature/fancy-copr-messages `7367a5f53 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/7367a5f536ee8c1b569b15ace59115684948b3f8>`_
- Merge pull request #216 from fedora-infra/feature/koji-longform-testfix `a223aa0e2 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/a223aa0e23337fb96d05577af566f5d5dd7e504c>`_
- Added Github Page_Build Message Handler `587bd3275 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/587bd327563465d71fe74575a663c2b207cdf448>`_
- Merge pull request #217 from Ghost-script/page_build `b88644e06 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/b88644e0614188ccce6edc4d2db428caba805d0d>`_
- Added Github Tead_Add message handler `1fb35abab <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/1fb35abab91ac60d09a87533a65de714d474eec1>`_
- Merge pull request #219 from Ghost-script/team_add `f6f593bd7 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/f6f593bd7fb4d483f4c297cb1f19ae6acdf5606c>`_
- Add processor for new karma messages. `c018104f9 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/c018104f9a13cd052b7875c535935ed9ec5e6e4f>`_
- Use FAS openid libravatar first for git.receive messages And porting scm tests from __init__.py to scm.py `45c2f47d1 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/45c2f47d14a610b4e736eadb8fedac91e7ed148a>`_
- These should be here. `94ece2b33 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/94ece2b3381b23846870484f57e2d06cb2a1908d>`_
- Merge pull request #221 from Ghost-script/openid_libravatar `49e3df842 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/49e3df8421549b59d2f843123427cd0540c82fd2>`_
- Add icon url for fedimg logo. `77f83a329 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/77f83a32964258644930e9a8734cab9299debbb2>`_
- Added message handler and tests for Github member (added to)/(removed from) messages `4f747e0f3 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/4f747e0f39b26529670d642d03496e05b1d5e814>`_
- Merge pull request #227 from Ghost-script/github_member `f50e03724 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/f50e03724e1f8ccdb1e16f0a3dcdfd13d24e5377>`_
- Merge pull request #223 from fedora-infra/feature/fix-conglomerate `738d431ea <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/738d431ea1c2faec67f2837bee54853926fbfe35>`_
- Merge pull request #224 from fedora-infra/feature/fedimg-icon `ef48b3a85 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/ef48b3a85873fa297f447cb34411e9c3f17c7c83>`_
- 0.4.4 `eb6b92dfd <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/eb6b92dfde4de6aea8f7046ae501d53bb3c41028>`_
- Adding Anitya tests for new version of packages detected mapped to multiple packages `0f1ae6b0d <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/0f1ae6b0ddd5415a9bac8b8e7d44bfde7b4539f9>`_
- Removing N from the list of values passed to list_to_series() function `6684e7e60 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/6684e7e6021487db3ddf1856f21dcdfa74f159ad>`_
- Merge pull request #228 from Ghost-script/anitya `775595942 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/77559594284e461ad058bbe3d77010aa82045020>`_
- Merge pull request #222 from fedora-infra/feature/karma `44e5bf4ee <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/44e5bf4ee80439f553f3fa4bf2b33e439fcb657d>`_
- Add tests and implementation for new meetbot line items. `6a96132c4 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/6a96132c4358d89947bc050ddfac3c625da293ad>`_
- Ignore koji longform tests if koji is not installed. `e2b53ef44 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/e2b53ef44b7d04d45acfbecdb3098d2360d255b1>`_
- Merge pull request #229 from fedora-infra/feature/halp-items `02bd9406b <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/02bd9406b73b686643b899785182ed6b150b1604>`_
- Merge pull request #230 from fedora-infra/feature/ignore-koji-longform-if-no-koji `83aad3c45 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/83aad3c45b25c67c7804c81a92874955dcaaa591>`_
- 0.4.5 `23dece4ef <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/23dece4ef26b2e5d4e8d75429512ba7ffee6139a>`_
- (meetbot) use the agent's name where available. `22b9d8280 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/22b9d82800db58ba860afad308b7ae780fea96d3>`_
- Merge pull request #231 from fedora-infra/feature/meetbot-tweaks `ad46e8983 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/ad46e8983eb5844522b25513bdda9053d317c817>`_
- Add more info about why karma was given `cdeaf8070 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/cdeaf8070bb58809f725ad9bf6d367724339185a>`_
- Merge pull request #232 from fedora-infra/feature/karma-tweaks `c8ca14c43 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/c8ca14c4304c2d3765af3d10c5b9b363579cb6d2>`_
- Shorten git commit emails if they have already been seen. `452eb15ec <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/452eb15ec42e093cb4ecf9cbe477885d23c6cfb4>`_
- Merge pull request #233 from fedora-infra/feature/seen-commits `514d67a0d <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/514d67a0dc128afa9b8b433476bb3f46ccd557b1>`_
- 0.4.6 `379251578 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/37925157809c583753982158edc34f4ef021eac4>`_
- Be careful with the trac ticket summary. `6b2373fe7 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/6b2373fe70ed500f557b99e35c50038de2876c66>`_
- Strip out None values from the bodhi usernames list. `bb52a3440 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/bb52a3440c0797bee280c817c85d764552e6c241>`_
- Merge pull request #235 from fedora-infra/feature/bodhi-anon `c9733443b <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/c9733443bd148a64958e900d93917a0bd28251d9>`_
- Merge pull request #234 from fedora-infra/feature/fix-trac-summary `74305eafa <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/74305eafa82ce48ecc1d3af41f7b0b554fb52c3f>`_
- (unrelated) these failure tests are unsustainable.  they change underneath all the time... `9ec4ec087 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/9ec4ec0871b20a090378214ed1209e1fca03664c>`_
- Add long_form for koji scratch builds. `12044f462 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/12044f462eeb28a5b5c8c1ceaaacdd978e33866c>`_
- Merge pull request #236 from fedora-infra/feature/longform-for-scratch `b387c333e <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/b387c333e6077cfb928447886a0d49685fba046e>`_
- De-duplicate subtitles from long_form representations. `312bb250e <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/312bb250e649c45fb6f0be20cbdc4e13cb7d341e>`_
- Merge pull request #237 from fedora-infra/feature/de-duplicate-subtitle `e7bf1014d <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/e7bf1014d3d87a5eee038a783126db2cf104f84b>`_
- 0.4.7 `5e5ef52d8 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/5e5ef52d8cd326eaf28051e73e692f6ce0c503eb>`_
- Add the Pagure processor for pagure's fedmsg messages `f1ce03a90 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/f1ce03a9019cce32cf3a42a03f89a8fdb5ba7ca9>`_
- Add unit-tests for pagure's fedmsg messages `85173cd70 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/85173cd704c795bbdb67f16e2e2d123d10c7bb00>`_
- Declare the pagure processor in the setup.py script `8d6450c9f <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/8d6450c9f4b5762e7c0cd644c063ca8c384bfc3f>`_
- Merge pull request #238 from fedora-infra/pagure `599ac8072 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/599ac8072418912b3fe12bb84bfb7e64032c6249>`_
- Include the comment text in emails about bodhi comments. `576fe8ce5 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/576fe8ce527a317d3f3c4a7baed32355e2afdc05>`_
- Trim end of line spaces `f55d11e62 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/f55d11e626b2a63d3f539f73561366af55d1d675>`_
- Add support to anitya for odd changes `380d8c454 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/380d8c454dd519b4d569aae5ac90a61e83977502>`_
- Add unit-tests for odd new upstream version `6e6d6f37a <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/6e6d6f37a74dc641bd2111018e77f3ff24711e2d>`_
- Adjust docstring to represent the action `e495b3ac3 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/e495b3ac3fa4d7390c869e8756fdbf21d1820180>`_
- Merge pull request #239 from fedora-infra/feature/fix-some-bodhi-things `96f883a24 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/96f883a24b4e53bad1345e415b98e5cdc98bfa05>`_
- Merge pull request #240 from fedora-infra/fix_docstring `945b74ba7 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/945b74ba721b881a91f3bcfc83ddfd441807151f>`_
- Handle new hotness message type. `1ba0b6909 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/1ba0b69090812bd2974a2106b6985ed6c404416b>`_
- These koji tests results are always changing.  We'll need to mock this long-term. `575fdc1e3 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/575fdc1e32088a6008a84a41b83757114d6798da>`_
- Merge pull request #242 from fedora-infra/feature/new-hotness-messages `cdaf5cf73 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/cdaf5cf7399452ebba055d69a218120f55517edb>`_
- 0.4.8 `3b88e2a5b <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/3b88e2a5b9506061faf8d345dab186f13c41bb95>`_
- Be more careful with null task_ids. `1b0a00659 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/1b0a0065924fcfbfd71ef2c1e8dfa17269cd44bb>`_
- PEP8. `fe593bca9 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/fe593bca98a6e7f04aabea1d57f22dc6e6dcf10d>`_
- 0.4.9 `2d7f90f9a <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/2d7f90f9ae53a2f449b6ad785d726ef4fb1b7a62>`_
- Be careful with a null host from koji. `8c28d021d <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/8c28d021dddbe8804584414735036251a15772c6>`_
- Merge pull request #244 from fedora-infra/feature/careful-with-null-host `09e2a442a <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/09e2a442a690935aaf14010d92dbb0e14913c96b>`_
- 0.4.10 `80908230f <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/80908230f39b7cb65bf2c065b2a4a31d964e6545>`_
- Use nice package icons where we can. `d4cf3aba7 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/d4cf3aba7774fe7ac5ea2c820fa83f9607e79c8d>`_
- Remove redundant line. `eb9bdd171 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/eb9bdd1712a757d705badca54d6d8904b07b060a>`_
- Merge pull request #245 from fedora-infra/feature/package-icons `2ea3f0892 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/2ea3f0892ceaf573c4703b15eb3a7cf752eb03f1>`_
- Add unit-tests for pkgdb messages sent when someone asks for a package to be unretired `923b3e918 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/923b3e9186bc0d83c26a21f4417e02ce33d13982>`_
- Adjust the pkgdb processor for messages asking for unretirement `e75627f85 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/e75627f8567b4f3fa96370a078127427fd00d9b3>`_
- Merge pull request #246 from fedora-infra/missing_pkgdb `3aa1190e3 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/3aa1190e3b0046a2d319a8df5ae41615511eea5f>`_
- 0.4.11 `b6b3f80f5 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/b6b3f80f5c59bc0ead82cc3428c779f5d8f87bf1>`_
- Try to workaround an odd variation in message structure. `c7f8dfae3 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/c7f8dfae32c491d8d06077d7e3cafc96454f9e96>`_
- Merge pull request #248 from fedora-infra/feature/anitya-workaround `e89c8f171 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/e89c8f171118b54f4ac94de680a0cdf99c7af359>`_
- Port to Python 3: `e659faa93 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/e659faa93072e4c366f4b5670a247cc9ba59710c>`_
- Merge pull request #249 from bkabrda/develop `0fcd3f770 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/0fcd3f77066ae7df7d168e0d476404f55c74de83>`_
- Add tox config for fun and profit. `3846162f3 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/3846162f3e6da44fc7eae7cb4aefc69aca06dab9>`_
- Add .tox to gitignore. `247d26166 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/247d261666514d6b426b761bdd0e96e9d1c330e3>`_
- Handle bodhi errata messages for #96. `4266f9c82 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/4266f9c82a589fac2c4e6b3a382d4c4a6451ec9e>`_
- Use the errata email for the long_form repr.  Fixes #96. `2b73918a8 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/2b73918a8951815c4f647f0d3da0ba885958c9a6>`_
- Handle new update karma threshold messages. `f7895a2c6 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/f7895a2c6928daff60760533205c9b638231af31>`_
- Merge pull request #251 from fedora-infra/feature/new-bodhi-messages `411bddc17 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/411bddc17f9ed6ca5c8324bce4961cdd889fc1f6>`_
- Merge pull request #250 from fedora-infra/feature/tox `36d9f5652 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/36d9f56524cb11cb0ac90c81047a45d9837a8baf>`_
- Use the bodhi "alias" instead of "title" if available. `917471103 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/917471103052886c971cd54f82818c964f78c006>`_
- Merge pull request #253 from fedora-infra/feature/use-bodhi-alias `c468b2a4e <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/c468b2a4e2329a1e375b7e0ea500f9048bbde237>`_
- Rename all occurences of "gravatar" to "avatar". `3da40c955 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/3da40c95593a4dff41a696732e209148e89ecf4a>`_
- Comment out a perennially-failing, network-dependent test case. `6560390b6 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/6560390b6cc11ab6f6d4ba5b1cd0f597970381f7>`_
- Remove unnecessary lines. `6e6b3f041 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/6e6b3f0416ef1be81fc35e9b107f15634f585935>`_
- Fix typo'd return value. `4df5e94a5 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/4df5e94a5d15971fcc4baca7078d7b4f006c961d>`_
- Merge pull request #254 from fedora-infra/feature/remove-gravatar `a5f06793c <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/a5f06793c4296c6ee9dadaae8053186fc9e91403>`_
- Add zanata processor and tests. `d4c0deed2 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/d4c0deed25fdb724d29d45c0f2690aadf42c95cf>`_
- Merge pull request #255 from fedora-infra/feature/zanata `b6599b694 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/b6599b69401acc2a7d3c52d42d621181f739211d>`_
- 0.5.0 `fde5a7cad <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/fde5a7cadb97ef78f4628039f3788df501df0197>`_
- Test against multiple version of six.  We have an old version on epel7. `3f47d4d88 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/3f47d4d880fc0f20adc4497dc59bf57a93c52d1d>`_
- Be careful with old python-six. `80aa83234 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/80aa8323438fd5da8875c63ee22ca4e27355201a>`_
- Adjust tox to test old python-six. `c637f3b94 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/c637f3b94d2a114a0892a821b737789d954bebbd>`_
- Merge pull request #258 from fedora-infra/feature/six-careful `db1435539 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/db1435539315b020e14710d247333dbef917a6ab>`_
- 0.5.1 `4951cbc1b <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/4951cbc1b496246097bff0d51d48e7d45cb8e740>`_
- Added tests for "fmn.rule.update" `22e424de0 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/22e424de0867369917fd9afe49083bf8bb26aac9>`_
- shorten Fedimg messages `31f79d788 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/31f79d788f4c09cbf8b60671120428d0869e7a00>`_
- remove deprecated comment `ec3e8afac <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/ec3e8afac0071b528edb186b2a5cea249fce9199>`_
- add this missing tmpl line `a7da68284 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/a7da68284846347b07f3a1553a598430d0b12813>`_
- print extra details for fedimg actions when applicable `c78bde198 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/c78bde198a7cdaf4f385af1d51720444180dd91a>`_
- update tests for new extra dict in fedimg output `7e0ccafa3 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/7e0ccafa3732f96c8ca267112321662620ff33fd>`_
- tests: test for fedimg task complete message `14e3abea2 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/14e3abea2e647368e24d035b18c0639240d79107>`_
- Merge pull request #257 from Ghost-script/bug247 `0b1d4ea22 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/0b1d4ea221133d09ab460561cc48855d2226c405>`_
- FAF (ABRT server) processor with tests `f08878aa5 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/f08878aa5ea081379874aa4bc0d7e98e62ac43f3>`_
- Merge pull request #259 from mbrysa/faf `19cc66e50 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/19cc66e50d57957826c6e3951c72705c628a9255>`_
- Sometimes, there is no blog post title. `706fdf3ee <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/706fdf3ee130f6df2b3eec298007368994c99a2b>`_
- Merge pull request #261 from fedora-infra/feature/no-planet-title `1cb772115 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/1cb77211559aab2b9a7318492d9699f5fb131d08>`_
- 0.5.2 `052ce32e7 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/052ce32e7806dcea41defca8051900122270221f>`_
- Try to make admin actions more understandable. `1b7508962 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/1b75089623fa375808a94a4fc3d40f8c06013ac5>`_
- Careful that there is no "agent" field. `1a7485e6e <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/1a7485e6ecc2efdc5fdf82287b5ec828d442694d>`_
- Merge pull request #262 from fedora-infra/feature/admin-actions-redux `68e1febe2 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/68e1febe2f5c48105368181135d608a667e56df5>`_
- Merge pull request #264 from fedora-infra/feature/scm-no-agent `98c969cda <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/98c969cdad1fe123da8344a7937fffa778215b9f>`_
- Fix broken links to election events. `0f2983b15 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/0f2983b1504eef39256185bbeea112f931d33224>`_
- Merge pull request #265 from fedora-infra/feature/voting-link `082a6ca76 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/082a6ca761ccf62f8bae2986d50515a985f04c67>`_
- Handle fp.o addresses. `8fcca42b0 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/8fcca42b02653085ae955482d96d68aaac3aa5a6>`_
- Merge pull request #266 from fedora-infra/feature/fp-o-addresses `8674c71cb <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/8674c71cbc9b9f95ab1fff89bb9ea9176a4e18c4>`_
- 0.5.3 `7b220635f <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/7b220635ffc04b989844d2e2fe5e1031baa5b4cc>`_
- typofix `bd845a291 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/bd845a2913706e1071967ad6a75a5877c528fc17>`_
- tests: there should be this icon here `9c07cba0e <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/9c07cba0e3f7bb930b92a6903a76740c211512f5>`_
- expand on the fedimg docstrings in the tests `0c3293715 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/0c32937156fd8977434be26a5ae156f53893bbde>`_
- oops -- need icons here, too `39d97f5dd <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/39d97f5dd401eb98da85ab71973344d3470dfcee>`_
- tests: add some expected objects for Fedimg `8458c011a <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/8458c011aa79c7a95744dd70b293c8a656c9c1b8>`_
- tests: missed tmpl assignment `cfe9ed6fb <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/cfe9ed6fbdc285dbac5d8fb075ce67f60bb9c18b>`_
- fedimg: refactor subtitle code a bit (fedimg tests run now) `6bc60607d <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/6bc60607da2fa98852b88b553857faba2a81352f>`_
- fedimg docstrings: s/awarded/published/g `3599044af <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/3599044af53c290804baf0ae5057f57ca16aa81c>`_
- Merge pull request #260 from fedora-infra/feature/improve-fedimg-details `8ba23df1e <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/8ba23df1e9f2747544ded447ffba2bb63be784a9>`_
- Extract the "package" from inconsistent admin action messages in a consistent way. `fa2d9a2b1 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/fa2d9a2b1dd29fe3c2636c5bb5c663ef4ac5673d>`_
- Merge pull request #267 from fedora-infra/feature/admin-action-fix `5144e9f1d <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/5144e9f1dc97e6452839f1f87fda5334e9ef4afe>`_
- 0.5.4 `ec1894aa0 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/ec1894aa0542caed2ca88790cabcc34f6b21866a>`_
- Fix syntax errors. `05452d49c <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/05452d49cfeca05ce21bc30f8a6b688f37201076>`_
- 0.5.5 `20f0a7fde <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/20f0a7fdeb22be4d17ae449cfc2a67546333dfff>`_
- Fix pagure regex. `6b451b01b <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/6b451b01b7c2043f92f46ef59349edb2e2a46841>`_
- Merge pull request #269 from fedora-infra/feature/pagure-regex `99da5003c <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/99da5003ce7395c5795e0e53967417d0a8e1d942>`_
- Add arrow for the travis tests. `dc9b9a2a5 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/dc9b9a2a5f2e2aa550d15fca1212bfb0c81bcaa0>`_
- Fix a typo in the FAF processor. `ed6798fb8 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/ed6798fb8dbb0417f4e71f1b24092f57d13304ef>`_
- Merge pull request #270 from fedora-infra/feature/typofix `ac080c469 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/ac080c469da14ac2f08ab33812fb34d09a7cada2>`_
- Update Koschei icon link `4e4f33824 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/4e4f33824bcf993d96c138364dfce871ef935f96>`_
- Merge pull request #271 from msimacek/feature/koschei-icon `aae60812a <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/aae60812a91e86ad8a41bc0fdd583acd085545bf>`_
- Add logic for the pagure's PR.flag.added and PR.flag.updated messages `ea86921ae <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/ea86921ae03d8cf5d485ae0acaccad9c9e41eb9e>`_
- Add unit-tests for pagure's PR.flag.added and PR.flag.updated messages `d37d61010 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/d37d6101014a0bf616c603187f2f85e73a36afa0>`_
- Adjust the subtitle as per @ralphbean's suggestions `86ec32958 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/86ec32958ca0914a1cfd9df52d939775654968a6>`_
- Merge pull request #272 from fedora-infra/pagure_flags `e9b580933 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/e9b580933f744e6cefa43267e59b64e090eb58d7>`_
- 0.5.6 `f614770e5 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/f614770e534b212d4e1ea547d7be50ef9562f044>`_
- Fix problems with pagure processor and test suite. `de7fc3f22 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/de7fc3f2264ab9e39d36070d76fafd83a848b43c>`_
- Merge pull request #273 from fedora-infra/feature/fix-pagure-tests `e5096fd5f <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/e5096fd5f9668bfabc039520a13535bfd116f5f7>`_
- 0.5.7 `d2db17c2b <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/d2db17c2b117dc018dc8e5c4076dfa982690fe11>`_
- Try to avoid pagure exceptions for some unhandled message type. `6488cea86 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/6488cea8620c97a1e6b6a8abc4846bc9dec69ed9>`_
- Merge pull request #274 from fedora-infra/feature/dance-around-pagure `494ca8edd <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/494ca8edda22469554edae6e02e5474d752ea96f>`_
- 0.5.8 `a42949a58 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/a42949a58e0f9bbf637eab05d018e8cc4da6a96d>`_
- Add support for pagure's message about commits `180899ccc <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/180899cccd6950cd8930ac574fc8d13997639236>`_
- User email2fas to be a little more FAS' username friendly `2aac21a45 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/2aac21a45a69fe8f06804eb841472564957e80ad>`_
- Merge pull request #276 from fedora-infra/more_pagure `a7570d83a <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/a7570d83a193f7f7f42e6ff4fde2e342206337c8>`_
- 0.5.9 `fd241927e <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/fd241927ef852979c0ab227d7b508b247be69a7e>`_
- 0.5.9 `28d44e3d3 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/28d44e3d31dfec7a71785fb3049d55d833d0fb16>`_
- Use badge.award 'description' in long_form `dbb892eb6 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/dbb892eb635154ffcd6bb9427436120991c8d775>`_
- Merge pull request #280 from pranavk/develop `1b0cf481f <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/1b0cf481f5f4699bf3deacce07ec741f649a58d3>`_
- Attempt to add titles to github PR/issue openings `649637393 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/649637393f21049120ba80304e528591f9d7bebe>`_
- Fix some syntax errors. `8ac39b3af <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/8ac39b3af0294c53c197d94b214293bc48510ef9>`_
- make tests pass `b2214a082 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/b2214a0820c1c69bd3d0b30e42c409062957c927>`_
- Merge pull request #282 from fedora-infra/issue-open-titles `d438f45d6 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/d438f45d6c2735b787b4761a5c051df8874032bb>`_
- Faster, please. `28170f2d9 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/28170f2d91678a98ee585746ae51e83595a77b13>`_
- Link directly to pagure comments. `633a39bbf <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/633a39bbfe3373eabbd7fbd79494d2d0fbd4c3ce>`_
- Merge pull request #283 from fedora-infra/feature/pagure-links `9d1feda98 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/9d1feda98397ba0ec02b1472354e34e78cd87381>`_
- Update language for pagure messages. `bd3da61ef <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/bd3da61efd0bf6a53c5f0621da3620a935f34dc1>`_
- Merge pull request #284 from fedora-infra/feature/pagure-language-changes `837191f7d <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/837191f7da987ec46885c2affac1ed3f40b902da>`_
- We should return a link... for #link things in irc meetings. `2b0ad74ab <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/2b0ad74ab30231c49c2f282d8308f1c131dca7a6>`_
- Remove spurious print statement. `f1748ed76 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/f1748ed7682c4202bd43e9fcfdad879b23c72563>`_
- Merge pull request #285 from fedora-infra/feature/link-link `8e3e2128c <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/8e3e2128c32f2584b8e6af78787c97391adb9a86>`_
- Update Koschei URL `4e08316e3 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/4e08316e3a206680584bddc36b6f096a71635c9a>`_
- Merge pull request #287 from mizdebsk/koschei `634098d16 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/634098d167c8dc7216094bd2ea65a8d85c7d6ca6>`_
- Adjust the docstring to reflect the test `2aef1ebcd <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/2aef1ebcdba69559e898fcc9f075fb5050cba36f>`_
- Add logic to process messages sent by pkgdb when changing the koschei monitoring flag `554038f11 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/554038f1133f5fdc4937eea864773fc5ec441501>`_
- Add unit-tests for the message sent by pkgdb when updating the koschei monitoring flag `97351e2f7 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/97351e2f7c2b125f3964786201d2585d1e7d4503>`_
- Add missing space to make the link work properly `43664879c <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/43664879ce6af5daf2fc076cf488e281ac76fb70>`_
- Add test message of a failed scratch build with information about the target `ba65c7241 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/ba65c72414c4dacf3a7d330a58939f436c326fff>`_
- Specify the target of the build if we can extract it from the message `a60706c22 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/a60706c22cfa47e26aa4cc48d7b0e1e985af7984>`_
- Merge pull request #288 from fedora-infra/pkgdb_koschei `2a3066914 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/2a3066914f9a5f1fe21fd59ee15f959c876b80e9>`_
- Merge pull request #289 from fedora-infra/scratch_with_target `79294105f <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/79294105ffb9377af3692679c82369a4d091212c>`_
- Careful for x-archived-at being None. `92e77072a <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/92e77072a61a57385df5a40822dd8e32a0d90b84>`_
- Fix grammar for github.pull_request.synchronize `42df2c3d4 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/42df2c3d4b92e108c96c1e3f33d43ee21ca99504>`_
- Merge pull request #290 from fedora-infra/synchronize-past-tense `7a1c74a81 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/7a1c74a81ec1ec1d631e662dffa0a971171def01>`_
- Update pagure comment links. `b23e24247 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/b23e242473d749ed7c1256981d2cbce5dea04ab1>`_
- Merge pull request #292 from fedora-infra/feature/pagure-link `60b33fe40 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/60b33fe4029c5739b8fa6eaaf058c1841324a41c>`_
- Ansible conglomerator (for fedora-hubs) `6a1d55773 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/6a1d55773ea33902cbebd94d3ef8fc5423e7ce01>`_
- Handle case where constituents have been pre-filtered. `e8e760e0e <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/e8e760e0e0361cbf6cffad5133f0db6c57b13b84>`_
- Tagger conglomerator (for fedora-hubs) `6e6202e39 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/6e6202e39804be3ac64db2e8badec5aecb4390ad>`_
- Consistency. `ec985c8d0 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/ec985c8d0f9910f533b0c3f303deaee5cb4673d9>`_
- Remove duplicate declaration. `ef62ab93e <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/ef62ab93e6002fa2f7e35fa495eec2b217ef8ea8>`_
- Merge pull request #294 from fedora-infra/feature/tagger-conglomerator `8a70eb667 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/8a70eb6671567fb37864ef641822310d42f3b97a>`_
- Drop hardcoding of humanized time in the test. `4eb882116 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/4eb882116db88926d8862d2d7702d26227b99d03>`_
- Try to handle all these plural cases. `c55e09523 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/c55e09523adc135b7c79b9e6eecb1374c1775267>`_
- Merge pull request #293 from fedora-infra/feature/ansible-conglomerator `9cf772c48 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/9cf772c48bb68ad4cbf95b77b554f54ec70c69d8>`_
- 0.5.10 `3bc79cebf <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/3bc79cebf66a9c42aaa06cd78aa96941055a445f>`_
- Fix incorrect key. `8e33726e0 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/8e33726e0ca3fa8597d4ea46659d3ff8732377a6>`_
- Merge pull request #295 from fedora-infra/feature/mm2-fix `43f26b3af <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/43f26b3af8563909806193fa934d31ecc443f897>`_
- Remove hardcoded relative time from tests. `435080a85 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/435080a85579bbd79d7ebafcd6f0d2bd3032fce0>`_
- Copr conglomerator. `7c7fdce89 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/7c7fdce89753a77a87e87eebf126d39f11998b03>`_
- Merge pull request #296 from fedora-infra/feature/copr-conglomerators `a4874f254 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/a4874f2547141cde45e338afe614677e69a61a5c>`_
- Protect ourselves from lists. `8ecfad370 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/8ecfad3709de3f94745a7aa37388b8fbccf97a43>`_
- Merge pull request #297 from fedora-infra/feature/buildsys-fix-weirdness `7b82342ab <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/7b82342ab7c8e7f89835d6598346c4b96b1bbbaf>`_
- 0.5.11 `9a2b24c52 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/9a2b24c52160956c1d00b84099e7531e0aec3d21>`_
- Update copr urls `ad8a1092b <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/ad8a1092b759adebf765939a18c1bf9134bc916e>`_
- Fix #96  "in advance of" should read "newer than" `684c98411 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/684c984118c52126154ad4b03bacf1497635a4b9>`_
- Update tests `facff07e6 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/facff07e62f74251c72eae2cea73441c2f3df365>`_
- Be still more careful with this mm2 field. `7a6a3e161 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/7a6a3e161f7f0cff08eaa52b201fe387b9287994>`_
- Merge pull request #299 from vhalli/develop `6d5f2f800 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/6d5f2f800f8fb4a8bab6369e447923bdc21c2e65>`_
- Merge pull request #300 from fedora-infra/feature/mm2-fix-again `883b464dc <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/883b464dcd31fead4391df14a6f5b42b658382f3>`_
- Merge pull request #298 from opoplawski/copr `ec625c4aa <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/ec625c4aa086fd481873f83ed35d718725bf70e0>`_
- Rename this to Legacy so it gets hidden from the html docs. `d9a8a3c0f <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/d9a8a3c0f93fae6e7cb4cbca7fc2e110f06e741f>`_
- Adjust this to match. `c6ad8b491 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/c6ad8b4917f54f13247d444f196ea1ffb45ff075>`_
- Fix for #277 unhandled 'pagure.issue.drop' messages `1f727829a <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/1f727829aeac4bc102a9ceba67a8b826d301f6a9>`_
- Merge pull request #301 from Ghost-script/Fix `7ed111ccc <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/7ed111ccc2804827b10dbd0db48971640b30eb3f>`_
- Handle a case where there is a different nested message for the-new-hotness. `e39da1936 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/e39da193613680d5de9474fdacd2b8061f964c5e>`_
- Merge pull request #303 from fedora-infra/feature/handle-another-hotness-case `57bfb6ec3 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/57bfb6ec38cc01dbad1d250bdf3a3e8546d31121>`_
- Be **extra** careful. `edc7e61db <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/edc7e61db2e4eb02719136c2ebe4c87a0cd4b5d2>`_
- Merge pull request #304 from fedora-infra/feature/extra-careful `0f1f01a9e <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/0f1f01a9e1dc603da537332a341eb7e9f3b217a4>`_
- Update conglomerators for fedmsg API change. `e50a2b823 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/e50a2b823885ac1fe3939979ef52b1900b5a3f5e>`_
- Processor for bodhi.masher.start `4df2b4247 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/4df2b42471886333a9a7946a3f9a04234b23e781>`_
- Truncate bodhi update titles when they're ridiculous long. `055d24de0 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/055d24de0aef5f3fecb8436e22dd8449dac31a98>`_
- Merge pull request #309 from fedora-infra/feature/truncate-update-title `056b867e8 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/056b867e8194036895196670460fe39638ce6112>`_
- Merge pull request #308 from fedora-infra/feature/bodhi-mash-start `181db5834 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/181db5834d733fc699d95c0da9c44a01c0cf19ef>`_
- Merge pull request #305 from fedora-infra/feature/subjective-conglomeration `ef932e552 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/ef932e552740ae7bc2cdc248551684f1d26b3965>`_
- Handle edge-case in copr conglomerator. `f759b6c0c <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/f759b6c0c891fb8d82ac0e960a0a49652870e6ac>`_

0.15.0
------

- Bugfix to ansible relative playbook.  You can run not-checked-in playbooks, btw. `46c82a191 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/46c82a191db5d5e974fdf3ed55645ccae7ce1b0c>`_
- Remove unneeded methods. `7cfb39e74 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/7cfb39e7427e70e2cafd2d6e822cccc5110b9fbd>`_
- Use the badge art as the icon, and the user avatar as the secondary. `c1464952b <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/c1464952b2a131642e45bb4e5f4f099aa29daa21>`_
- Merge pull request #30 from fedora-infra/feature/badge-icons `e610ed014 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/e610ed014b739cffd225ab1585d2efe518dfa1e8>`_
- Follow in the footsteps of fedora-infra/fedmsg#173. `26cbcaab2 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/26cbcaab29f100183e3bc0e1f862abf4b7acadb4>`_
- Handle new git.receive message bodies if they're available. `f18aebe1f <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/f18aebe1f5c3809b4b6259feb8a2f16f17d70d7c>`_
- Support rank.advance messages from the badges world. `6f757311f <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/6f757311f2dec5f449f391a852fb3c9aa5b9a167>`_
- More pythonic! `022e3c27d <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/022e3c27dd3bab327ff84ef4b2ddfcead319b6d1>`_
- Merge pull request #31 from fedora-infra/feature/githook-abspath `610dc7bc0 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/610dc7bc0e520d91e78e3c1668011ae152eb106a>`_
- Add a test showing that this never worked. `ddcaf59c0 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/ddcaf59c046d54ecea680e1613ff861e0928d881>`_
- Fix the ansible relative playbook stuff to make sense and match the test. `5a5541783 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/5a55417836a6efa3037fb208abd43f66b6c47714>`_
- [scm] fix subtitle for older messages without username specified `ad5e2c7c2 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/ad5e2c7c2ecb62ce8496cb8af7fe94e78e4aff2d>`_
- Merge pull request #35 from fedora-infra/feature/idempotency-following-suit `1928d92b0 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/1928d92b0f1dd6a54b1352bc6abee88020a5b257>`_
- Merge branch 'develop' into feature/scm-old-message-bugfix `9f41909b9 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/9f41909b91d16a236061b5d326086e9e611680c2>`_
- Merge branch 'develop' into feature/ansible-relative-playbook-bugfix `946ca3bab <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/946ca3bab2298c853ef62db8edf45ecf82fabdd5>`_
- Somehow this got left out of one of the merges. `bff70ecee <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/bff70ecee6991ba8752b739def768e51f3e55c18>`_
- Merge branch 'develop' into feature/badges-rank `66d0156e9 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/66d0156e9e5a3108e158a42fbcdfa1a8bda845d3>`_
- Catch up to the latest from the develop branch. `b3619e38a <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/b3619e38a19f6ed06fa0cecef6ab4bb7a3bddf28>`_
- Merge branch 'develop' of github.com:fedora-infra/fedmsg_meta_fedora_infrastructure into feature/scm-old-message-bugfix `6aad75e8c <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/6aad75e8c871bd96459c5d257d1a293feee1006a>`_
- Add test suite to cover older SCM messages without username specified `8c01e50eb <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/8c01e50eb0bbcddb0d54d1034fed616162d41b1c>`_
- Merge pull request #34 from fedora-infra/feature/scm-old-message-bugfix `a2f793b62 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/a2f793b62567c4805dff9c9a90e35bb219e7b9bf>`_
- Merge pull request #28 from fedora-infra/feature/ansible-relative-playbook-bugfix `045742bb2 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/045742bb2e1cdcb5bd216f1344281265270fa481>`_
- Check the contents in _get_user. `32b6ce7ab <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/32b6ce7ab95a3ce5a45bf697e05227a78d432a87>`_
- Merge pull request #32 from fedora-infra/feature/badges-rank `77a03320c <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/77a03320c2cf1e503539f2de1ad4bc1e282290c2>`_
- 0.2.0 `460612755 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/46061275597cf51154b6d4345732a5904247848a>`_
- Merge branch 'develop' of github.com:fedora-infra/fedmsg_meta_fedora_infrastructure into develop `ddca35716 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/ddca35716872884d8e6973ce398b4f27edf333dd>`_
- 0.2.1 `2cbc327b9 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/2cbc327b90db28e80e3b4ebde6f746ad1d15c2bb>`_
- Fix another one of these that we missed. `916ca7582 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/916ca75821944d564bcfd5ccc4ded5d200cf057c>`_
- Handle impossibly unlikely datanommer events. `760d9f3b6 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/760d9f3b692dc1af1ba86d310e61eec621fc51bf>`_
- Only return meetbot links when the meeting is actually over. `9bb73693c <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/9bb73693c7005952860f09fda37288762c3fab7f>`_
- Merge pull request #36 from fedora-infra/feature/wat `605950b3d <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/605950b3d8f7f3bf941c36de18015c872a572fbb>`_
- Merge pull request #37 from fedora-infra/feature/no-link-at-start `98ab1adac <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/98ab1adac0318c57a21791f9517554ec936d0094>`_
- Add message handlers for fedocal. `61310888c <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/61310888cfb1d827dfb87cf6ebf7016fd49bdc10>`_
- Update owner to point-of-contact for pkgdb2. `314985840 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/3149858404cb5324e040acbb6fab1ff47661e340>`_
- Handle new package.update message format. `87c0689fb <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/87c0689fb3c589c3c777eae55351abcb7c17f07e>`_
- Handle new branch start and complete messages. `503fb1550 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/503fb1550e23c6b847976b29bc0ce86e4e70a193>`_
- Handle messages for new pkgdb collections. `c0ad7c834 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/c0ad7c834f7e9c701ecca727307047ad77b560ad>`_
- Handle messages for updated pkgdb collections. `500937f9d <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/500937f9d45f4747b2c29c825bac22f54f5eb800>`_
- Support relative delta stuff for fedocal reminders. `7229b93d0 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/7229b93d0698a8becf5736240c9cd97d586c025c>`_
- Link directly to fedocal meetings. `87fd59bdc <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/87fd59bdcb1e0db3cde7396c7475deedffb77f3f>`_
- Nuancier stuff. `31a309ca9 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/31a309ca9b57b1ac64bd66e9c37c232def66a2a8>`_
- Merge pull request #40 from fedora-infra/feature/nuancier `52381965d <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/52381965db4f8637974fde6eb788826ac3f3307e>`_
- 0.2.2 `5dc6e3cf1 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/5dc6e3cf195f3e992e0dcb058d71a2b47f04732e>`_
- Merge branch 'feature/fedocal' into develop `add3992cf <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/add3992cf3b3cea646b15eda2d75f465da4fd30f>`_
- Keep formatting consistent. `4f90fd269 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/4f90fd2698d26954b3cb0ebf351787999e0b4861>`_
- Merge pull request #38 from fedora-infra/feature/packagedb2 `cc9d468f3 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/cc9d468f39c43ef89f6c4d89cb6830099379ce07>`_
- 0.2.3 `bab0c0018 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/bab0c00187b82b1143f5bd63f145ef4cba04e91a>`_
- disable avatar test `5845dae6c <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/5845dae6cf2f666397d0495b914abbd5431fd786>`_
- Handle the new badges message. `cd8973c74 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/cd8973c740bf23c2b09217342387e45a89b9ed40>`_
- For the very first time. `846f90774 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/846f90774515b5905a053b854ed22da665c2dd54>`_
- Merge pull request #42 from fedora-infra/feature/badges-login `770bb4b19 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/770bb4b199190464e95a594949b26e39a02dd14a>`_
- Add the __doc__ trick to the bottom of all the test modules. `5bee972ad <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/5bee972ad7703590c66daf0945dfa75e39df2956>`_
- Fix issue with import (kitchen) and refactoring the code. `7d66afb02 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/7d66afb02c4bc0e862d960c5820bca302c228ab2>`_
- Reorder to install requires `81f470470 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/81f470470cb09c6e441f97bb41111affbc4f4034>`_
- PEP8, refactoring `839979c56 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/839979c567042376446df4c2a00856124cb6cb80>`_
- Remove blank spaces in bodhi.py msg `f0fa59956 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/f0fa5995660481ccfb1ea0d92f94fafa8be14695>`_
- Change in setup.py, sys.version_info < (2, 7) `0df4fcd05 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/0df4fcd05fd066a10607fab7d9e0b29b0239fef7>`_
- PEP8 `7e2e3926c <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/7e2e3926c408dd3da58cb2627bffa3bec7ea6e3a>`_
- Move that docs trick into a function. `10389be00 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/10389be001dcfd4b4f27175a818a1834186b91ab>`_
- PEP8/cosmetic while I'm here. `d214ac277 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/d214ac277d8b3c4fa5d0c1d2dfc4e77b5e08a92a>`_
- Add forgotten file. `c10f0cd21 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/c10f0cd21d7ed4015ac332c162dffca424cde343>`_
- Merge pull request #43 from fedora-infra/feature/docs-fix `9ba32c187 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/9ba32c187e3c75076830d9bab3d69c725d5f921c>`_
- Update bodhi.py `13e07f110 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/13e07f110ee566fdff4146dbf7c01fde641c1a3d>`_
- Update setup.py `3b1eb842f <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/3b1eb842fa0643646a4dcd3915248619c7a6f838>`_
- Merge pull request #44 from yograterol/develop `d899914c1 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/d899914c173790766204e0110bc63bef5a56fa71>`_
- Replace string concatentation with literals `05005c6ad <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/05005c6adbe772ace3f56c652bb5a32f21eeba63>`_
- Merge pull request #45 from echevemaster/develop `a4fcc2fc8 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/a4fcc2fc8c5a8e7f29dd91344b7a16c51971f254>`_
- Make Git icons square `9be80070f <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/9be80070f5a4c392d1f4410065268f17d1a02f35>`_
- Fix tests for git logo change `459e51399 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/459e5139969875e1c08728d90501bb2c989ec100>`_
- whoops `5d60aa18a <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/5d60aa18afac298152c6659882a17befd35fe10d>`_
- Merge pull request #46 from fedora-infra/feature/square-git-logo `b909ef640 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/b909ef64086916d7adc126c5df42087c982fe22a>`_
- Handle old compose branches. `a783a995d <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/a783a995d17a348d1b0b177b300f9c47332392a4>`_
- Copr processor with accompanying tests. `57639b9ad <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/57639b9ad114c185a3665fc82dd7d77d747fd746>`_
- Merge pull request #47 from fedora-infra/feature/old-compose-branches `1f85a8b95 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/1f85a8b95e7efb33b521d70dad01ea40d3d4775f>`_
- Support copr.worker.create messages. `9f8fbccf9 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/9f8fbccf9c68a720b19cc11850b7c147f33dad12>`_
- Merge pull request #48 from fedora-infra/feature/coprs `fa5c09ec2 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/fa5c09ec229e2bd33839ea8cd43ecbd710d7e845>`_
- 0.2.4 `4462b341f <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/4462b341f36a8693fc3f739f38c96a4e2a554ddb>`_
- Fixed docstring for the bodhi multi-build update test `3db4e27c0 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/3db4e27c0dfd757ee2fbae4f5022f3b312574ae1>`_
- Tests for cnucnuweb messages. `8130a748c <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/8130a748c7be938304386934fa5965f7f285fa25>`_
- Test for new version messages. `c23c9d280 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/c23c9d2801b5f2eeb871da20041b84647d96bd1a>`_
- Add instructions to the README. `4d1c8efeb <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/4d1c8efeb41c172701d2a883b672da5c90ede980>`_
- cnucnu processor written to the tests. `3ef6caebf <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/3ef6caebfe6a9f5e5e20d1b6ee01dbff690a653a>`_
- Merge branch 'develop' of github.com:fedora-infra/fedmsg_meta_fedora_infrastructure into develop `8a013f5ca <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/8a013f5caae4f4ae781afe98fd60d87ca735f928>`_
- RFE: https://github.com/fedora-infra/fedmsg/issues/118 `f437dc51d <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/f437dc51dc79dfbb6c94fba1b1b45807e25a638c>`_
- Merge pull request #50 from fedora-infra/feature/cnucnuweb `5dc92b4ea <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/5dc92b4eaf9dd72f2ab19f09ee8bea01b3a7ef3f>`_
- Handle scratch builds. `1626fda81 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/1626fda81eb536684594f18514702ecdf68a2f2b>`_
- Support for epelbeta compose messages.  Fixes #52. `af8511171 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/af8511171a0315c6ddfce3734ab4c073f0935c60>`_
- Merge pull request #51 from fedora-infra/feature/scratch-builds `32154f6cb <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/32154f6cbb3e1dbff57c814f1a57365f80293a38>`_
- Merge pull request #53 from fedora-infra/feature/epelbeta `03ba3c8cd <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/03ba3c8cdf7cdecabc7b9e80010c40acfb7f5428>`_
- 0.2.5 `28bbb0a13 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/28bbb0a13d193d1d7da6c7f0f74232bb25ff442f>`_
- Add meta information and tests for the new messages added to fedocal `4f8a864dc <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/4f8a864dca3294aace306a4a95be6852bd7e0dd4>`_
- Update the pseudo messages to reflect changes to fedocal `544931a19 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/544931a19d3d943f92e93be173973ba86695fc6a>`_
- Merge pull request #55 from fedora-infra/fedocal `1479eb33b <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/1479eb33b19d5ed968d38286b27626651f31cb74>`_
- Use a new location for rawhide compose links.  Fixes #56. `4ca0a55a3 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/4ca0a55a39e12d340cd0d662fa8169310f9e28f0>`_
- Merge pull request #57 from fedora-infra/feature/new-compose-links `87bee86ec <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/87bee86ecd8615f1104938675ed20e20a7cee6f8>`_
- Handle cancelled scratch builds. `6fce5f96a <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/6fce5f96aedd2c05edfd0793646c9a8df433c711>`_
- Merge pull request #58 from fedora-infra/feature/cancelled-scratch-build `2f88e4026 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/2f88e40262b9812d370e8c2c13d1975e309a2e76>`_
- Add tests and processor stuff for new tagger usage messages. `c0c979b76 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/c0c979b763b60476508ca9e7c6cae622ed6b04a3>`_
- Handle anonymous users here. `7c0386c87 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/7c0386c8794ef50091e847f1181ec32a83b2e1ef>`_
- Merge pull request #59 from fedora-infra/feature/tagger-usage-toggle `e05fed039 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/e05fed039eb2e9d358da0389ee5eefa4ecafc72b>`_
- Adjust entry point name to match the topic modname. `981cacde2 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/981cacde25a2a4cdcd5d9fa57e2c63ca737b3ac1>`_
- Distinguish between the primary koji instance and the secondary ones. `733ba3f90 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/733ba3f90b9d942a9ff8d73ec655bb2f72b2b538>`_
- Merge pull request #60 from fedora-infra/feature/secondary-kojis `4bf8d14e9 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/4bf8d14e912c6b564e6518bb8b22cefe21d77dcb>`_
- 0.2.6 `cd4676bd5 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/cd4676bd56ba059eeedb84f2686f99a126d440fb>`_
- Avoid modifying the original message in that last feature. `de02d9e1d <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/de02d9e1dabf5c9818b6b3505e5396f1363aaad8>`_
- 0.2.7 `8ff643c84 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/8ff643c84c90b87eda06a15faed5175b1bff9ce2>`_
- Recover from failing to cache fas. `403838dd2 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/403838dd239d3aee659ae5c12459889b22f97975>`_
- Add summershum processor and tests. `ad2cb5ba3 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/ad2cb5ba3caddbcec93cc6dc3b469c10917ab030>`_
- Merge pull request #62 from fedora-infra/feature/summershum `8ff4d7f1a <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/8ff4d7f1a5e2223ca78d77d91264f870cb550f21>`_
- Merge pull request #61 from fedora-infra/feature/careful-with-the-fascache `0f7c1944c <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/0f7c1944cbb1af65391ef425cd8c0e9e783246d2>`_
- 0.2.8 `61e71be95 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/61e71be957e3c77fb7fb1102315c526f835874f0>`_
- Update to handle new nuancier messages. `285be6abd <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/285be6abd790ff6588e1cdab536024fbfb3c8999>`_
- Turns out that this field might not necessarily be a FAS username... `45e8f8ea0 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/45e8f8ea00bd69521936756dda091e7685e23757>`_
- Merge pull request #63 from fedora-infra/feature/nuancier-heavy `4229bb504 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/4229bb5047016b55d322ca949c5e5dac702f4c12>`_
- Legacy support - old bodhi messages don't have this field. `d5d3ed74f <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/d5d3ed74f34acc85183f9cb8ca1441e568c76e1e>`_
- Merge pull request #64 from fedora-infra/feature/bodhi-legacy `71b0d2a19 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/71b0d2a198df07d1de81fd4291ad7735ad154ca9>`_
- Add links for summershum messages. `4e6b83b14 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/4e6b83b14393afb70432d1fab7c76d2179a15c67>`_
- Merge pull request #65 from fedora-infra/feature/links-for-summershum `e370d3fa0 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/e370d3fa0c4ad7670bfcf8d5f4295097f16d8dab>`_
- Add support for upcoming jenkins messages `7f474516f <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/7f474516f0c9330e6625587dae22d7c893ad5745>`_
- Fix tests. Thanks @ralphbean! `0e824e73c <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/0e824e73cdd9ed314ccbd7761f9cfd7d0863ad69>`_
- correct copyright year `b21b42b00 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/b21b42b00446d5acb71b19d7ebc209392e498c53>`_
- Legacy support - old bodhi messages don't have this field. `8b9fce49a <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/8b9fce49a691b43d689b3d27bb87eb3bde8cb888>`_
- Add links for summershum messages. `e47ed6f3b <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/e47ed6f3ba2b9164d776baed254741acc0cf327e>`_
- Merge branch 'develop' of github.com:fedora-infra/fedmsg_meta_fedora_infrastructure into develop `f04722910 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/f047229101575d77c60e7ff59362c8820f128eb9>`_
- 0.2.9 `fff744d0a <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/fff744d0a481d6e6acb30357d4deba6be8c4135f>`_
- Koji messages should really have a secondary icon. `920935ecb <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/920935ecb4878aca2f6e5328362e19fd1ebf70a3>`_
- Planet gets an icon too. `7048681ad <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/7048681ad561eb349f8d5c620dfd5474d8ac90cd>`_
- Sort out the tagger icons. `a85d5dd6b <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/a85d5dd6b3e15c6ceb6e0e1c2e18accb24eae38a>`_
- Give askbot an icon, courtsey of @ryanlerch. `111ccfd30 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/111ccfd3056ec0f1d68c81a47c5be3d6209d8d76>`_
- Secondary icons for lookaside messages. `5070bc97e <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/5070bc97efca3f06ebb57cab35fdb115c5c0d0fc>`_
- Make the git fallback icon more consistent with the other categories. `59b07fe99 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/59b07fe9991ef4dd9055be443708f5743f25bd34>`_
- Include the package name in summershum message subtitles. `54ca99f52 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/54ca99f520a180d737b629b1c939aecb7123360b>`_
- Merge pull request #67 from fedora-infra/feature/icons `55bf4269a <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/55bf4269ac045ddea995646420644542aad4eeed>`_
- Merge pull request #68 from fedora-infra/feature/summershum-pkg `5bb493442 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/5bb493442979079e84cd31281e09840f9021becc>`_
- Ansible needs an icon, right? `8ad630df2 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/8ad630df2e34230fd6fc487870c132006d3a0dd7>`_
- And this one badge message could use an icon too. `11248bad1 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/11248bad10d2218483b4c5972c0b7e222cfc474f>`_
- Merge pull request #69 from fedora-infra/feature/more-icons `b8f592e59 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/b8f592e598c4a1741d11bf78d96b00ff304088e0>`_
- 0.2.10 `5864cf427 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/5864cf427080d2241ecb8c08ef32757a39b8fd9f>`_
- A processor for github2fedmsg. `11c95c4d2 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/11c95c4d2b9e2ab01a7f621171e07af13da3148a>`_
- Merge pull request #70 from fedora-infra/feature/github `365cf5365 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/365cf53657f3d1088a25514ba14a1fe6283b3370>`_
- Add tests and processor for the new ftp sync messages. `34bfa48aa <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/34bfa48aa5bf931f4b7d51a1bbe38ad69839fa9b>`_
- Merge pull request #71 from fedora-infra/feature/ftpsync `98e7e293a <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/98e7e293a12b155e93ee422ae8e1a524346bf7ce>`_
- The bytes field is actually 'human readable' `1496bbe72 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/1496bbe722cfeb38ec7a26b1b6834da7d9b4d12f>`_
- 0.2.11 `d5cd3bff5 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/d5cd3bff51d66c5fddebda4cac0bd79564472b16>`_
- Need to pass through the config here... `2ff1888a6 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/2ff1888a60fb9051d6e9a0575193ed4825a2f98b>`_
- BZ processor and a test. `3e7ce519f <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/3e7ce519fad93ee5f0ffedadac4881aa6bff62a3>`_
- Handle messages for "new bugs" `410baa648 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/410baa648361795ded8c915b7b96a68a944b8b76>`_
- Correct module doc. `e91840446 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/e918404463f885f9de89ccfae685419325c290bf>`_
- Merge pull request #72 from fedora-infra/feature/bugzilla `b7b94bcf2 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/b7b94bcf2e463413740d2535cc0f3e3fd4e5a577>`_
- Use https for copr-be. `fb4e6249f <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/fb4e6249f1cc560d089badff9166fa4b158d0dda>`_
- https for wiki links, please. `b26b8ca11 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/b26b8ca11e3554f33335cccc137ea5a3d4704c2a>`_
- https for meetbot, please. `f195772d8 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/f195772d89f333210e36a184c496d5f3ffae37bc>`_
- Merge pull request #73 from fedora-infra/feature/https `162d231a6 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/162d231a6bcc370f0503879a3558c8f92bfdb0ba>`_
- Clarify user role at endmeeting.  Fixes #29. `e74642892 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/e7464289233e0993c1d1366ef14a240ea80ead35>`_
- Merge pull request #74 from fedora-infra/feature/user-at-endmeeting `a8b5cff01 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/a8b5cff014d11de6a22cd49245180630739bddc5>`_
- Remove "slave" field from jenkins `fbf3fc841 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/fbf3fc8417dab72d2981545ffb48495a8cf3be9c>`_
- Merge pull request #75 from fedora-infra/jenkins-take2 `ac853fcee <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/ac853fcee2ace23cf08253dd37f9c4fd02016d6a>`_
- Test tagger rank change messages.  Fixes #14. `e0541cde8 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/e0541cde81c6e250e7349f31a3414501202f0a88>`_
- Merge pull request #76 from fedora-infra/feature/test-tagger-rank `413194c36 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/413194c369704c5ca666a821d12cdf4a70a1801c>`_
- First work on the ElectionsProcessor for fedora-elections `ae75f73e1 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/ae75f73e149b19274fa656790ecef3ad733e6123>`_
- Update the elections Processor now that the messages contain an agent `3b4990e72 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/3b4990e72e465bedb3904b8f7e7022fd02780296>`_
- Adjust the __link__ now that the elections is on apps `f602cfbcf <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/f602cfbcf155ba689c279c60c03412dab288fddc>`_
- Manage messages regarding elections' candidate (new, edit, delete) `dc00a61a8 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/dc00a61a83f6e2bd045c780ea63ea0f8f4a74640>`_
- Adjust the setup.py file to include the elections processor `3c6e15edc <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/3c6e15edc6eb6a9cd03153b8c5913706744223b7>`_
- Import the ElectionsProcessor from the right file `843f8cfde <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/843f8cfde54c792f783314ab04d9fe4eaba47aaa>`_
- Fix trailing slash in the link in the elections processor and make it valid python `3c731ac51 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/3c731ac514d80d66de5fab67eab90b65b4cbc21b>`_
- Fix the usernames method `540b48954 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/540b4895441297c52b450fe3b3d2bad8712cc38d>`_
- pep8 fixes to the fedocal tests `831958858 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/831958858577d313258e333ce709136d397f9dfb>`_
- Fix the name, messages from the elections are of type fedora_elections `1e6d8c61e <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/1e6d8c61e2c79dff8fd55310e30491df1a470115>`_
- Fix the topic for editing or deleting candidates (and not elections) `dd27ca13e <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/dd27ca13efdb07e7dc902ec238f418cf4499adf1>`_
- The messages are only broadcasting one candidate at a time, no list `f59ed4b3a <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/f59ed4b3a943f4f57398c979e6f3b0bd8e84cfcb>`_
- Add unit-tests for the fedora_elections messages `77ebbff64 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/77ebbff649639c3703446494787f5d2b61d8a57a>`_
- Link the unit-tests for fedora_elections into the main test suite `03887eaa1 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/03887eaa143a019500d2ec9f252cfaf090c650c6>`_
- pep8 fixes on the trac tests `90a3d0933 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/90a3d0933c65015eb09a1714e5c656851eea0055>`_
- pep8 fixes on the summershum tests `2080bdca7 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/2080bdca77d44c108e05491a0bc0b3e3c939611f>`_
- pep8 fixes on the mailman3 tests `0b0f1a69b <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/0b0f1a69bf756b2a801767462af8e838386d93d1>`_
- pep8 fixes on the pkgdb tests `7e914cc87 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/7e914cc87a1d3d71734fdb6303b8bdb6571fb8da>`_
- pep8 fixes on the jenkins tests `05d3ddb25 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/05d3ddb2569d713532ed6a0adc2850a996d53d64>`_
- pep8 fixes on the github tests `a4e11b75a <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/a4e11b75a9a32b7abdf3db39070cecd50f3d2459>`_
- pep8 fixes on the askbot tests `723536331 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/7235363314355638a55c5c3e80313da08bc4e939>`_
- pep8 fixes on the ansible tests `29d4de8e7 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/29d4de8e76c5161b37e8bcf2a8f8f19dca22cafc>`_
- pep8 fixes on the pkgdb meta file `9ddcabbee <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/9ddcabbee4dd2b8af6e4300ad0d4ffed7f384df6>`_
- pep8 fixes on the jenkins meta file `5da6fcd04 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/5da6fcd04c68ad387949f3b7c411f1f38bf00863>`_
- pep8 fixes on the fasshim meta file `c090e4281 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/c090e42812cb82b379c4f4f1b729337163ed5d30>`_
- pep8 fixes on the cnucnuweb meta file `cbcd846f9 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/cbcd846f9048088ed35966dc475e822117ed056b>`_
- pep8 fixes on fedmsg.d/base.py `8232320fa <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/8232320fa1bb1583919823337c8f143866aecfe3>`_
- pep8 fixes on the setup.py file `363058da5 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/363058da5b6db9e0a001a75afa2c7725536889a8>`_
- Merge pull request #77 from fedora-infra/elections `7dd0715b4 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/7dd0715b4f1b35363223788689fa6384b982f667>`_
- Merge pull request #78 from fedora-infra/pep8 `b787911bf <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/b787911bf1cc638a660558b7d592b116744cfd67>`_
- Be careful with copr messages here. `5a6fbd0c4 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/5a6fbd0c406db5f935b19f927933332bf3ccee43>`_
- Use the new copr frontend url. `7c0830cfc <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/7c0830cfc9cd235b0e3be872423c30d5da80f235>`_
- Merge pull request #80 from fedora-infra/feature/take-care-with-copr `cf64f50d1 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/cf64f50d1c352b25ff0ac81f9f6c11e619abee01>`_
- Retire this one bodhi masher message. `043dbad9b <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/043dbad9b9f63b7f41cb12591490ff52224dfcba>`_
- Merge pull request #82 from fedora-infra/feature/retire-masher-message `e395dd421 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/e395dd42192265c0ccee92d6d188f5218b0ca5e3>`_
- Give fedmsg.meta its own doc infrastructure. `0b866c2c3 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/0b866c2c364e546cfd26e7fd2ec8460e3da27258>`_
- Merge pull request #83 from fedora-infra/feature/doc-split `7181bf8d6 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/7181bf8d6b089033eb6dd5d830cbc860b2117b6f>`_
- Adjust the URL to point to the right pkgdb2 page `c4249c393 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/c4249c3933e22f3f109baa9ed78242f7052cfaf0>`_
- Adjust the unit-tests to use the correct URL for pkgdb2 `91b941e4f <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/91b941e4f89e3b925e3772713d0ba1bfbe08ffc1>`_
- small pep8 fix to make pep8bot happy `e9f5d285a <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/e9f5d285a4eb5dfdf75493df65d9587fc4ccb361>`_
- Merge pull request #84 from fedora-infra/pkgdb2_url `5136e3434 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/5136e343476edc3271ca1ab3cd70ec10bf512aa8>`_
- Copr icon. `a1d296828 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/a1d296828022853ee88e6b9a45fc587d858df68c>`_
- Test that icon, too. `27d0552cd <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/27d0552cdeec1162a81690c32dfa2d080a94c1e7>`_
- Icons for meetbot. `9e733ea93 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/9e733ea93d33238a01cd0f469db5ea0dcd23c76f>`_
- Just to be sure. `e0c087f96 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/e0c087f961caefa974ac7cbad679db62fbf9eb29>`_
- More being sure. `44ab1f881 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/44ab1f88149818bea1e75e2a63bdfaeb239b8644>`_
- Ignore the topics .rst doc.  It is auto generated. `b884d5b6f <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/b884d5b6fd5caba540f45d8dcbfda7084c656d7c>`_
- Update koji examples. `dc1611712 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/dc1611712652219aa5aa5b5d09ce75c498a004c7>`_
- Merge pull request #87 from fedora-infra/feature/update-koji-examples `5822fe792 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/5822fe792c4bfef104067d9a89f742482083c2d5>`_
- Merge pull request #86 from fedora-infra/feature/meetbot-icon `672917fe3 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/672917fe32cb8ad32de5355bc152fa39c5282dc8>`_
- Merge pull request #85 from fedora-infra/feature/copr-icon `bba920ec1 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/bba920ec1ac21e82551186dad1ff9e3a87f9c77e>`_
- Fix meetbot topic changes. `903861a4e <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/903861a4eb9838c35dec31fe1681f09bb8f33aee>`_
- 0.2.12 `02f169e06 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/02f169e06e923cc74316827ded14b9ea7544a951>`_
- Processor and tests for FMN messages. `f8aa9b47f <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/f8aa9b47f9c678599a846d0c2c558f7ba31edcd0>`_
- Merge pull request #88 from fedora-infra/feature/fmn `9d693257b <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/9d693257b58d9696ddda3795a1c307a9d88072b5>`_
- Actually add the code for this. `9bce4b293 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/9bce4b293e6ec07a7416c63f62f88a3ed3cbb0bd>`_
- Merge branch 'feature/fmn' into develop `2521946b3 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/2521946b36cc08ed6d42de3ca79e50d610597d96>`_
- Pkgdb: Avoid redirects to URL with trailing slash `de99f5914 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/de99f59142fca006260ea74b2ee0a8ef2c06b243>`_
- Merge pull request #92 from tyll/avoid-redirects `4d9387fc8 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/4d9387fc85f1e984769e5b7426bc31f393f31f98>`_
- Pkgdb: Make package retirement messages explicit `42d30bda3 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/42d30bda3ef9464b0a7917f5b19f927cce4a41a3>`_
- Merge pull request #91 from tyll/develop `80fc3d9ea <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/80fc3d9eaeb067fe3a4f098b65e3225497bcb784>`_
- 0.2.13 `4a838f948 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/4a838f9480912806872e902f941a6a28d89acab3>`_
- Fix .rst syntax. `ff4853a39 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/ff4853a390171e944655b9d564f9ee4ebe41a763>`_
- compose: remove unused import `93ff47576 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/93ff47576d37fc49497f7eac43272c2a76d1a503>`_
- Use https where currently possible `62a9c6cbf <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/62a9c6cbf4ab61cf6e489f9c33c798e4721a5e36>`_
- Allow mentions in bodhi comments.  /cc @codeblock. `ffe34c428 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/ffe34c428ba5c6483c0eb76d428c495f0250645d>`_
- Merge pull request #94 from fedora-infra/feature/mentions `56a3b4270 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/56a3b42705cec5e1c821c93096039c1a99adceb7>`_
- Initial go at a fedmsg meta config for the new fedimg service. `b47fa4205 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/b47fa4205c2d3bc616696cac39a20c2a4dc14624>`_
- Typofix `f4a928d1e <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/f4a928d1e6b8ccae65345d964f967860f9ee18a5>`_
- Add marked up text and tests for bodhi messages. `bc68050a5 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/bc68050a55584ae13763c9375f2b2ee239cb307c>`_
- Merge pull request #98 from fedora-infra/feature/marked-up-bodhi `f8b840b96 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/f8b840b966d89e709f9ba18731d42ff1917a75fd>`_
- Merge pull request #93 from tyll/https `7e364d43f <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/7e364d43f2caeb360dfa2cf65613efe33a597e08>`_
- Allow the FAS url to be configurable. `dfab75e91 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/dfab75e91edc6832e79dfc1f4b8e097f95d66dff>`_
- Use a nuancier icon. `e309fb85d <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/e309fb85d03d540d9d9156f4a9dd107db68323ba>`_
- Cook our own avatar links. `84ba908dd <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/84ba908dd4173e35e93b5094abb0160a8f61a5fb>`_
- Use libravatar. `07a3e0a20 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/07a3e0a20c24c3bb7e12d9fc95864074a53fef0b>`_
- Update the tests to expect libravatar. `de7a296da <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/de7a296da74c612712bb8641c7093584dd08af1d>`_
- Merge pull request #100 from fedora-infra/feature/nuancier-icon `880a12c82 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/880a12c828dee94c30f103a20beb972690241f04>`_
- Show icons in docs. `0a02161f4 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/0a02161f4e33e4e7fd1c9d91d5ca1a68eec73528>`_
- Merge pull request #102 from fedora-infra/feature/show-icons-in-docs `25c003e03 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/25c003e030ffe731c9337bf6cb7b512cb06d05ca>`_
- Merge pull request #99 from fedora-infra/feature/configurable-fas-url `403b005f0 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/403b005f019eadaa41214dd64d2b0e528bc4f9c0>`_
- Merge pull request #101 from fedora-infra/feature/libravatar `78d057b2e <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/78d057b2e949588662cbb864a2396eca59ffaf65>`_
- Remove some stuff we don't need. `9fb656b2a <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/9fb656b2af6646355809ef743a06cafb57821fef>`_
- Make successful status 'completed' instead of 'succeeded' `f75a7711a <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/f75a7711ac6f60bcefd84ebd5c7e9318e64744b5>`_
- Tweaks as per @threebean's comments. `40fd23e49 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/40fd23e49903511bf5a3d85209760a84238bee95>`_
- Author --> Authors to match other files. `e6b19ba0b <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/e6b19ba0b3f01fe6f2217bd61f75052efd5e46c4>`_
- Start writing a test for Fedimg fedmsgs. `bb8590a21 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/bb8590a21cec481d262f3ffb71a90f4f22440799>`_
- Looks like this fedimg test passes `5d6e69df5 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/5d6e69df50b03f0ab959f731b4b55bb9d7826c8a>`_
- Typofix `d282bff37 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/d282bff37a3283e3957da7de4096864880c7700a>`_
- PEP 8 `675bfcc7f <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/675bfcc7fdb7ddb034e709f7944610a32a9317b6>`_
- These things aren't sets. `f69d1742f <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/f69d1742fced458564f66343e735b4f6c38a0ded>`_
- Crucial - declare the FedimgProcessor. `7bd2ce597 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/7bd2ce59746ed4b38e2150f8cbd9bd4d0d42c703>`_
- Run fedimg tests as part of the big suite. `7f3bebc6b <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/7f3bebc6b41386dc8832eeff5b9a555eab364804>`_
- Handle github.status messages. `7b3bad3bb <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/7b3bad3bbfcb86ed9c589ac0e6610585d642cee2>`_
- Handle github.delete messages. `4222b6491 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/4222b649189a20efc3fc7efb6131dc90ff768ad5>`_
- Handle pull request review comments. `72ada211c <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/72ada211c98aa4667be0a226013361822a14f051>`_
- Reorganize the way msg2objects works for github so that it makes more sense. `b118d4e1b <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/b118d4e1b8f8f291b283ddefc946785b5ae4bede>`_
- Fix key name. `b742848e2 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/b742848e2f44f49eebeca755a4dbe3c2e15c3627>`_
- py2.6 doesn't support str.format() without indexes `4d112edca <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/4d112edcacfdf203ff9889f67d02c1b5b090756e>`_
- This should be the image name, not the URL. `ca6b47006 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/ca6b47006b471c952e90a32ced32dc1c5c2dc731>`_
- Support commit comments. `a91f1a75b <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/a91f1a75b4648d394268b5ecb42e92d0d9c50b00>`_
- Merge pull request #103 from fedora-infra/feature/fedimg-meta `90379f404 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/90379f404f95757e8b05f04e1b57ce504cfa42f4>`_
- Merge pull request #104 from fedora-infra/feature/more-github-stuff `329d97cd8 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/329d97cd85a08fe3d4bd917bda2e190efcd1827b>`_
- 0.2.14 `9b4e0e58a <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/9b4e0e58aede0a0da96c44503d0c4d2318d85eb1>`_
- Add secondary icons for some cvsadmin and releng stuff. `fc4d4759e <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/fc4d4759e064e22279f7b8d1ddc66ac832dac8a5>`_
- Merge pull request #105 from fedora-infra/feature/some-secondary-icons `4ca3d5e97 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/4ca3d5e9776accc0c70182b0b55197b8e3e46ba8>`_
- Sometimes, these can exist, but be None. `fa432bff7 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/fa432bff7e9b6712d5dbfd1e93af5f9ebaf06959>`_
- Use short hashes here. `8598913ae <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/8598913aec0cfa58563aaa58bbfd5bd00d821cd7>`_
- Merge pull request #106 from fedora-infra/feature/short-hash `f50709d99 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/f50709d99a863412386e2bed523c0681b573a2a2>`_
- Kerneltest message handler and tests. `8d1b08b83 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/8d1b08b837778aa162321157ca53a05df12de7c8>`_
- Merge pull request #108 from fedora-infra/feature/kerneltest `4be76c72d <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/4be76c72df16430cd6570aa700d7359dc6af7f3b>`_
- Remove trailing slash that are no longer is use with elections2 `6201fe737 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/6201fe7371288c7ecdaf9904d9708cece790d4c9>`_
- Adjust the unit-tests to remove the trailing slash `7a38c4c62 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/7a38c4c62586e93495e4534601070729b5c7736a>`_
- Merge pull request #113 from fedora-infra/fix_elections `87f91f142 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/87f91f142d7237a482a99c3255c1de49b0e14a96>`_
- Indicate success of copr builds. `47e4e4e0b <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/47e4e4e0b24a74de7b08d9724ac3eca5968924af>`_
- Handle case where this can be None. `6415d246c <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/6415d246c189635bb93633a30a77ca709420b12b>`_
- Fix bug in subtitle for pkgdb.branch.start `015d6efd1 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/015d6efd11ec67a51babaa98875d565e33904d72>`_
- Merge pull request #114 from fedora-infra/feature/fixups `7abaad2a2 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/7abaad2a2b371ab9da761524806ca17747074c02>`_
- 0.2.15 `cac2991d1 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/cac2991d1acb6c81cb2d2baf237c99b30dc5725e>`_
- Handle an edge case with github messages. `895dab10a <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/895dab10ab8d1881c75cb53d52cab30afb22603e>`_
- Merge pull request #115 from fedora-infra/feature/github-edge-case `a74c6e9cf <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/a74c6e9cfca33b2e2b084eb6ecdaa9bff8adcd35>`_
- Add meta code for fedimg.image.test topic `bb65093d6 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/bb65093d607cd4be6174412fae0b664cafbf0ac0>`_
- Merge pull request #116 from fedora-infra/feature/fedimg-test-messages `89cf61d20 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/89cf61d20a71dea0cc53fc69dc5645f9a228fa13>`_
- Include the chroot in the description of finished builds on copr `3dcb851e9 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/3dcb851e931a6701da069f43a31509d64097fc9c>`_
- Adjust the unit-test for copr messages to reflect the addition of the chroot on the finished build message `5ba200ff9 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/5ba200ff9b6bfb8e03763f7367294f79febbcf91>`_
- Merge pull request #118 from fedora-infra/endbuild_chroot `f513436a2 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/f513436a2bee9b2be883ece084c8693182b45907>`_
- Hide old pkgdb1 retirement messages from the docs. `7d9c23a1b <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/7d9c23a1ba3066cc0d2aae36e7b172dc8ce68441>`_
- Merge pull request #119 from fedora-infra/feature/legacy-retirement `fc257d074 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/fc257d0743793d04e28392ea17b613b0f0298533>`_
- Add support for github.watch messages. `74fd4f45b <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/74fd4f45bd6ecbb06a6f8510464367c94a4d8649>`_
- Handle both starts and stops. `9fbfe371f <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/9fbfe371feab18a85398f535e1956a647a406b98>`_
- Merge pull request #120 from fedora-infra/feature/github-watch `b65ad6ab2 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/b65ad6ab275bba61f4177980d531d0c70c69a503>`_
- Added Class and Test `ccfea0d56 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/ccfea0d56453babd29e490bfbdad5936eaf6e2a0>`_
- added class for fedora college `c140ff8ba <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/c140ff8bac230a57d3ac5613dd5d5cef633070b4>`_
- Minor changes in file description `12329eeda <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/12329eeda662f78eabd2a64fdf6b5bad5c19f038>`_
- Merge pull request #121 from hammadhaleem/develop `ab6154c59 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/ab6154c59eeba5f3d2bff22434b513253a18019b>`_
- The topic packag.update.status is not package.update `9e852081d <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/9e852081d27a47f2569d1d0a2faa831c6ed9d13c>`_
- Handle the pkgdb.package.update messages `24022da8b <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/24022da8b5664e5ab0755ebd943674548fc75207>`_
- Adjust the unit-test name for PackageUpdateStatus `222f977bf <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/222f977bf16adeda8de14ce2b330fc2533ca615f>`_
- Add unit-tests for the package.update topic `a681f1b1f <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/a681f1b1fea2d5d581b63929c35de63f75b1620f>`_
- Merge pull request #122 from fedora-infra/fix_pkgdb `698c279f9 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/698c279f9d9f601540cdd8ea335849d12040fd70>`_
- Get the tests passing again. `b241d815e <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/b241d815ed951ad49abca8e4144d683dbad96c40>`_
- 0.2.16 `1a8d00b18 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/1a8d00b18ce287e6b1a685611df17630fbaa7300>`_
- add several jenkins statuses `2b7f67a68 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/2b7f67a689413978a2b431382f9c4b8582850a2c>`_
- Merge pull request #124 from fedora-infra/jenkins-try-again `de9a741a4 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/de9a741a4530870eb9377a8ac9891a69992c90fc>`_
- 0.2.17 `edd3fe59e <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/edd3fe59ec84ab9c38248a71aa86e5ceeca1b247>`_
- Fix tests. `3643db6e1 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/3643db6e189965561aea38b6ff286e87fcf4faf7>`_
- 0.2.18 `b46069572 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/b46069572f66b9c9ab8d2661b4fa2d38095e07ab>`_
- Comment out time-sensitive test. `1a8fe7b89 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/1a8fe7b89f6f4f7193740f6bb146f67fb2835c73>`_
- Debug missing topic. `b51dcb708 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/b51dcb7087484c8f6256c76beb9c80cb861f6a4e>`_
- Add missing topic. `6a1bd32d2 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/6a1bd32d2a4d8b228de4d1d910820561e2b1ca60>`_
- Merge pull request #126 from fedora-infra/feature/more-jenkins-fixes `22175af34 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/22175af34a7bd05a43356022c86fbb290ee5424a>`_
- Handle pkgdb.package.delete. `eb73eaf92 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/eb73eaf92d1b43dc1eef57245310fa98b09cfb2a>`_
- pkgdb.package.branch.delete and pkgdb.acl.delete `0df5e488d <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/0df5e488d0624548584c19e7f1d48ab17ae7d125>`_
- Merge pull request #128 from fedora-infra/feature/those-other-pkgdb-messages `c9ab3f9ed <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/c9ab3f9ed679144cf75519ced04d469e06d08d66>`_
- Handle the new pkgdb fedmsg messages `7fa96b37c <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/7fa96b37c8cc2c02e94a3d003cfa19e8f6f3e550>`_
- Adjust the unit-tests to test for these new messages `4dbf902f9 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/4dbf902f9977f8be3b94a11a2031c23a44990b93>`_
- Merge pull request #129 from fedora-infra/new_pkgdb `2b1a61c55 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/2b1a61c5557f55efea04db46efd68763ba6a39e0>`_
- There are case where the `action` dict is not there and case where it is `f9b10d582 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/f9b10d582224e2ef903ba25f6b5aabb1e649d514>`_
- Merge pull request #130 from fedora-infra/new_pkgdb `282e8fff2 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/282e8fff213a24bf57b18998f45f863994382dd3>`_
- Handle pkgdb critpath change messages. `5cb94cdb6 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/5cb94cdb6d80453404004edb28056bbb70093e74>`_
- Merge pull request #131 from fedora-infra/feature/critpath-messages `e273a0c1d <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/e273a0c1d3185b017918c74db1dea0ee03c1f590>`_
- 0.2.19 `53205342c <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/53205342c1de9e9b8e36006dcbe178dc173e2ef6>`_
- Throw a threading lock around the fas cache. `f920b11f4 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/f920b11f4a70832888101ad78757bf8e10540935>`_
- Merge pull request #132 from fedora-infra/feature/lock-around-fas-cache `8578931c4 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/8578931c449f37326145bd9ced4b045fee768040>`_
- First bodhi conglomerator. `179b922d5 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/179b922d553e6a3494e42a757378962814e063bc>`_
- Bugfix. `3ff8ebb5a <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/3ff8ebb5a7bc408eba99abc4e1e839177280cb9e>`_
- Unnecessary.  self.produce_template(..) actually includes this. `82e84ec37 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/82e84ec37e0ae2f1ba0e43145f7dad5f4ea6ea17>`_
- Link directly to copr builds. `19229d94a <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/19229d94aa04dc0cebbac61585d2fc19920eabfc>`_
- Merge pull request #134 from fedora-infra/feature/copr-builds `c616a8a9b <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/c616a8a9b0e5dd4a86c627e858cf20fbb0c32979>`_
- Merge pull request #133 from fedora-infra/feature/first-bodhi-conglomerator `0409486e8 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/0409486e80cdffab570d4fec0f769050fc6ba64a>`_
- Hardcode topic_prefix_re. `dd68205b1 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/dd68205b15586b0969e0269c7ccafac86adfe380>`_
- Merge pull request #136 from fedora-infra/feature/topic-prefix-hardcode `6a918f896 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/6a918f896ec08e4fe373dd2a50a1708c9e724821>`_
- Split that one into two different ones: for testing and stable. `e903f7af4 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/e903f7af404245d2180ebc21d0b57ba9a7418ffe>`_
- Add two new bodhi conglomerators. `8e7ae9ddb <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/8e7ae9ddbe8515f7952edc5dac57f828a0344675>`_
- Re-namespace stuff into a submodule.  There's going to be a lot of these... `247bd9a14 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/247bd9a14b868a0289efd174e65eadd6ba5acc02>`_
- Bodhi conglomerators for comments on updates. `6802ced0f <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/6802ced0f36677ee41abd8666532b50c37625cf1>`_
- Update docstrings as per review. `a3be25dbe <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/a3be25dbee4b272d5f5e364915e2a00c1697b205>`_
- Add meta information for the new pkgdb.package.branch.new messages of pkgdb2 `188e77354 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/188e77354274d2c88317794bb415937978e39c36>`_
- Add unit-tests for the pkgdb.package.branch.new messages `5a292463f <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/5a292463f020e5b8c6149071278aa8e9de65ee96>`_
- Show the new status attribute. `b798cf243 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/b798cf2435f32c49b80d73f7d30d3e0ecd0483da>`_
- Handle messages without status gracefully `f57035f5a <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/f57035f5aa69815cde9c498f3dfcccf7db257eec>`_
- Merge pull request #137 from fedora-infra/feature/more-bodhi-conglomerators `04afd1391 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/04afd139185c6876a30925f2a81f629b20ac0a89>`_
- Merge pull request #138 from fedora-infra/new_pkgdb `9c61d3bd6 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/9c61d3bd675d7b3ef2edf961ac77a7d66f96c633>`_
- s/Old/Legacy/ `0a421598a <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/0a421598af975a919db297b57bfc90c4f3e0d15d>`_
- Merge pull request #139 from fedora-infra/feature/new_status_for_fas `fb61fa224 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/fb61fa2248fd2d95ab3546b992708ba8914b5577>`_
- Fix the copr owner/user disagreement. `3b079a3c5 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/3b079a3c566c9de690c209aa82f29e002ef47da0>`_
- Fix copr usernames() method. `a7458caf6 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/a7458caf650a4b7e634efe3080634277634a108b>`_
- Merge pull request #140 from fedora-infra/feature/copr-owner-fix `6a466ce96 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/6a466ce96e38919b7f088e377e7a0965b2d5e9b4>`_
- 0.3.0 `c8c980bc9 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/c8c980bc96479943bab02a5f2e81028b17503aeb>`_
- Catch new subpackages. `19d315a48 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/19d315a48587c1e9798f3271e5b4865cd1b09814>`_
- 0.3.1 `c297cfb4a <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/c297cfb4ab918464baf9df704917b116440e4669>`_
- Add basic documentation on how to get started with fedmsg_meta_fedora_infrastructure `44bcf7c11 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/44bcf7c113dc8d188c4b1197bffa8caa6cb66c39>`_
- Embed the start documentation in the main documentation `2956dff6c <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/2956dff6c60aa62e3ba39d7dfe8d22b4f8b33fb9>`_
- Merge pull request #142 from fedora-infra/start_doc `d18f5e8ce <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/d18f5e8ceda77732e490cd54a74bf62a8bdcf495>`_
- Handle ancient ansible messages with no userid. `8305e290b <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/8305e290bd8d896fbd10fc598e5f46c6d14e289c>`_
- Merge pull request #144 from fedora-infra/feature/legacy-ansible `c2ae68bb0 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/c2ae68bb068db5571fdfd15e525232630384d418>`_
- Handle other kinds of pkgdb status updates. `5b8c5345b <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/5b8c5345b1b365ded1ac583d768a2f753c7e3454>`_
- Mark these pkgdb examples as Legacy `dbb15f79e <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/dbb15f79efc9fcea6468f60c74c1b268c53db355>`_
- Handle ancient koji messages that do not have tag info. `c71f146fd <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/c71f146fd13ae77083f4401a77e7f6a1a01e38db>`_
- Return the full patch for scm long_form. `7f93e7174 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/7f93e71743c8f1c07abf993fb8bf7324432e7589>`_
- Remove errant print statement. `e1aef8055 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/e1aef8055fd3b9a92ff0d0908356d0a87eb30853>`_
- Fix fedorahosted repo links that do not end with '.git' `135eaa4fc <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/135eaa4fc4367cd16176a310126fead81268b222>`_
- Merge pull request #149 from fedora-infra/feature/hosted-git-fixlist `9f518717b <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/9f518717b432d617044b12cd7d34b6b019bcc853>`_
- Merge pull request #145 from fedora-infra/feature/more-pkgdb `75338058d <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/75338058d8431dce292402bba9dddd1ecdeb4a47>`_
- Merge pull request #148 from fedora-infra/feature/patch-long-form `50d2e38d5 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/50d2e38d54cde33bc32015845aa914ba05676947>`_
- Merge pull request #147 from fedora-infra/feature/legacy-tagless `4a05f88a9 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/4a05f88a9295309c1e1ed0336ad576d076f12755>`_
- Revert these at @pypingou's suggestion. `13661ec89 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/13661ec8988d9d82a238883c968897aa02cd93ef>`_
- Merge pull request #146 from fedora-infra/feature/pkgdb-legacy `d2a61a143 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/d2a61a1439d9067d3c61d5315f01aba14e0d20c0>`_
- Handle enhanced bugzilla messages. `d0896ec55 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/d0896ec55c7cb775c924d3c79e943f418f634ea3>`_
- Merge pull request #151 from fedora-infra/feature/enhanced-bugzilla `30436b137 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/30436b137e47229a5a399db432cdf2d75119ad5d>`_
- 0.3.2 `154b44808 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/154b448087765d9d7291fd572ed1c8cc019fa309>`_
- Fix doc building. `216283439 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/216283439b2084c472b7474d997fc3d745760892>`_
- Merge pull request #152 from fedora-infra/feature/doc-fix `3a27bd980 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/3a27bd980b0595ca79ca396fd65e0a0c66e3e480>`_
- Adjust the cnucnuweb processor and rename it to anitya processor `f56f91a31 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/f56f91a31d88e70d97dca1262224abdcd57ee97d>`_
- Rename the cnucnuweb processor to anitya processor `b7b75444a <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/b7b75444a8abad43f32a2049cc204c83c7fa4345>`_
- Adjust the cnucnuweb unit-tests for anitya `9a8c23cfb <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/9a8c23cfb82d186e5d8c4ce512080a5645c7d0df>`_
- Rename the cnucnuweb unit-tests to anitya `cc2d84ec4 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/cc2d84ec428aea8b110836c89202c9b85d322494>`_
- Run the anitya unit-tests `3694ba826 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/3694ba8261fcdbdd0316254dd691f1f5f1c79ac7>`_
- Use the anitya processor instead of the cnucnuweb one `3e4e8fd30 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/3e4e8fd303186bfaf787dc8a58f9d1cd5e864443>`_
- Merge pull request #153 from fedora-infra/anitya `c8cee4658 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/c8cee46584fd613b58e5a26860c8a2428794360e>`_
- Add processor for Koschei messages `5ce91f4ef <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/5ce91f4ef9ec4cc5dc095289504c255a4d4b49ef>`_
- Test for KoscheiProcessor `01c04bd53 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/01c04bd53c9fc2d819662118bcf6fb17ec750fcd>`_
- Fix out-of-sync docstring `336fd4665 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/336fd46656c8a45b5055a5c641166f8f56de96d9>`_
- Adjust the anitya.project.map.update to reflect how it looks in reality `e116f64bf <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/e116f64bfc17a71fbd0f5841d39a9277407f4f8d>`_
- Adjust the anitya unit-tests so that the example messages fit the reality `036ac065b <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/036ac065b8ea608bfacf1ab8d8cdd44a2eac1544>`_
- Add logic to support removal of project mapping in anitya `bbeabe08f <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/bbeabe08fbe1fe00e515fab895b96e89807cfaae>`_
- Add unit-tests for the removal of project mapping in anitya `2457e6f44 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/2457e6f44a2cfaba6f5e6c703736762fc542a375>`_
- Adjust the unit-tests for the anitya.project.remove messages to reflect the reality `0db4a3cc5 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/0db4a3cc574c7bd6f13a40a0508e0d59b080ac65>`_
- Remove build_task_id and repo_id fields from the message `3eb169c07 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/3eb169c07815f9d1c0cfe4bd88b3e848adbe8736>`_
- Add subtitle for transition from ignored `61283c5d6 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/61283c5d6cde3711327b2bb64c83ee9a299d429b>`_
- Include repo and koji instance in subtitle `e45546a5e <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/e45546a5e24da7160c151f5a89075f5088d43e77>`_
- Merge pull request #155 from msimacek/feature/koschei `129c4bf2b <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/129c4bf2b74ccab93dd99dde4a9dd72afec6fc69>`_
- Set the right topic prefix for anitya. `7cc7f8d07 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/7cc7f8d0725f358355cd160d4ce0bceac0840eab>`_
- Change the example topics. `af991d628 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/af991d628638458be0e32b6bcb83162a917614ae>`_
- Get fedoraproject emails without having to query fas.  Fix libravatars. `fc39cf40c <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/fc39cf40ceb9ae850a470ffa07cf6e831abeb01b>`_
- PEP8. `12ccf915a <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/12ccf915a14ffcd59ab4bde2cb54ba45059f6ea4>`_
- Add a non-fedora user to get avatars and usernames right. `bdead3c90 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/bdead3c9091506bfdc771b8d50790c85ad4a329d>`_
- Merge pull request #154 from fedora-infra/anitya `0e94efcd2 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/0e94efcd20c408e225c487e1020a987310568bc0>`_
- 0.3.3 `fc0d4ddc9 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/fc0d4ddc99ecb3489977ee3442cc318e0e981bcd>`_
- Require a particularly modern fedmsg for building the docs. `4cff9aee1 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/4cff9aee1b735480b9d8e887bbf4f24bbba9a8ab>`_
- Fix doc_utilities. `39d76afce <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/39d76afce8fbedde2fa9dc8353160b208d961a9f>`_
- Merge pull request #157 from fedora-infra/feature/fix-doc-utilities `e44639b5a <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/e44639b5ab80fa9c89111d6957f4a9028c021bf9>`_
- Add groups field to koschei.package.state.change `bd803dd63 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/bd803dd63a4c4175c5dd8ed25b2ad4bbca311122>`_
- Merge pull request #158 from msimacek/feature/koschei `77b94ee68 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/77b94ee6809464db47523cb7a2912be1569cbbf4>`_
- Update the unit-tests for anitya's update message `16e9eda19 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/16e9eda1994c7e2a171f8f4d6a089a54b0a9ae3f>`_
- Fix the anitya processor for the update message `faaee82d6 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/faaee82d68f45cce264e7d869985e914601ae2e8>`_
- Fix the message sent by anitya and adjust the expectations as well `69d060e26 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/69d060e26e5e4c81c9c66473cdc446b16dd28897>`_
- Fix subtitle for anitya, inverted old and new releases `e8664961c <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/e8664961c4d1542457b5d9b9236c9753660e4959>`_
- Add failing test case for #160. `3f92641c0 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/3f92641c047cbabd150e6c7a79584024b68d73de>`_
- Fix #160. `1efc6d618 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/1efc6d6184808c8fe5bfc5d3920f68d0e2e20d7f>`_
- Add unit-tests for a message of update having no "old" version being updated `672d66c9b <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/672d66c9bdc70bc90f76dc0e97717558453fbefd>`_
- Adjust the anitya processor for message having no "old" version being updated `3452e6733 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/3452e6733dadcadd6fb004b45468b2194253c163>`_
- Merge pull request #161 from fedora-infra/feature/more-pkgdb-fixes `41b24ef89 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/41b24ef899d426bf1779aa2471bc8de276d7bfda>`_
- Merge pull request #159 from fedora-infra/fix_anitya `2b6bc5fe0 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/2b6bc5fe0222f83ff709cfd29291db5c9a78af33>`_
- Have anitya re-use pkgdb's icon for now. `e3be0f1d5 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/e3be0f1d581e13e4b9b8f80148c1ab669671c15b>`_
- Merge pull request #162 from fedora-infra/feature/anitya-metadata `82d007fb9 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/82d007fb964127070a3c972fc8d6d7175a7174c5>`_
- 0.3.4 `62897a2d7 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/62897a2d786d35c8c091836fa578a47b299a2ea3>`_
- Handle legacy anitya messages. `d052cb001 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/d052cb001dea8a7ec8766221ebcf27420b2de0d8>`_
- Merge pull request #163 from fedora-infra/feature/anitya-fixes `e117278ed <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/e117278ed8c4df2f3382c579cd3c10e216457b6f>`_
- 0.3.5 `e1378fc0e <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/e1378fc0e8e6ce5c58ce1780491e419002da702c>`_
- Apparently we're not guaranteed to have this value. `3720084c7 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/3720084c7280772a34dff80cff996bce4e6c49d6>`_
- Merge pull request #164 from fedora-infra/feature/yet-another-anitya-fix `4d0486963 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/4d04869639fea1fe106ddd737a2666c6d388a8e5>`_
- Add unit-test for pkgdb's message about monitor status change `92e377a87 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/92e377a87ed20ca9d156a0a59555882bc16c433f>`_
- Adjust the pkgdb processor to handle the change in monitoring status `6d0f58fed <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/6d0f58fed357f528daa6a68356d1fe1eb5ade4ce>`_
- Remove trailing slash on pkgdb objects both in the logic and the tests `13a363f40 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/13a363f40aa5d18ace71cf6f2f1ffe1501186e31>`_
- Merge pull request #166 from fedora-infra/pkgdb `cc8274752 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/cc82747520f05ee08abc8329b3421be5ea4ad1d4>`_
- Handle mailman links with and without prefixes. `3f5d6b15e <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/3f5d6b15edbf63f0bdcbcd9d06c761113b839b5f>`_
- mailman:  convert emails to fas usernames where we can. `ce35a7abb <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/ce35a7abbf810b1e88bfab0221da81f9ce557410>`_
- mailman:  No longer chop up emails into usernames. `146235413 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/14623541345dd598785b9271b89b539c6d54d0ab>`_
- Merge pull request #167 from fedora-infra/feature/mailman-fixes `2328588fe <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/2328588fe93f14c161eda76c360d52bb6e849204>`_
- Move fas tests out into their own file. `d77079aa5 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/d77079aa538c0e2da40356fe74ba30e1c3c763c8>`_
- Add fas tests that actually cover current messages. `85c2d7e4f <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/85c2d7e4fa33a0a8fe8a405b1a18879f9d2ce9fa>`_
- Merge pull request #169 from fedora-infra/feature/fas-fixes `50e9715d0 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/50e9715d0188acb933f18de03eb404323383a68d>`_
- lookaside: Dehardcode some assumptions `9391abfee <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/9391abfee6bd02fa499c81dd4a14cde8e18915f2>`_
- Merge pull request #170 from bochecha/feature/lookasidemsgs `526d28373 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/526d2837387265ee82dc430ae2cce233d4dfbdcd>`_
- Handle anitya's fedmsg message when an admin removes a version of a project `df274699d <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/df274699d5ab967e81157b8fb2ce4521be07f496>`_
- Merge pull request #171 from fedora-infra/drop_version_anitya `130ee11e0 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/130ee11e071bcfbfa3ff2f4b97647f8e654c4649>`_
- Clarify the purpose of the anitya.project.add.tried message. `8e9fef33a <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/8e9fef33ae422534fe07d921331d29a97835c232>`_
- Fix test failures for conglomerator ordering. `690d1182b <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/690d1182b0a6b8c273b0c06faa4af07dfc8d24ce>`_
- Merge pull request #173 from fedora-infra/feature/conglom-ordering `66a923908 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/66a923908cd2f26b8bc2e0b72a97d20fa12cdb32>`_
- Merge pull request #172 from fedora-infra/feature/anitya-try `0385f486f <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/0385f486fda27f7f8f1073796dc5be090f6cbb5c>`_
- Remove a bunch of the wiki upload messages. `25f6fa69e <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/25f6fa69e40ae5813b7550eef15dc03acb402cf0>`_
- Merge pull request #174 from fedora-infra/feature/new-wiki-upload `681f485e0 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/681f485e04b281e3e607da4a71525bf69069407a>`_
- A BySubject pkgdb conglomerator. `4921a5dfa <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/4921a5dfa49112861a70cfc5e585290dcad40aee>`_
- Reorganize and add two more ACL conglomerators. `af26e8ad8 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/af26e8ad80a549be645bb48eeef2af149bcf7174>`_
- Switch order here. `bcc7f56ba <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/bcc7f56ba5378aae63f8b4f3650a07799bcc5046>`_
- The New Hotness `b50f491d9 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/b50f491d9bc499ac5110c06a3f6671dd57ff8df8>`_
- Possessive nouns. `b6b9a9d59 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/b6b9a9d596c555db9994371934358dad14dc2400>`_
- Add forgotten koji task states. `d7eb88edd <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/d7eb88eddbb12257b34a309937933ea1f3d9279e>`_
- Merge pull request #176 from fedora-infra/feature/hotness `b05104234 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/b051042347fdb61ff59add69fc73cbd462a8239c>`_
- Merge pull request #177 from fedora-infra/feature/pkgdb-conglom `9a56d0d69 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/9a56d0d69ddb5c46cfecf9cf50d922a4fe068c25>`_
- 0.3.6 `4257c1a44 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/4257c1a44e6706a0cb0b1539f096077e333a99e5>`_
- Distinguish between these two anitya examples. `728f1e3b5 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/728f1e3b58aad49d66b19728ff4585f65b212f77>`_
- Typofix. `0d15c4c83 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/0d15c4c83f1dab6dd21c6910419d1a10a37d5be7>`_
- Merge pull request #178 from fedora-infra/feature/anitya-de-duplicate `001d0a503 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/001d0a5038f14f665506e9d6512f8586aea2ca71>`_
- anitya is behind ssl now. `0b7bfd039 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/0b7bfd0393a40cbe38f341620b0c420f16045904>`_
- Whoops!  Include hotness tests in the main battery. `1b38710bf <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/1b38710bfbc0e959104421be0d1626c355c20a72>`_
- Point hotness messages at partner-bz if they are from the staging environment. `a6fd536a7 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/a6fd536a7064a472c2d6a98b3197871354d26e7e>`_
- Point stg koji messages at the stg koji hub. `8984cbca7 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/8984cbca7b8287d3eb3db420fe2fc589a94f3c4c>`_
- Merge pull request #179 from fedora-infra/feature/links `ca4f3f678 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/ca4f3f678c5695f7b7efc8631ff35911a1dadadd>`_
- First pass at mirrormanager message handling. `232b817d0 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/232b817d016872996251ea7feb4459110f9ec401>`_
- netblocks messages. `2308e08f2 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/2308e08f27a9388fd956bdd1d260f7ee6ff09594>`_
- Fix string comparison in the fedimg proc. `2988d50cd <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/2988d50cdef4a2c617f20817911826f2f7863f0e>`_
- Merge pull request #181 from fedora-infra/feature/fedimg-comparison `d936eb60f <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/d936eb60f8eb83a9e03ee7bdc7d795fabb74d43a>`_
- Merge pull request #180 from fedora-infra/feature/mm2 `9bdc8293a <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/9bdc8293adb7928cf91fb80dcecd621c259cc57e>`_
- 0.3.7 `7b06763ec <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/7b06763ec4f1526c6b2ce96430864fa289cfb36d>`_
- Add support for the messages sent by anitya when the admins delete a distribution `0f1a7f1d1 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/0f1a7f1d1863939760f81f21d4af5c458d376355>`_
- Fix up topic in anitya's tests `fd54958e4 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/fd54958e4484248f8f08f63bec571b6b26305d52>`_
- One more adjustement in the anitya's tests `4de012eb2 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/4de012eb25dd574e99671fd8daf80ebf032072b4>`_
- Fix topic for the anitya tests `f8f4e5295 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/f8f4e5295670748e4c14627d9bb5afbb78b681a5>`_
- Fix anitya's unit-tests `f1e55074c <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/f1e55074c4f56dfc664da4443b25177accb6d6a1>`_
- Merge pull request #182 from fedora-infra/delete_distro `34bed947b <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/34bed947b591bdb6c646ff9fbd9ae04b9a2d9b97>`_
- 0.3.8 `5e2791f74 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/5e2791f74b3ef0b9dad193cc39c4e5422cc33289>`_
- Add and test the second kind of hotness followup message. `2dd8a3029 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/2dd8a30291c2eda3ab8e6290daae0c5d537a1d34>`_
- Mark a test as Legacy that should have been marked so a while ago. `4319119b4 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/4319119b49138590d505a1b32a022083769076af>`_
- No longer stuff package owners in msg2usernames for pkgdb. `1389de4f2 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/1389de4f295823cae23d60227e32d1f75b3e58f6>`_
- Merge pull request #184 from fedora-infra/feature/hotness-followup2 `cac1a95e5 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/cac1a95e5ef3da2edcb2e1fe3bd6420730dd11f4>`_
- Merge pull request #185 from fedora-infra/feature/pkgdb-usernames-kludge-removal `53443d205 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/53443d205f064269adae20db6c74b96f97f31b3e>`_
- 0.3.9 `f4ded79be <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/f4ded79be7b568d1e1b12778b28563e0af63c584>`_
- Handle Fedora Atomic ftpsync links. `882c623bd <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/882c623bd98f9572612899c85bcbbabb91e5f879>`_
- Merge pull request #189 from fedora-infra/feature/atomic-links `5f4357368 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/5f4357368d8009ee3c45fb8e3625378fa8ca627b>`_
- The summershum icon moved. `77f01db46 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/77f01db4623d2b894b28cbfc4243eb07cbeadfa9>`_
- PEP8. `14008cf14 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/14008cf1440133e7999538302e90b8b082d37d94>`_
- Handle hotness.project.map messages. `916876f53 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/916876f53d5601b2dd202eb31172018b3331bd03>`_
- Merge pull request #191 from fedora-infra/feature/hotness-mapping `7c767a849 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/7c767a849f1763d2a044eb4ed017c383cee45889>`_
- Merge pull request #190 from fedora-infra/feature/summershum-icon-change `78b6f5e2a <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/78b6f5e2ae3757191ef8c51597fb1a95ec154c38>`_
- Find out the package concerned when processing admin.action.status.updpte `69613068c <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/69613068cc12341ff832ee1386c6f4d67d82d361>`_
- When returning the list of packages, cover the new branch request messages `68b3caf71 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/68b3caf71d410a85a3f25ddbeba94201b1a3dee8>`_
- Add the explanatory message in the human readable format `536153367 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/536153367bacf54083cb43aed4b1962aa66dc487>`_
- Add a new test: an update message for a new branch request that is denied `e13a84d5a <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/e13a84d5a3f90aada480cc730b91fbba48225164>`_
- Merge pull request #192 from fedora-infra/fix_pkgdb_for_admin_actions `0b4327faf <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/0b4327faf081c862c4ee6418df72224e4f7d3de7>`_
- 0.3.10 `036ee5bbb <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/036ee5bbb6aafcf2808b563df7fa19878b98d8a6>`_
- Create test to elicit the error from #193. `2fa9cb4e1 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/2fa9cb4e1670475cac0eab0e3fed99511b5bf1e8>`_
- Fix #193. `65270ecd1 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/65270ecd1d6a8c4b68778711746561fbf36b0621>`_
- Merge pull request #194 from fedora-infra/feature/fix-pkgdb-messages `15d0a6c7a <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/15d0a6c7ad9bb0efb316898b619b82ed7a721543>`_
- 0.3.11 `ace76a125 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/ace76a125718fe28d0e2e95d39bd768ead5190fc>`_
- Move bodhi tests to their own module. `6ff109049 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/6ff1090492c0923e351bced438f7837fa7b2e616>`_
- Handle bodhi.stack.save messages. `fba701bba <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/fba701bbaf070f96b496ff1898b11b94cb6c4ee4>`_
- Handle bodhi.stack.delete messages. `529620de6 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/529620de620c58678c0b40906c976cc7dcd3e01a>`_
- Handle bodhi.update.edit messages. `bb945a037 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/bb945a037d621fa7685f2ce64ed2b43622229818>`_
- Handle new sigul messages (via koji). `442be7de2 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/442be7de22adef9cd8121bab21e4a0d042d2d0c4>`_
- Merge pull request #196 from fedora-infra/feature/sigul `6b7f2cec2 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/6b7f2cec2b23b84097ed0f31219909c4efcfaf5d>`_
- 0.3.12 `2cf84d830 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/2cf84d830016ea9f44830468a678ec786809a4a7>`_
- Handle bodhi1 and bodhi2 buildroot override messages. `1e4e9ded7 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/1e4e9ded73afed97b4b19756d5b30812fd966aeb>`_
- Handle mashtask and update.complete.* messages. `d67d0bb9d <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/d67d0bb9d80e79fc1602988421a13afc6923fafe>`_
- Handle bodhi.update.eject messages from the mash process. `52cd572a1 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/52cd572a104bbaf05de4be4e14b8f858d11faa52>`_
- Mention the sigkey in the rpm.sign subtitle. `82797fb70 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/82797fb701a80ada5ab902779a05b25e97695fa7>`_
- Merge pull request #197 from fedora-infra/feature/sigkey `08e02b792 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/08e02b79265767b5055b9b00297794490b82fdd6>`_
- Merge pull request #195 from fedora-infra/feature/bodhi2 `4780ce209 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/4780ce209043ac2d4fa98a47e58711689350fc94>`_
- Fix tests. `aa2753037 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/aa275303744c3b06029a0008b78290244547959d>`_
- Merge pull request #198 from fedora-infra/feature/more-grouped-attrs `9804090f2 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/9804090f24f7187fa1ffe9b1ab867f6b8f92ffbc>`_
- Demote this error message. `39531fd41 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/39531fd4198cd65053e0fe3208784cec106a1210>`_
- Merge pull request #199 from fedora-infra/feature/demote-error-message `88353d4cf <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/88353d4cfc3527e004bd6957e0f61f95255f92f3>`_
- 0.4.0 `6d9b2b801 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/6d9b2b801b25e1baebcbf1eb4f9ee6159516078c>`_
- Handle None at the end of mass branch... ;p `e197b8cfd <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/e197b8cfd08d83c28c6fd0323d09c3f36058431d>`_
- Create long-form output for github events. `aace64d95 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/aace64d95af6270e68e561018a3d55c8beba3208>`_
- Include full irc logs in meetbot long_form repr. `7baa7c9fd <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/7baa7c9fdcdc3093596496a60d354ef96071ac49>`_
- Merge pull request #200 from fedora-infra/feature/more-long-form `57c239cb2 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/57c239cb28c0be043450f1f3aa858bba001317e2>`_
- Modernize these fas examples. `9b66461b4 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/9b66461b49e29d40b58e8047d539456af6828c3d>`_
- Convert one FAS example into a legacy test. `3610f5373 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/3610f5373a7440b523c6ad6fe5d3805c14e2f3ea>`_
- Merge pull request #201 from fedora-infra/feature/legacy-fas `08b066f71 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/08b066f71cfa84571b0da93ecf5c6a525de0914f>`_
- Add some debugging around the fas cache lock. `dceb30b96 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/dceb30b96b2eb53f24ea69b9591f48b204dc9773>`_
- Merge pull request #202 from fedora-infra/feature/debugging `adb030de1 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/adb030de10d6a1d2ba47317de625c235812b4419>`_
- Handle "release" messages from github. `b5de46eaa <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/b5de46eaaac5b193a01fc810d60d074f2c7123db>`_
- Merge pull request #203 from fedora-infra/feature/github-releases `68b366138 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/68b36613875cde28d44472c34a0de7f714e278cd>`_
- Pkgdb dropped the from_branch information when requesting a new branch `fd8dba4bb <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/fd8dba4bb183e88ed80f2b0d0b20306dc47580d1>`_
- Adjust the unit-tests to reflect the changes on the messages sent by pkgdb `aa5dc85c0 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/aa5dc85c08c291fe5f6cd24069aa4ef4a12d5c4c>`_
- Merge pull request #204 from fedora-infra/pkgdb_drop_from_branch `c272313de <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/c272313de337ee7763a2b0986631cbe0466be4ee>`_
- Fix elections messages. `3fec1f459 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/3fec1f459b682ed2b75278c94110b1780ad2d1db>`_
- Convert github.watch messages to github.star. `fbdf5fe1c <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/fbdf5fe1c8d47c13064c4ae9b3e036bcc6a9c656>`_
- Associate usernames and packages with the hotness followup messages. `1e5d95ca7 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/1e5d95ca76f14763a9d38b11b2785e979d5134c4>`_
- Merge pull request #206 from fedora-infra/feature/more-github-fixes `3f31862e3 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/3f31862e3ad71584736649aee8a544c7d0d73876>`_
- Merge pull request #207 from fedora-infra/feature/hotness-users `2dc580447 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/2dc5804477f112c6bf623c1980aec058c361e163>`_
- Merge pull request #205 from fedora-infra/feature/elections-fix `5dad82741 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/5dad82741471a050af66b612b5acf8a6ff346624>`_
- 0.4.1 `bfce43e2f <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/bfce43e2f15c7190ea0ca7d9b8fd8adfdd1cc5b7>`_
- Add a long_form field for message about uploading files to the lookaside cache `86432850d <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/86432850d2a6f631817672a9ac10e7c5526d9eb5>`_
- Fix getting the current folder so that we can call that file directly `e73fe2b97 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/e73fe2b971e543a85b6487b457228f86d10c435d>`_
- Adjust the example patch for the change in cgit version `05e6f1f46 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/05e6f1f468ed481bbf49e06628fa6b445012a704>`_
- Add unit-tests for the long_form format of uploading to the lookaside cache `f980ec535 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/f980ec535d8e8eb348e296b4d87ec4dae14b193b>`_
- Merge pull request #209 from fedora-infra/long_form_lookaside `a37198d07 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/a37198d07a701cab168238ee0f8e9158f4984e16>`_
- Update this test to use a real build from somewhere. `0199f78c1 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/0199f78c1c1c13fa6ea1adea8cf74e0d57e000e2>`_
- Implement a long-form value for koji builds. `3bc8b1cc4 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/3bc8b1cc406c03a53e15e68c231c04c78d72e0f1>`_
- Add a way to disable these ourselves in koji and travis-ci. `aa6808eea <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/aa6808eea64e5a80aedcdd81d2691bd7978fcfaf>`_
- Add long-form values for trac tickets. `e1ec60be1 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/e1ec60be1f562f9faf31f7224ac5ed369ce88559>`_
- (anitya) Substitute Fedora package name for project name if available. `c99580a13 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/c99580a13a8268853b51f73193effd40ee3de5bd>`_
- Be on the safe side. `e964f8a9c <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/e964f8a9cf884486e64786748ea527bdc032ebad>`_
- Merge pull request #212 from fedora-infra/feature/anitya-sub-in-package-name `97573944f <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/97573944f7e9e69fcefdebb243b18b6352ee3b65>`_
- Merge pull request #211 from fedora-infra/feature/trac-longform `94a38f832 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/94a38f83291f794b6c1fb8e3abd065829b9af6ff>`_
- Also test longform for failed builds. `67c5fbab0 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/67c5fbab0335e822b670e4b379f0a7a020977ed4>`_
- Also test longform for cancelled builds. `9bab7ad7f <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/9bab7ad7f25863d84d3c2b686e2a7e4f7b706b6f>`_
- Merge pull request #210 from fedora-infra/feature/koji-longform `c60343c09 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/c60343c091d221cfbdef64d3b47e793f53bd2fed>`_
- 0.4.2 `900b4a596 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/900b4a596867d7c09b6fecd85353b40d010290ed>`_
- Comment out the buildsys cancel long form test. `f50eda651 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/f50eda6519a76f8eacf8e681e2b41e831c7ff7b6>`_
- Be more careful with these timestamps. `64f6116cf <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/64f6116cf59a0eda0fab1ff1a709ae8fe804cb7a>`_
- 0.4.3 `4bbd5b245 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/4bbd5b245314d6705cab494d68598eaf152db2d9>`_
- Make github longform tests conditional. `4f46090dd <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/4f46090ddb15c676b51b5b8537220612349b6a68>`_
- Move zodbot tests to their own file, and make the long_form part conditional like the others. `0a99a6226 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/0a99a6226856c77ec35eb18a9e12eda7fa0d69b0>`_
- Merge pull request #213 from fedora-infra/feature/more-longform-conditionals `b030cf966 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/b030cf96603fd6117874814c2f04dab31dcb0b6f>`_
- Don't return prematurely if parent task is still open. `1f80bf7c2 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/1f80bf7c2e666378f23ebe5c83d5e1222142c3c7>`_
- Merge pull request #214 from fedora-infra/feature/koji-longform-fix `fd9cea78a <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/fd9cea78a2eeb68ffc91791ef224d254fa414e1e>`_
- Handle case where result never gets defined. `727bbe1c7 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/727bbe1c7085bd0a7e32ae2afdb75461328307e9>`_
- Add new copr fields to the docs. `d7cb97119 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/d7cb97119ec87d6e2576779f0ad9cd8f17b63fb0>`_
- Adjust copr.end subtitle to indicate the version of the build. `186811dac <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/186811dacbf3b268240b31d927236d58716df024>`_
- Add a long_form representation for copr build completions. `7488a49e9 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/7488a49e9d1df4c5f5c73a53bd6daa77228ab16a>`_
- Add a build failure test just to make sure we have all the bases covered. `b4eb0807f <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/b4eb0807f6855a14028606669c344ff890f4bce3>`_
- There is more info here now... `d8f8e3713 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/d8f8e3713a7ba091d2e2374d39d17732cb0839f8>`_
- Add a link to more useful logs at @danvratil's suggestion. `0a46fdd69 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/0a46fdd69e86884aa4ac00de06eae58adf54151d>`_
- Also link to root.log. `dd1c085a8 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/dd1c085a8698e19b9ff5da3b43f6c8ea5e234a49>`_
- Oh, and of course, https please. `4a15d69c5 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/4a15d69c51a808fb4ad9973bf9e7c5b600731961>`_
- Merge pull request #215 from fedora-infra/feature/fancy-copr-messages `7367a5f53 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/7367a5f536ee8c1b569b15ace59115684948b3f8>`_
- Merge pull request #216 from fedora-infra/feature/koji-longform-testfix `a223aa0e2 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/a223aa0e23337fb96d05577af566f5d5dd7e504c>`_
- Added Github Page_Build Message Handler `587bd3275 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/587bd327563465d71fe74575a663c2b207cdf448>`_
- Merge pull request #217 from Ghost-script/page_build `b88644e06 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/b88644e0614188ccce6edc4d2db428caba805d0d>`_
- Added Github Tead_Add message handler `1fb35abab <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/1fb35abab91ac60d09a87533a65de714d474eec1>`_
- Merge pull request #219 from Ghost-script/team_add `f6f593bd7 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/f6f593bd7fb4d483f4c297cb1f19ae6acdf5606c>`_
- Add processor for new karma messages. `c018104f9 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/c018104f9a13cd052b7875c535935ed9ec5e6e4f>`_
- Use FAS openid libravatar first for git.receive messages And porting scm tests from __init__.py to scm.py `45c2f47d1 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/45c2f47d14a610b4e736eadb8fedac91e7ed148a>`_
- These should be here. `94ece2b33 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/94ece2b3381b23846870484f57e2d06cb2a1908d>`_
- Merge pull request #221 from Ghost-script/openid_libravatar `49e3df842 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/49e3df8421549b59d2f843123427cd0540c82fd2>`_
- Add icon url for fedimg logo. `77f83a329 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/77f83a32964258644930e9a8734cab9299debbb2>`_
- Added message handler and tests for Github member (added to)/(removed from) messages `4f747e0f3 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/4f747e0f39b26529670d642d03496e05b1d5e814>`_
- Merge pull request #227 from Ghost-script/github_member `f50e03724 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/f50e03724e1f8ccdb1e16f0a3dcdfd13d24e5377>`_
- Merge pull request #223 from fedora-infra/feature/fix-conglomerate `738d431ea <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/738d431ea1c2faec67f2837bee54853926fbfe35>`_
- Merge pull request #224 from fedora-infra/feature/fedimg-icon `ef48b3a85 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/ef48b3a85873fa297f447cb34411e9c3f17c7c83>`_
- 0.4.4 `eb6b92dfd <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/eb6b92dfde4de6aea8f7046ae501d53bb3c41028>`_
- Adding Anitya tests for new version of packages detected mapped to multiple packages `0f1ae6b0d <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/0f1ae6b0ddd5415a9bac8b8e7d44bfde7b4539f9>`_
- Removing N from the list of values passed to list_to_series() function `6684e7e60 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/6684e7e6021487db3ddf1856f21dcdfa74f159ad>`_
- Merge pull request #228 from Ghost-script/anitya `775595942 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/77559594284e461ad058bbe3d77010aa82045020>`_
- Merge pull request #222 from fedora-infra/feature/karma `44e5bf4ee <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/44e5bf4ee80439f553f3fa4bf2b33e439fcb657d>`_
- Add tests and implementation for new meetbot line items. `6a96132c4 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/6a96132c4358d89947bc050ddfac3c625da293ad>`_
- Ignore koji longform tests if koji is not installed. `e2b53ef44 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/e2b53ef44b7d04d45acfbecdb3098d2360d255b1>`_
- Merge pull request #229 from fedora-infra/feature/halp-items `02bd9406b <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/02bd9406b73b686643b899785182ed6b150b1604>`_
- Merge pull request #230 from fedora-infra/feature/ignore-koji-longform-if-no-koji `83aad3c45 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/83aad3c45b25c67c7804c81a92874955dcaaa591>`_
- 0.4.5 `23dece4ef <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/23dece4ef26b2e5d4e8d75429512ba7ffee6139a>`_
- (meetbot) use the agent's name where available. `22b9d8280 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/22b9d82800db58ba860afad308b7ae780fea96d3>`_
- Merge pull request #231 from fedora-infra/feature/meetbot-tweaks `ad46e8983 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/ad46e8983eb5844522b25513bdda9053d317c817>`_
- Add more info about why karma was given `cdeaf8070 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/cdeaf8070bb58809f725ad9bf6d367724339185a>`_
- Merge pull request #232 from fedora-infra/feature/karma-tweaks `c8ca14c43 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/c8ca14c4304c2d3765af3d10c5b9b363579cb6d2>`_
- Shorten git commit emails if they have already been seen. `452eb15ec <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/452eb15ec42e093cb4ecf9cbe477885d23c6cfb4>`_
- Merge pull request #233 from fedora-infra/feature/seen-commits `514d67a0d <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/514d67a0dc128afa9b8b433476bb3f46ccd557b1>`_
- 0.4.6 `379251578 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/37925157809c583753982158edc34f4ef021eac4>`_
- Be careful with the trac ticket summary. `6b2373fe7 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/6b2373fe70ed500f557b99e35c50038de2876c66>`_
- Strip out None values from the bodhi usernames list. `bb52a3440 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/bb52a3440c0797bee280c817c85d764552e6c241>`_
- Merge pull request #235 from fedora-infra/feature/bodhi-anon `c9733443b <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/c9733443bd148a64958e900d93917a0bd28251d9>`_
- Merge pull request #234 from fedora-infra/feature/fix-trac-summary `74305eafa <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/74305eafa82ce48ecc1d3af41f7b0b554fb52c3f>`_
- (unrelated) these failure tests are unsustainable.  they change underneath all the time... `9ec4ec087 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/9ec4ec0871b20a090378214ed1209e1fca03664c>`_
- Add long_form for koji scratch builds. `12044f462 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/12044f462eeb28a5b5c8c1ceaaacdd978e33866c>`_
- Merge pull request #236 from fedora-infra/feature/longform-for-scratch `b387c333e <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/b387c333e6077cfb928447886a0d49685fba046e>`_
- De-duplicate subtitles from long_form representations. `312bb250e <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/312bb250e649c45fb6f0be20cbdc4e13cb7d341e>`_
- Merge pull request #237 from fedora-infra/feature/de-duplicate-subtitle `e7bf1014d <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/e7bf1014d3d87a5eee038a783126db2cf104f84b>`_
- 0.4.7 `5e5ef52d8 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/5e5ef52d8cd326eaf28051e73e692f6ce0c503eb>`_
- Add the Pagure processor for pagure's fedmsg messages `f1ce03a90 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/f1ce03a9019cce32cf3a42a03f89a8fdb5ba7ca9>`_
- Add unit-tests for pagure's fedmsg messages `85173cd70 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/85173cd704c795bbdb67f16e2e2d123d10c7bb00>`_
- Declare the pagure processor in the setup.py script `8d6450c9f <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/8d6450c9f4b5762e7c0cd644c063ca8c384bfc3f>`_
- Merge pull request #238 from fedora-infra/pagure `599ac8072 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/599ac8072418912b3fe12bb84bfb7e64032c6249>`_
- Include the comment text in emails about bodhi comments. `576fe8ce5 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/576fe8ce527a317d3f3c4a7baed32355e2afdc05>`_
- Trim end of line spaces `f55d11e62 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/f55d11e626b2a63d3f539f73561366af55d1d675>`_
- Add support to anitya for odd changes `380d8c454 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/380d8c454dd519b4d569aae5ac90a61e83977502>`_
- Add unit-tests for odd new upstream version `6e6d6f37a <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/6e6d6f37a74dc641bd2111018e77f3ff24711e2d>`_
- Adjust docstring to represent the action `e495b3ac3 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/e495b3ac3fa4d7390c869e8756fdbf21d1820180>`_
- Merge pull request #239 from fedora-infra/feature/fix-some-bodhi-things `96f883a24 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/96f883a24b4e53bad1345e415b98e5cdc98bfa05>`_
- Merge pull request #240 from fedora-infra/fix_docstring `945b74ba7 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/945b74ba721b881a91f3bcfc83ddfd441807151f>`_
- Handle new hotness message type. `1ba0b6909 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/1ba0b69090812bd2974a2106b6985ed6c404416b>`_
- These koji tests results are always changing.  We'll need to mock this long-term. `575fdc1e3 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/575fdc1e32088a6008a84a41b83757114d6798da>`_
- Merge pull request #242 from fedora-infra/feature/new-hotness-messages `cdaf5cf73 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/cdaf5cf7399452ebba055d69a218120f55517edb>`_
- 0.4.8 `3b88e2a5b <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/3b88e2a5b9506061faf8d345dab186f13c41bb95>`_
- Be more careful with null task_ids. `1b0a00659 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/1b0a0065924fcfbfd71ef2c1e8dfa17269cd44bb>`_
- PEP8. `fe593bca9 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/fe593bca98a6e7f04aabea1d57f22dc6e6dcf10d>`_
- 0.4.9 `2d7f90f9a <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/2d7f90f9ae53a2f449b6ad785d726ef4fb1b7a62>`_
- Be careful with a null host from koji. `8c28d021d <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/8c28d021dddbe8804584414735036251a15772c6>`_
- Merge pull request #244 from fedora-infra/feature/careful-with-null-host `09e2a442a <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/09e2a442a690935aaf14010d92dbb0e14913c96b>`_
- 0.4.10 `80908230f <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/80908230f39b7cb65bf2c065b2a4a31d964e6545>`_
- Use nice package icons where we can. `d4cf3aba7 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/d4cf3aba7774fe7ac5ea2c820fa83f9607e79c8d>`_
- Remove redundant line. `eb9bdd171 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/eb9bdd1712a757d705badca54d6d8904b07b060a>`_
- Merge pull request #245 from fedora-infra/feature/package-icons `2ea3f0892 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/2ea3f0892ceaf573c4703b15eb3a7cf752eb03f1>`_
- Add unit-tests for pkgdb messages sent when someone asks for a package to be unretired `923b3e918 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/923b3e9186bc0d83c26a21f4417e02ce33d13982>`_
- Adjust the pkgdb processor for messages asking for unretirement `e75627f85 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/e75627f8567b4f3fa96370a078127427fd00d9b3>`_
- Merge pull request #246 from fedora-infra/missing_pkgdb `3aa1190e3 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/3aa1190e3b0046a2d319a8df5ae41615511eea5f>`_
- 0.4.11 `b6b3f80f5 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/b6b3f80f5c59bc0ead82cc3428c779f5d8f87bf1>`_
- Try to workaround an odd variation in message structure. `c7f8dfae3 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/c7f8dfae32c491d8d06077d7e3cafc96454f9e96>`_
- Merge pull request #248 from fedora-infra/feature/anitya-workaround `e89c8f171 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/e89c8f171118b54f4ac94de680a0cdf99c7af359>`_
- Port to Python 3: `e659faa93 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/e659faa93072e4c366f4b5670a247cc9ba59710c>`_
- Merge pull request #249 from bkabrda/develop `0fcd3f770 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/0fcd3f77066ae7df7d168e0d476404f55c74de83>`_
- Add tox config for fun and profit. `3846162f3 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/3846162f3e6da44fc7eae7cb4aefc69aca06dab9>`_
- Add .tox to gitignore. `247d26166 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/247d261666514d6b426b761bdd0e96e9d1c330e3>`_
- Handle bodhi errata messages for #96. `4266f9c82 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/4266f9c82a589fac2c4e6b3a382d4c4a6451ec9e>`_
- Use the errata email for the long_form repr.  Fixes #96. `2b73918a8 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/2b73918a8951815c4f647f0d3da0ba885958c9a6>`_
- Handle new update karma threshold messages. `f7895a2c6 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/f7895a2c6928daff60760533205c9b638231af31>`_
- Merge pull request #251 from fedora-infra/feature/new-bodhi-messages `411bddc17 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/411bddc17f9ed6ca5c8324bce4961cdd889fc1f6>`_
- Merge pull request #250 from fedora-infra/feature/tox `36d9f5652 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/36d9f56524cb11cb0ac90c81047a45d9837a8baf>`_
- Use the bodhi "alias" instead of "title" if available. `917471103 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/917471103052886c971cd54f82818c964f78c006>`_
- Merge pull request #253 from fedora-infra/feature/use-bodhi-alias `c468b2a4e <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/c468b2a4e2329a1e375b7e0ea500f9048bbde237>`_
- Rename all occurences of "gravatar" to "avatar". `3da40c955 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/3da40c95593a4dff41a696732e209148e89ecf4a>`_
- Comment out a perennially-failing, network-dependent test case. `6560390b6 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/6560390b6cc11ab6f6d4ba5b1cd0f597970381f7>`_
- Remove unnecessary lines. `6e6b3f041 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/6e6b3f0416ef1be81fc35e9b107f15634f585935>`_
- Fix typo'd return value. `4df5e94a5 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/4df5e94a5d15971fcc4baca7078d7b4f006c961d>`_
- Merge pull request #254 from fedora-infra/feature/remove-gravatar `a5f06793c <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/a5f06793c4296c6ee9dadaae8053186fc9e91403>`_
- Add zanata processor and tests. `d4c0deed2 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/d4c0deed25fdb724d29d45c0f2690aadf42c95cf>`_
- Merge pull request #255 from fedora-infra/feature/zanata `b6599b694 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/b6599b69401acc2a7d3c52d42d621181f739211d>`_
- 0.5.0 `fde5a7cad <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/fde5a7cadb97ef78f4628039f3788df501df0197>`_
- Test against multiple version of six.  We have an old version on epel7. `3f47d4d88 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/3f47d4d880fc0f20adc4497dc59bf57a93c52d1d>`_
- Be careful with old python-six. `80aa83234 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/80aa8323438fd5da8875c63ee22ca4e27355201a>`_
- Adjust tox to test old python-six. `c637f3b94 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/c637f3b94d2a114a0892a821b737789d954bebbd>`_
- Merge pull request #258 from fedora-infra/feature/six-careful `db1435539 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/db1435539315b020e14710d247333dbef917a6ab>`_
- 0.5.1 `4951cbc1b <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/4951cbc1b496246097bff0d51d48e7d45cb8e740>`_
- Added tests for "fmn.rule.update" `22e424de0 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/22e424de0867369917fd9afe49083bf8bb26aac9>`_
- shorten Fedimg messages `31f79d788 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/31f79d788f4c09cbf8b60671120428d0869e7a00>`_
- remove deprecated comment `ec3e8afac <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/ec3e8afac0071b528edb186b2a5cea249fce9199>`_
- add this missing tmpl line `a7da68284 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/a7da68284846347b07f3a1553a598430d0b12813>`_
- print extra details for fedimg actions when applicable `c78bde198 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/c78bde198a7cdaf4f385af1d51720444180dd91a>`_
- update tests for new extra dict in fedimg output `7e0ccafa3 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/7e0ccafa3732f96c8ca267112321662620ff33fd>`_
- tests: test for fedimg task complete message `14e3abea2 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/14e3abea2e647368e24d035b18c0639240d79107>`_
- Merge pull request #257 from Ghost-script/bug247 `0b1d4ea22 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/0b1d4ea221133d09ab460561cc48855d2226c405>`_
- FAF (ABRT server) processor with tests `f08878aa5 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/f08878aa5ea081379874aa4bc0d7e98e62ac43f3>`_
- Merge pull request #259 from mbrysa/faf `19cc66e50 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/19cc66e50d57957826c6e3951c72705c628a9255>`_
- Sometimes, there is no blog post title. `706fdf3ee <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/706fdf3ee130f6df2b3eec298007368994c99a2b>`_
- Merge pull request #261 from fedora-infra/feature/no-planet-title `1cb772115 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/1cb77211559aab2b9a7318492d9699f5fb131d08>`_
- 0.5.2 `052ce32e7 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/052ce32e7806dcea41defca8051900122270221f>`_
- Try to make admin actions more understandable. `1b7508962 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/1b75089623fa375808a94a4fc3d40f8c06013ac5>`_
- Careful that there is no "agent" field. `1a7485e6e <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/1a7485e6ecc2efdc5fdf82287b5ec828d442694d>`_
- Merge pull request #262 from fedora-infra/feature/admin-actions-redux `68e1febe2 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/68e1febe2f5c48105368181135d608a667e56df5>`_
- Merge pull request #264 from fedora-infra/feature/scm-no-agent `98c969cda <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/98c969cdad1fe123da8344a7937fffa778215b9f>`_
- Fix broken links to election events. `0f2983b15 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/0f2983b1504eef39256185bbeea112f931d33224>`_
- Merge pull request #265 from fedora-infra/feature/voting-link `082a6ca76 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/082a6ca761ccf62f8bae2986d50515a985f04c67>`_
- Handle fp.o addresses. `8fcca42b0 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/8fcca42b02653085ae955482d96d68aaac3aa5a6>`_
- Merge pull request #266 from fedora-infra/feature/fp-o-addresses `8674c71cb <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/8674c71cbc9b9f95ab1fff89bb9ea9176a4e18c4>`_
- 0.5.3 `7b220635f <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/7b220635ffc04b989844d2e2fe5e1031baa5b4cc>`_
- typofix `bd845a291 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/bd845a2913706e1071967ad6a75a5877c528fc17>`_
- tests: there should be this icon here `9c07cba0e <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/9c07cba0e3f7bb930b92a6903a76740c211512f5>`_
- expand on the fedimg docstrings in the tests `0c3293715 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/0c32937156fd8977434be26a5ae156f53893bbde>`_
- oops -- need icons here, too `39d97f5dd <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/39d97f5dd401eb98da85ab71973344d3470dfcee>`_
- tests: add some expected objects for Fedimg `8458c011a <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/8458c011aa79c7a95744dd70b293c8a656c9c1b8>`_
- tests: missed tmpl assignment `cfe9ed6fb <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/cfe9ed6fbdc285dbac5d8fb075ce67f60bb9c18b>`_
- fedimg: refactor subtitle code a bit (fedimg tests run now) `6bc60607d <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/6bc60607da2fa98852b88b553857faba2a81352f>`_
- fedimg docstrings: s/awarded/published/g `3599044af <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/3599044af53c290804baf0ae5057f57ca16aa81c>`_
- Merge pull request #260 from fedora-infra/feature/improve-fedimg-details `8ba23df1e <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/8ba23df1e9f2747544ded447ffba2bb63be784a9>`_
- Extract the "package" from inconsistent admin action messages in a consistent way. `fa2d9a2b1 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/fa2d9a2b1dd29fe3c2636c5bb5c663ef4ac5673d>`_
- Merge pull request #267 from fedora-infra/feature/admin-action-fix `5144e9f1d <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/5144e9f1dc97e6452839f1f87fda5334e9ef4afe>`_
- 0.5.4 `ec1894aa0 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/ec1894aa0542caed2ca88790cabcc34f6b21866a>`_
- Fix syntax errors. `05452d49c <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/05452d49cfeca05ce21bc30f8a6b688f37201076>`_
- 0.5.5 `20f0a7fde <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/20f0a7fdeb22be4d17ae449cfc2a67546333dfff>`_
- Fix pagure regex. `6b451b01b <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/6b451b01b7c2043f92f46ef59349edb2e2a46841>`_
- Merge pull request #269 from fedora-infra/feature/pagure-regex `99da5003c <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/99da5003ce7395c5795e0e53967417d0a8e1d942>`_
- Add arrow for the travis tests. `dc9b9a2a5 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/dc9b9a2a5f2e2aa550d15fca1212bfb0c81bcaa0>`_
- Fix a typo in the FAF processor. `ed6798fb8 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/ed6798fb8dbb0417f4e71f1b24092f57d13304ef>`_
- Merge pull request #270 from fedora-infra/feature/typofix `ac080c469 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/ac080c469da14ac2f08ab33812fb34d09a7cada2>`_
- Update Koschei icon link `4e4f33824 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/4e4f33824bcf993d96c138364dfce871ef935f96>`_
- Merge pull request #271 from msimacek/feature/koschei-icon `aae60812a <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/aae60812a91e86ad8a41bc0fdd583acd085545bf>`_
- Add logic for the pagure's PR.flag.added and PR.flag.updated messages `ea86921ae <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/ea86921ae03d8cf5d485ae0acaccad9c9e41eb9e>`_
- Add unit-tests for pagure's PR.flag.added and PR.flag.updated messages `d37d61010 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/d37d6101014a0bf616c603187f2f85e73a36afa0>`_
- Adjust the subtitle as per @ralphbean's suggestions `86ec32958 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/86ec32958ca0914a1cfd9df52d939775654968a6>`_
- Merge pull request #272 from fedora-infra/pagure_flags `e9b580933 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/e9b580933f744e6cefa43267e59b64e090eb58d7>`_
- 0.5.6 `f614770e5 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/f614770e534b212d4e1ea547d7be50ef9562f044>`_
- Fix problems with pagure processor and test suite. `de7fc3f22 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/de7fc3f2264ab9e39d36070d76fafd83a848b43c>`_
- Merge pull request #273 from fedora-infra/feature/fix-pagure-tests `e5096fd5f <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/e5096fd5f9668bfabc039520a13535bfd116f5f7>`_
- 0.5.7 `d2db17c2b <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/d2db17c2b117dc018dc8e5c4076dfa982690fe11>`_
- Try to avoid pagure exceptions for some unhandled message type. `6488cea86 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/6488cea8620c97a1e6b6a8abc4846bc9dec69ed9>`_
- Merge pull request #274 from fedora-infra/feature/dance-around-pagure `494ca8edd <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/494ca8edda22469554edae6e02e5474d752ea96f>`_
- 0.5.8 `a42949a58 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/a42949a58e0f9bbf637eab05d018e8cc4da6a96d>`_
- Add support for pagure's message about commits `180899ccc <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/180899cccd6950cd8930ac574fc8d13997639236>`_
- User email2fas to be a little more FAS' username friendly `2aac21a45 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/2aac21a45a69fe8f06804eb841472564957e80ad>`_
- Merge pull request #276 from fedora-infra/more_pagure `a7570d83a <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/a7570d83a193f7f7f42e6ff4fde2e342206337c8>`_
- 0.5.9 `fd241927e <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/fd241927ef852979c0ab227d7b508b247be69a7e>`_
- 0.5.9 `28d44e3d3 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/28d44e3d31dfec7a71785fb3049d55d833d0fb16>`_
- Use badge.award 'description' in long_form `dbb892eb6 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/dbb892eb635154ffcd6bb9427436120991c8d775>`_
- Merge pull request #280 from pranavk/develop `1b0cf481f <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/1b0cf481f5f4699bf3deacce07ec741f649a58d3>`_
- Attempt to add titles to github PR/issue openings `649637393 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/649637393f21049120ba80304e528591f9d7bebe>`_
- Fix some syntax errors. `8ac39b3af <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/8ac39b3af0294c53c197d94b214293bc48510ef9>`_
- make tests pass `b2214a082 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/b2214a0820c1c69bd3d0b30e42c409062957c927>`_
- Merge pull request #282 from fedora-infra/issue-open-titles `d438f45d6 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/d438f45d6c2735b787b4761a5c051df8874032bb>`_
- Faster, please. `28170f2d9 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/28170f2d91678a98ee585746ae51e83595a77b13>`_
- Link directly to pagure comments. `633a39bbf <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/633a39bbfe3373eabbd7fbd79494d2d0fbd4c3ce>`_
- Merge pull request #283 from fedora-infra/feature/pagure-links `9d1feda98 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/9d1feda98397ba0ec02b1472354e34e78cd87381>`_
- Update language for pagure messages. `bd3da61ef <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/bd3da61efd0bf6a53c5f0621da3620a935f34dc1>`_
- Merge pull request #284 from fedora-infra/feature/pagure-language-changes `837191f7d <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/837191f7da987ec46885c2affac1ed3f40b902da>`_
- We should return a link... for #link things in irc meetings. `2b0ad74ab <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/2b0ad74ab30231c49c2f282d8308f1c131dca7a6>`_
- Remove spurious print statement. `f1748ed76 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/f1748ed7682c4202bd43e9fcfdad879b23c72563>`_
- Merge pull request #285 from fedora-infra/feature/link-link `8e3e2128c <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/8e3e2128c32f2584b8e6af78787c97391adb9a86>`_
- Update Koschei URL `4e08316e3 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/4e08316e3a206680584bddc36b6f096a71635c9a>`_
- Merge pull request #287 from mizdebsk/koschei `634098d16 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/634098d167c8dc7216094bd2ea65a8d85c7d6ca6>`_
- Adjust the docstring to reflect the test `2aef1ebcd <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/2aef1ebcdba69559e898fcc9f075fb5050cba36f>`_
- Add logic to process messages sent by pkgdb when changing the koschei monitoring flag `554038f11 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/554038f1133f5fdc4937eea864773fc5ec441501>`_
- Add unit-tests for the message sent by pkgdb when updating the koschei monitoring flag `97351e2f7 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/97351e2f7c2b125f3964786201d2585d1e7d4503>`_
- Add missing space to make the link work properly `43664879c <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/43664879ce6af5daf2fc076cf488e281ac76fb70>`_
- Add test message of a failed scratch build with information about the target `ba65c7241 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/ba65c72414c4dacf3a7d330a58939f436c326fff>`_
- Specify the target of the build if we can extract it from the message `a60706c22 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/a60706c22cfa47e26aa4cc48d7b0e1e985af7984>`_
- Merge pull request #288 from fedora-infra/pkgdb_koschei `2a3066914 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/2a3066914f9a5f1fe21fd59ee15f959c876b80e9>`_
- Merge pull request #289 from fedora-infra/scratch_with_target `79294105f <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/79294105ffb9377af3692679c82369a4d091212c>`_
- Careful for x-archived-at being None. `92e77072a <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/92e77072a61a57385df5a40822dd8e32a0d90b84>`_
- Fix grammar for github.pull_request.synchronize `42df2c3d4 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/42df2c3d4b92e108c96c1e3f33d43ee21ca99504>`_
- Merge pull request #290 from fedora-infra/synchronize-past-tense `7a1c74a81 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/7a1c74a81ec1ec1d631e662dffa0a971171def01>`_
- Update pagure comment links. `b23e24247 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/b23e242473d749ed7c1256981d2cbce5dea04ab1>`_
- Merge pull request #292 from fedora-infra/feature/pagure-link `60b33fe40 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/60b33fe4029c5739b8fa6eaaf058c1841324a41c>`_
- Ansible conglomerator (for fedora-hubs) `6a1d55773 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/6a1d55773ea33902cbebd94d3ef8fc5423e7ce01>`_
- Handle case where constituents have been pre-filtered. `e8e760e0e <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/e8e760e0e0361cbf6cffad5133f0db6c57b13b84>`_
- Tagger conglomerator (for fedora-hubs) `6e6202e39 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/6e6202e39804be3ac64db2e8badec5aecb4390ad>`_
- Consistency. `ec985c8d0 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/ec985c8d0f9910f533b0c3f303deaee5cb4673d9>`_
- Remove duplicate declaration. `ef62ab93e <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/ef62ab93e6002fa2f7e35fa495eec2b217ef8ea8>`_
- Merge pull request #294 from fedora-infra/feature/tagger-conglomerator `8a70eb667 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/8a70eb6671567fb37864ef641822310d42f3b97a>`_
- Drop hardcoding of humanized time in the test. `4eb882116 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/4eb882116db88926d8862d2d7702d26227b99d03>`_
- Try to handle all these plural cases. `c55e09523 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/c55e09523adc135b7c79b9e6eecb1374c1775267>`_
- Merge pull request #293 from fedora-infra/feature/ansible-conglomerator `9cf772c48 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/9cf772c48bb68ad4cbf95b77b554f54ec70c69d8>`_
- 0.5.10 `3bc79cebf <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/3bc79cebf66a9c42aaa06cd78aa96941055a445f>`_
- Fix incorrect key. `8e33726e0 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/8e33726e0ca3fa8597d4ea46659d3ff8732377a6>`_
- Merge pull request #295 from fedora-infra/feature/mm2-fix `43f26b3af <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/43f26b3af8563909806193fa934d31ecc443f897>`_
- Remove hardcoded relative time from tests. `435080a85 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/435080a85579bbd79d7ebafcd6f0d2bd3032fce0>`_
- Copr conglomerator. `7c7fdce89 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/7c7fdce89753a77a87e87eebf126d39f11998b03>`_
- Merge pull request #296 from fedora-infra/feature/copr-conglomerators `a4874f254 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/a4874f2547141cde45e338afe614677e69a61a5c>`_
- Protect ourselves from lists. `8ecfad370 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/8ecfad3709de3f94745a7aa37388b8fbccf97a43>`_
- Merge pull request #297 from fedora-infra/feature/buildsys-fix-weirdness `7b82342ab <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/7b82342ab7c8e7f89835d6598346c4b96b1bbbaf>`_
- 0.5.11 `9a2b24c52 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/9a2b24c52160956c1d00b84099e7531e0aec3d21>`_
- Update copr urls `ad8a1092b <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/ad8a1092b759adebf765939a18c1bf9134bc916e>`_
- Fix #96  "in advance of" should read "newer than" `684c98411 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/684c984118c52126154ad4b03bacf1497635a4b9>`_
- Update tests `facff07e6 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/facff07e62f74251c72eae2cea73441c2f3df365>`_
- Be still more careful with this mm2 field. `7a6a3e161 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/7a6a3e161f7f0cff08eaa52b201fe387b9287994>`_
- Merge pull request #299 from vhalli/develop `6d5f2f800 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/6d5f2f800f8fb4a8bab6369e447923bdc21c2e65>`_
- Merge pull request #300 from fedora-infra/feature/mm2-fix-again `883b464dc <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/883b464dcd31fead4391df14a6f5b42b658382f3>`_
- Merge pull request #298 from opoplawski/copr `ec625c4aa <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/ec625c4aa086fd481873f83ed35d718725bf70e0>`_
- Rename this to Legacy so it gets hidden from the html docs. `d9a8a3c0f <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/d9a8a3c0f93fae6e7cb4cbca7fc2e110f06e741f>`_
- Adjust this to match. `c6ad8b491 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/c6ad8b4917f54f13247d444f196ea1ffb45ff075>`_
- Fix for #277 unhandled 'pagure.issue.drop' messages `1f727829a <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/1f727829aeac4bc102a9ceba67a8b826d301f6a9>`_
- Merge pull request #301 from Ghost-script/Fix `7ed111ccc <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/7ed111ccc2804827b10dbd0db48971640b30eb3f>`_
- Handle a case where there is a different nested message for the-new-hotness. `e39da1936 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/e39da193613680d5de9474fdacd2b8061f964c5e>`_
- Merge pull request #303 from fedora-infra/feature/handle-another-hotness-case `57bfb6ec3 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/57bfb6ec38cc01dbad1d250bdf3a3e8546d31121>`_
- Be **extra** careful. `edc7e61db <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/edc7e61db2e4eb02719136c2ebe4c87a0cd4b5d2>`_
- Merge pull request #304 from fedora-infra/feature/extra-careful `0f1f01a9e <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/0f1f01a9e1dc603da537332a341eb7e9f3b217a4>`_
- Update conglomerators for fedmsg API change. `e50a2b823 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/e50a2b823885ac1fe3939979ef52b1900b5a3f5e>`_
- Processor for bodhi.masher.start `4df2b4247 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/4df2b42471886333a9a7946a3f9a04234b23e781>`_
- Truncate bodhi update titles when they're ridiculous long. `055d24de0 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/055d24de0aef5f3fecb8436e22dd8449dac31a98>`_
- Merge pull request #309 from fedora-infra/feature/truncate-update-title `056b867e8 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/056b867e8194036895196670460fe39638ce6112>`_
- Merge pull request #308 from fedora-infra/feature/bodhi-mash-start `181db5834 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/181db5834d733fc699d95c0da9c44a01c0cf19ef>`_
- Merge pull request #305 from fedora-infra/feature/subjective-conglomeration `ef932e552 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/ef932e552740ae7bc2cdc248551684f1d26b3965>`_
- Handle edge-case in copr conglomerator. `f759b6c0c <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/f759b6c0c891fb8d82ac0e960a0a49652870e6ac>`_

0.1.9
-----

- @laarmen asked in #fedora-apps if we could invert the msg2emails dict to make things easier for email-centric debian infrastructure. `53971f006 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/53971f006a6bcec69ce2d89825a0929724694b24>`_
- Merge pull request #25 from fedora-infra/feature/invert-msg2emails `83b2d3388 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/83b2d33885f4758f5a7f5a931f5d718a8b27876e>`_
- Try to preserve some of that memory. `af74d218d <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/af74d218d3df49ee381b8e0495e016e6b8c4af09>`_
- Merge branch 'develop' of github.com:fedora-infra/fedmsg_meta_fedora_infrastructure into develop `6cf9bd865 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/6cf9bd865ee62ba15c28e225094932cffbb15aad>`_
- Update the link url for badges. `548b749c2 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/548b749c2093bbb16f2becb71e531fe1eea01e17>`_
- Revert "Update the link url for badges." `1fbef4ab6 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/1fbef4ab645004926194c9c3a18e4a06433815d1>`_
- AnsibleProcessor with tests. `c5a380b7f <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/c5a380b7f474c7a1ea2576c77d097cd26cee275f>`_
- Be more careful when constructing relative_playbook. `ca33e4b5a <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/ca33e4b5ac4e5bce9167c96bd5e8e8b4ad653a53>`_
- Merge branch 'feature/ansible' into develop `88d07f247 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/88d07f247c809d7794983d2777ad5aba32348d93>`_

0.1.8
-----

- Cover more cases when determining the tagger icon.  Fixes #21. `2a3db0417 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/2a3db04176ab21a14dc8a6cab71fef9889cc7d44>`_
- Correct/nicer link for badges. `f9ec367ac <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/f9ec367ac2283fa8b23468d63c82c3a846afb3c3>`_
- Merge pull request #22 from fedora-infra/feature/tagger-icon `4fbec04b1 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/4fbec04b18ab2b68c66684d6ecbd5ea2f60a6937>`_
- Merge pull request #23 from fedora-infra/feature/username-for-badge-links `76a168cd4 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/76a168cd40108ff06ce44898e21fef77a75ff993>`_
- [mediawiki] Nuke a '.' for consistency in subtitles. `3e361c43d <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/3e361c43de1d6fa6682a8cf1c77c60a628ae3a44>`_
- Merge pull request #24 from fedora-infra/feature/string-consistency `2809dc57d <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/2809dc57d3b8a7a13081b5d0df8158ec3623613d>`_
- Remove a period that was missed in a previous commit. `64888923d <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/64888923d8f0459846daf6dbe66e9b9c22fbd76a>`_
- Cache fas for irc msg2usernames and friends. `85b40d6fc <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/85b40d6fcbf0393ea459e79871f9dd9d9552f487>`_
- Mock out the fas cache during tests. `3d46f885c <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/3d46f885ced8bc1efdbb46a00b4ae0fef5a0e094>`_
- Random cleanups pointed out by @lmacken. `bda4c8c71 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/bda4c8c7190662c045a9591762a88756aadb722b>`_
- Be more careful with that default socket timeout. `6df24e52e <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/6df24e52ec45d1d8f4912df8efa076e1ee5e3483>`_
- Merge branch 'feature/fas-cache' into develop `bfa3fa45d <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/bfa3fa45d009639055383a165c038430f2d7724f>`_
- @relrod says people > persons `3d043f4de <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/3d043f4de63e5d469fc9936f0087575554d49a1e>`_

0.1.7
-----

- Added failing test for badge messages. `4a5826704 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/4a5826704953f01a221c62fb877ca5a47806d673>`_
- Update tests with a more current message example. `b29097948 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/b29097948f39d9aa2efd9ee6b889c3f1adca1a68>`_
- Add the processor for badges messages. `a6259e308 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/a6259e308ad254e2df277b1fa97e611361f49ac9>`_
- Merge pull request #20 from fedora-infra/feature/badges `fade3fdda <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/fade3fdda827f1d5722925cd0efad2e3832792c9>`_

0.1.6
-----

- Don't declare tickets open or closed unless the status has actually changed. `9e7b13a64 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/9e7b13a64dbc285ef68249dd7283b87c2df54000>`_
- Make PlanetProcessor.__name__ match the actual message topic `2140e1154 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/2140e1154f555bf2e3eb2e193d36d5154bbc0dfe>`_
- Reorganize fas shim to: `3512466f8 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/3512466f838c6761c66312a6ab5e9454079612db>`_
- Mailman3 processor and test. `aa71d2484 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/aa71d2484f665493aefff0e99cb1f1dba55c946f>`_
- PEP8 and corrections. `48a2c6183 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/48a2c61832f0fe888706fd4677b941744abdd0d2>`_
- The "references" header actually specifies whether or not it is a reply. `ca575bdd9 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/ca575bdd9588ec94b771b3e8f9af2dbdfb2bdec4>`_
- And... references can be None. `5ff1ea136 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/5ff1ea136e66dd586c7456a70ea48326dcdd53f3>`_
- Another test for mailman. `2762640f2 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/2762640f26ea286114ef1ca63bbfcbc7eab87266>`_
- Emit a warning and don't TB when handling an invalid mailman3 message. `b37d76d43 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/b37d76d43d64e0f1ba9eb2a79f27b7eabf124e9e>`_
- Check both "references" and "in-reply-to" headers when determining mailman3 subtitle. `8b01fb543 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/8b01fb543d385317abdf06dbca6cd3f82045dad7>`_
- Modify test to handle both cases. `aaca846d0 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/aaca846d0cb91d99901188f917e191bbc0bd2c88>`_
- Handle that dichotomy in the mailman .objects method, too. `694b4a1c6 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/694b4a1c647285805745e7b9ba751eb99f3189ce>`_
- Merge pull request #18 from fedora-infra/feature/mailman3 `2d672aafb <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/2d672aafb6a9a98b792e5c6689c88f979b2d8431>`_

0.1.5
-----

- Point all compose links at dl.fp.o. `77056aad2 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/77056aad208cdd32e4943547dca3333d8738f826>`_
- Add a local BaseProcessor that produces fedora-specific emails and gravatars for messages. `25816d49c <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/25816d49c1fffaaf0b8ad86513dc7f49ab5e49b6>`_
- Add an example email and avatar test. `2d52e4559 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/2d52e4559a6f2cc28899693abe98c01388cff0f5>`_
- Leave libravatar optional for now. `ce07184ac <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/ce07184ac365aebc5738f4ee63199654cec1d666>`_
- Merge pull request #13 from fedora-infra/feature/dl `1a7144ffa <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/1a7144ffae244a1f35e66e52a084d0f4581560d3>`_
- declare that encoding. `1e0c753ad <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/1e0c753add4aa4d6c8f49f60db79172f7dd9831b>`_
- Merge pull request #16 from fedora-infra/feature/avatars-and-emails `48d8b81cf <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/48d8b81cf07f5aac047b00bc5dd67f7e3286ceae>`_
- Initial test for trac messages. `75626ce7f <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/75626ce7f7f5b902ed36f26c592ae54407e23f8d>`_
- PEP8 `611e55925 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/611e559253449993a0a919903b95837aec1587d7>`_
- Correct a test topic. `e1d2b0cd5 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/e1d2b0cd5c23bdabc023ef9fc6e8662ab5226910>`_
- Add some fields we are going to need. `380cfd7c2 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/380cfd7c2f6be76e137e5e6bec515a7251543066>`_
- Trac processor implementation. `d858857b8 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/d858857b8094fd1da62bbbe0000d050aee0de141>`_
- Use appropriate base class. `af2183e0d <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/af2183e0d0b5b8eac3f06815454685e4845a1b7f>`_
- Merge pull request #17 from fedora-infra/feature/trac `3e46a0c91 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/3e46a0c9112b48b1eb3b2f08794cb1677ee23ef5>`_

0.1.4
-----

- Move tagger tests out into their own submodule. `ff128fe28 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/ff128fe287edcadc1e6ca432df714968ee873e64>`_
- Whoops.  Forgot to include this file. `49bb7e9f4 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/49bb7e9f49794972911b7c84f34660409dc75019>`_
- Test old and new tagger messages both. `2286df1d9 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/2286df1d9ed93461772e5dd3942188b663394290>`_
- Compatibility with old and new tagger messages. `a2ee0dd3b <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/a2ee0dd3b7ff78ee4e4035520c11347ee1781367>`_
- Add anonymous field to new messages. `9a4f37c76 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/9a4f37c766504eebe9138e4d1114a77da1925ef1>`_
- Add test for tagger rating changes. `5cb6f58bf <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/5cb6f58bf0436549b7db1ce379f70d4ff2ef29e5>`_
- Fix syntax errors. `5bcc4a0d5 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/5bcc4a0d58d70dc58bb8928e2405d84d00ac3205>`_
- Handle fedoratagger rating updates. `daecc80b3 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/daecc80b38a75c3e12a5b7b1392ee2e1fb20b381>`_
- Merge branch 'feature/tagger' into develop `8c6d7c0cd <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/8c6d7c0cd0928477945c92917a574fcb6735a32d>`_

0.1.3
-----

- Make sure we can handle a None for the user in koji messages. `3277e6016 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/3277e60160665c0158e89afd925812c38b4dc92a>`_
- Make messages make a little more sense when there is no owner of a koji build. `2311934ec <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/2311934ec8ebc7901fdc45172f7b2967c0d38632>`_
- Typofix. `bed16f607 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/bed16f607163af616b2bebbbe8603211076e0694>`_
- Be more careful with old pkgdb2branch messages from datanommer. `307a1cd5f <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/307a1cd5fe29e8c4d58e1686c4ab533e3562a005>`_

0.1.2
-----

- For dgilmore, remove the "for public consumption" clause. `e6addbe3f <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/e6addbe3fb3c8ca1eaefa98bb054b266b4ad4095>`_
- Rename __doc__ to .doc for the topics-to-doc script. `34c169793 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/34c169793a573a750a39cd8faef538d2f57cff25>`_
- Docstrings for askbot tests. `95967c2fc <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/95967c2fcf50218e44c7679bec62b18b5a50807f>`_
- Correct factual error. `6dcead744 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/6dcead744ab7259769e192c942ab53063d1ae1a6>`_
- Koji docstrings. `da06d7f2c <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/da06d7f2cc1e82f751110e0548707d5703a25428>`_
- Compose docstrings. `e7e7b08ea <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/e7e7b08ea8f30fcaee0e45a9839f2a520e829ff4>`_
- Pkgdb docstrings. `2cb033f2b <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/2cb033f2b273ea5672b91f26d19a164235c3bf3d>`_
- Planet docstrings. `c382b4846 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/c382b4846e7b4e54d7addc4df54ab5a0c1fe5484>`_
- s/OldStyle/Legacy/g `bf9ec9c4b <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/bf9ec9c4b332e01972beec617219681e747df8b3>`_
- FAS docstrings. `24e78b272 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/24e78b272e3f3b35b31d9783b8ebb39e194ca0a4>`_
- Bodhi docstrings. `f7339d401 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/f7339d401977644b8c638d42cd8bb653889bb392>`_
- Fix old test that I missed a long time ago. `92e863c85 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/92e863c855b65a1e004335053060a32849c0ed9f>`_
- Meetbot docstrings. `1752eca88 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/1752eca88924e96739a76437882cf150edda9039>`_
- Fedora Tagger docstrings. `e29fcdc9f <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/e29fcdc9f6dc4533aa45b67260bb51b6b79d4d10>`_
- Wiki docstrings. `341aad86d <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/341aad86dfc1fe79cf8072408d609051336b7225>`_
- pkgdb2branch messages. `4651e6f16 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/4651e6f163b54fd9eb302f4efc3d6db2aff14b35>`_
- SCM messages. `226b7e0fd <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/226b7e0fd182b1959234387294bd30b04ec7f9f9>`_
- Merge pull request #12 from fedora-infra/feature/docstrings-for-tests `a24c54cd9 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/a24c54cd9631816c838363f7cb7d16b031beaab7>`_

0.1.1
-----

- Use the non-https fedorahosted cgit url until infra#3672 is fixed. `916fb9973 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/916fb99733870ced83d1620d144eca8990f4f05c>`_
- Give up on askbot deep linking. `f63baad50 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/f63baad500eb49a41f9d6d070a9a99b1a99ad58c>`_
- Merge branch 'develop' of github.com:fedora-infra/fedmsg_meta_fedora_infrastructure into develop `732e0133f <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/732e0133f324e59ea8d754922d3482a63822a82e>`_
- Better debug of unhandled messages. `42527d43d <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/42527d43da061e8658715bcabdc0d71a1a22b583>`_
- Handle messages on the buildsys.package.list.change topic. `202fe1ec7 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/202fe1ec7aabcf865915690b026f19a7a70581da>`_
- Merge pull request #5 from fedora-infra/feature/better-debug `d2c5aeb5f <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/d2c5aeb5fa5f169bcacd0a5487ddd93d48730aab>`_
- Merge pull request #6 from fedora-infra/feature/the-missing-link `f910853ad <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/f910853ad19be9670f4037c077d6265fdc0cae59>`_
- The planet currently doesn't support https `08e667995 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/08e66799536b67225e8dc9995a06327865b20ffe>`_
- Handle topic changes from meetbot. `4fff9631d <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/4fff9631ddf24884cd9aa4ea496d651ffe4e5a6e>`_
- Handle links from koji package list changes. `b89e7269d <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/b89e7269de1fbf094013d809c1b4f8bacf949163>`_
- Satndardize absence of "object" prefix. `2f96c6c4a <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/2f96c6c4a4586d96cced71e04587a66a10c85e9f>`_
- Move compose tests out of the big test file (for organization's sake) `252445802 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/25244580241cb465c9a8d8d3c2a66e80b31d7319>`_
- Add message bodies to compose tests that are already being sent in production. `4bebe3a73 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/4bebe3a738a04473d9e7a4b7516518e73e9a91fd>`_
- Use actual branch name for "branched" compose messages. `43476f661 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/43476f661f3f51b2bca9eb4cc1e558990d12d1b3>`_
- Duplicate compose tests into legacy and newschool (over the addition of an "arch" field) `f6605fa0c <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/f6605fa0c726ef34a7a1f946f1da82526682f311>`_
- Secondary arch compose tests. `773578b38 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/773578b38f54249e5b6ddba806b5bd8c231291d6>`_
- Tweaks to primary compose tests. `49b26d5b9 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/49b26d5b9561ed07ace4bae1c461f6d56c5a92a9>`_
- Straighten compose processor out to meet the new tests. `287fc165e <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/287fc165e8bad3a82883a66ed9cf6a7ca83c686a>`_
- Merge pull request #7 from fedora-infra/feature/standardize-object-prefix `0b9cb2b7f <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/0b9cb2b7fd7b25de6cac33d1c8fba425461e9765>`_
- Merge pull request #10 from fedora-infra/feature/secondary-arch-compose `12b7f2ae2 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/12b7f2ae25ad8739dba2a0110f938234c9008e16>`_
- Merge pull request #9 from fedora-infra/feature/meetbot-topic-changes `166190804 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/166190804724bd41230408951e516cf61e67e077>`_
- Merge pull request #8 from fedora-infra/feature/koji-list-change-links `85e39afc0 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/85e39afc01a19b1cbc018f1d8c8b4bc6490219ce>`_

0.1.0
-----

- Use the bodhi 'agent' instead of the update submitter (fixes #113) `c5bceac66 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/c5bceac669782e4ffe70a7ec179eef318409cc1d>`_
- Add support for the new msg['agent'] to the bodhi unit tests. `fda949837 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/fda94983777358067e3bd314cb2f49b084398442>`_
- Set KojiProcessor.__name__ to 'buildsys' instead of 'koji'. `ecff43baf <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/ecff43baff22c275ff8e6c7862d4795f80eaadfd>`_
- Include the "tagger" in buildsys messages. `1e89b2cd7 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/1e89b2cd7a28d91b5dfcfbaab47d837e578c1cd0>`_
- Merge branch 'develop' of github.com:fedora-infra/fedmsg_meta_fedora_infrastructure into develop `385825ae8 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/385825ae85eb60114e141039e2c4c10064c2b78e>`_
- Set KojiProcessor.__name__ to 'buildsys' instead of 'koji'. `d1162492e <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/d1162492e5619cfeffb96af186f33fb4959d04ad>`_
- Merge branch 'develop' of github.com:fedora-infra/fedmsg_meta_fedora_infrastructure into develop `de19b5d6b <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/de19b5d6b29cf5cefdb2d25e6559b7d61350f03a>`_
- First round of tests for askbot plugin. `45ecb9b60 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/45ecb9b609742c8a6ba3cb2477b852975e1cab9d>`_
- All askbot handlers except for subtitle. `1d54042f2 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/1d54042f2ade37f77623b94e9a5f9a7ad6789ca0>`_
- Some subtitle for post edits. `7c82aff2d <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/7c82aff2d9800afd91564935824b7b718d68b57a>`_
- Fixes to one deletion test. `989ffa582 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/989ffa582c29de74b59c7d18435ee77c0f03b7bf>`_
- Last of the subtitle code for askbot. `e0a96d96c <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/e0a96d96cefc1b6fcb9d22f9aa068228bcb2f0e1>`_
- pep8 `746984328 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/74698432813a723f079d6df656db1672e9b68c6b>`_
- Little tweaks. `1e722d1cb <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/1e722d1cb4fc9e16503ad4789a7334872a1c8fc5>`_
- s/pkgdb/askbot/ `6f1778a9c <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/6f1778a9c3c7921f1dcf930d7474504c88947976>`_
- Move some tmpl.format calls out a level of nesting for simplicity's sake. `4860bc08b <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/4860bc08bd5540791cd23f011238d39c545b3813>`_
- Merge branch 'feature/askbot' into develop `79a455bf4 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/79a455bf476006f56ed0e87b8322ff1a4e256382>`_
- Handle old-style scm messages. `0af3e1981 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/0af3e19818edd95d1ef0ab951b29cf63552daf87>`_
- For koji, use http links, not https. `16325cd5a <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/16325cd5a6d48a1db72b1321ca6902bf09d4f2db>`_
- Use https for compose messages, not http. `1dd78964b <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/1dd78964b245e530c611b898103f99f504e98762>`_
- Merge pull request #2 from fedora-infra/feature/http-not-https `5f2540646 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/5f2540646cbeb2857e02cf092b7b956c4c61e384>`_
- Merge pull request #3 from fedora-infra/feature/https-not-http `05d39c33f <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/05d39c33f72d57c40c19159fa14852be364a36dd>`_
- Fix up koji tests after the https shuffle. `10e3c6268 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/10e3c626893f4e113981bc62d59ebbb6c1cceb9c>`_

0.0.9
-----

- STATE 1 is "closed" `9d7bb2275 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/9d7bb227569ae2dac678726306bb74a52a312569>`_
- Much better.  Use the correct enums from koji. `2466d2b9f <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/2466d2b9ffea0da446bee238046c0236a745efce>`_
- Handle new and old style fas messages. `b4962173e <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/b4962173ec0b07a02e59715a5d80342e96833f3c>`_
- Handle usernames and links in koji messages. `4ee46b0f7 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/4ee46b0f73b58605e1af0f6f55459ebe507184ae>`_

0.0.8
-----

- Planet Processor. `f4ba3a0b8 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/f4ba3a0b871716bc800cfbf24a505e62404698e8>`_
- Stubs for buildsys.tag. `0a6c6e1d6 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/0a6c6e1d69db0f8ca9e4f77f28b3a07682c1f92b>`_
- Handle some build state changes. `02c612e54 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/02c612e540556a2a1c9fa866a4cc0e4e16c4dbca>`_
- buildsys untag and repo.ini messages. `b4db03029 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/b4db0302961fe3139b6181664673cd6db9e9bfe8>`_
- One last koji message type. `18eef2a3e <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/18eef2a3eefeca6afe4c05f0b92c210fd727a068>`_

0.0.7
-----

- Updates for git topics. `aaca74704 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/aaca74704b9470a846e1bd25ea88b3ba661efd80>`_
- 0.0.6 `5ce1a8027 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/5ce1a8027ce0fe4d139d8d73fd9abe6248445095>`_
- Fix to git.lookaside messages. `a1abbc0ab <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/a1abbc0ab186eb0560e8924dd85298c931185b37>`_

0.0.5
-----

- Support for new git/scm messages. `de2bc9570 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/de2bc9570b08a7db0f7a456a7bb2cb61668e75bb>`_
- Same for lookaside messages. `751b86b3b <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/751b86b3bb9e81bf5812d5a514c4e765af14ea5b>`_

0.0.4
-----

- Added a config for tests. `a0e9db882 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/a0e9db8826f5292c10c1612ceeb35a8b534a404a>`_
- Change namespace to fix tests. `c509d0787 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/c509d078773c4b6bb94c9b81c3b187c964bc4560>`_
- First pkgdb messages. `11e50b58b <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/11e50b58bc8c8274aebb39d9d710ddb1db70cdce>`_
- TODO list. `bb805e545 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/bb805e545ae81995840d8cc27f383e9a5f3c259a>`_
- pkgdb.owner.update. `126579c3f <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/126579c3f69d9dfb099387ccf315b22d8ffc4c47>`_
- pkgdb.acl.request.toggle. `4ca441a9d <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/4ca441a9dc8b61ce3f965aa795d658fc33e7b29d>`_
- grammar `a460e9ec3 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/a460e9ec3d8f8404005cfb93b449b19a0f7daced>`_
- pkgdb.package.retire. `aae5bb1fc <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/aae5bb1fcc0bff32690bed37c36cc0f8d70ba1aa>`_
- todo update. `b665aa428 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/b665aa428e9098eb267c7c6b370295f1227b4eff>`_
- pkgdb.acl.user.remove. `93372562a <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/93372562a25a6d6755362ebe40678d2cbebf6177>`_
- pkgdb.package.new. `112ca191f <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/112ca191ff34e2f400c1677bcc168210be58c791>`_
- pkgdb.package.update. `41357a555 <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/41357a55596ecd40c926438205e31b6adf4eafb6>`_
- pkgdb.branch.clone. `5402557bc <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/5402557bc3382c47fb9b384f749d06da5d9d292a>`_

0.0.3
-----

- s/fedmsg.text/fedmsg.meta/g `eb05cfe8a <https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/commit/eb05cfe8a0499323f1958a2f406e36d65a3edb8e>`_
