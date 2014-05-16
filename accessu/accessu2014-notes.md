# AccessU 2014 Notes

This year was my first AccessU (and my first trip to Austin!), and I attended sessions in the development and testing tracks, mostly. My tweets were well-received, so I thought I'd make a page of my notes and the resources that were shared by presenters and attendees.

Here's the full class list: [AccessU 2014 Schedule](http://www.knowbility.org/v/accessu-course-list/John-Slatin-AccessU/3i/)

You can also [read these notes in their original tweet form](https://twitter.com/search?f=realtime&q=%23AccessU%20from%3Adevonpersing).

A few acronyms I use:

* **a11y** is short for accessibility.
* **AT** is assitive technology, such as screen readers, braille readers, other text-to-something technologies, guided access, screen magnifiers, etc.
* **SR** is screen reader.
* **JS** is JavaScript.
* **PwD** is a _person_ with a disability or disabilities, or _people_ with disabilities.

## Monday

### Integrating Accessibility into Agile, Continuous Development

_Susann Keohane and Mary Jo Mueller_

### Modern Web Accessibility with JavaScript and WAI-ARIA

_Paul J. Adam_
[@pauljadam](https://twitter.com/pauljadam) on Twitter  
[pauljadam.com](http://pauljadam.com/)

### Personas, Buy-in Sessions, and Tips to Bring Accessibility to Life

_Shawn Henry_  
[@shawn_slh](https://twitter.com/shawn_slh) on Twitter
[Profile at W3C WAI](http://www.w3.org/People/Shawn/)

### CSS3/JavaScript Selectors

_Estelle Weyl_  
[@standardista](https://twitter.com/standardista) on Twitter  
[standardista.com](http://standardista.com/)

[CSS3/JavaScript Selectors slides](http://estelle.github.io/selectors/)

* Don't import a JS library just to target nodes. Use `querySelector` and `querySelectorAll` in native JS with modern selectors.
* The modern selector list works in IE9 and later.
* Check out the slides for demos and cheat sheets!

## Tuesday

### iAccessibility (iOS/iPhone/iPad)

_Paul J. Adam_

[iAccessibility slides](http://pauljadam.com/iaccessibility/)

[previous version of the talk focusing on iOS 6](http://pauljadam.com/ia11y/#ia11y)

* Slides from this talk were build using the a11y friendly jQuery Mobile framework.
* Apple started doing a11y in iOS in earnest in 2003, and has expanded support from vision issues only to support for hearing, learning/cognitive, physical and motor skill issues.
* iOS Guided Access, which allows users to hide certain UI elements, comes with an API that allows developers to detect the mode and adjust the UI to it. This is also helpful for devices placed in an kiosk mode.
* iOS 7 allows multiple a11y supports to be assigned to the triple-click home button shortcut. If multiple options are assigned, the OS will ask you which you want to turn on or off via a dialog.
* iOS 7 useres can customize the look fo Web VTT captions to meet their personal needs and preferences.
* Introducing a11y supports early can help people adapt as a disability worsens. For example, helping a person learn VoiceOver on their phone as their vision starts to fail will make it easier for them to rely on it when their vision is lost completely.
* VoiceOver on iOS (like JAWS) will try to guess form labels if not are explicitly assigned, based on the proximity of text.
* iOS provides a variety of supports outside of a11y settings that can be helpful for PwD, such as location-based reminders, custom notification vibrations, and speaking selected text.

### Consistency in Expert Accessibility Testing

_Glenda Sims_
[@goodwitch](https://twitter.com/goodwitch) on Twitter

* Experts can spend wildly different amounts of time on the same task, and can report wildly different numbers of issues, depending on how they test and report. For example, Deque ran an experiment where 9 experts each tested the same page against WCAG. their tests lasted from 1 to 8.5 hours, numbers of errors reported ranged from 1 to more than 35. Part of what was learned was the need for better internal standards for testing, but also standarizing how errors and issues should be reported.
* Just like regular code reviews for developers, consistency requires peer review for designers, devs, testers, and a11y experts.
* Manual testing at scale requires a combination of checklists and brains (brains first!).
* Share out work between types of testers: Provide clear checklists to QA staff, and enlist analysts to make calls about WCAG, best practices, and browser/AT bugs.
* When in doubt, lean toward standards-based screen readers and screen readers that are free.
* One way to achieve browser/AT coverage and catch each others mistakes is to spread out testing different combinations along the cycle of a project. Have devs use NVDA and Firefox, and have testers use JAWS and IE, for example.
* Sometimes testing means reporting bugs to AT companies and browser vendors. Sometimes major bugs require workarounds to be created.
* Clearly differentiate between WCAG 2.0 Level AA (or other guideline) violations and best practice recommendations.
* Create a customized guide for clients that leverages that standards they are targeting but is tailored to fit their design, dev, and testing practices.
* Goal for testing and reporting is equal access, accurate and consisten report of barriers and solutions, and efficient use of limited resources for testing.
* End goal is happy PwDs who can use the site/software, experts who don't hate their jobs, and clients.

### Sustainable A11y: Long-term Monitoring and Reporting

_Glenda Sims_

### Android Web & Native Accessibility in 4.4 KitKat

_Paul J. Adam_

## Wednesday

### Responsive Web Design

_Derek Featherstone_

## Resources

These resources came out of a variety of sessions.

### Technologies and Specs

* [Evolution of Accessibility in iOS: Screenshots of iOS 3.0 to 7.0 Accessibility Settings](http://pauljadam.com/iaccessibility/#evolution)
* [WebVTT: The Web Video Text Tracks Format](http://dev.w3.org/html5/webvtt/) W3C spec

### Automated Testing

Note that JavaScript bookmarklet and favelet tools can be used on mobile/tablet devices as well as desktop.

* [HTML CodeSniffer bookmarklet](http://squizlabs.github.io/HTML_CodeSniffer/)
* [Jim Thatcher's favelets](http://jimthatcher.com/favelets/)

### Demos

* [HTML5 Video Accessibility](http://www.pauljadam.com/demos/html5-video-a11y.html)
* [HTML5 Input Types Demo](http://www.pauljadam.com/demos/html5-input-types.html)
* [University of Washington Accessible University 2.0 before and after demo](http://www.washington.edu/accesscomputing/AU/)
* [Form related UI psuedo-classes](http://estelle.github.io/selectors/#slide21) for styling form validation based on `aria-required` states and HTML5 form input attributes

### Cheatsheets

* [WAI-ARIA Support Matrix](http://www.pauljadam.com/demos/ariasupport.html) for common ARIA attributes, for VoiceOver (on OSX and iOS with Safari) and TalkBack (on Android with Firefox and Chrome)
