$(document).ready(function() {
  // add toggle functionality to abstract and bibtex buttons
  // height is measured via scrollHeight rather than a fixed max-height,
  // so the open/close transition matches the actual content size
  function setPanelOpen($panel, open) {
    if (open) {
      $panel.addClass('open');
      $panel.css('max-height', $panel.prop('scrollHeight') + 'px');
    } else {
      $panel.removeClass('open');
      $panel.css('max-height', '0px');
    }
  }

  function bindToggle(triggerClass, otherClass) {
    $('a.' + triggerClass).click(function() {
      var $entry = $(this).parent().parent();
      var $panel = $entry.find('.' + triggerClass + '.hidden');
      var $otherPanel = $entry.find('.' + otherClass + '.hidden.open');

      if ($otherPanel.length) {
        setPanelOpen($otherPanel, false);
        $entry.find('a.' + otherClass).removeClass('active');
      }

      var isOpen = $panel.hasClass('open');
      setPanelOpen($panel, !isOpen);
      $(this).toggleClass('active', !isOpen);
    });
  }

  bindToggle('abstract', 'bibtex');
  bindToggle('bibtex', 'abstract');
  $('a').removeClass('waves-effect waves-light');

  // bootstrap-toc
  if($('#toc-sidebar').length){
    var navSelector = "#toc-sidebar";
    var $myNav = $(navSelector);
    Toc.init($myNav);
    $("body").scrollspy({
      target: navSelector,
    });
  }

  // add css to jupyter notebooks
  const cssLink = document.createElement("link");
  cssLink.href  = "../css/jupyter.css";
  cssLink.rel   = "stylesheet";
  cssLink.type  = "text/css";

  let theme = localStorage.getItem("theme");
  if (theme == null || theme == "null") {
    const userPref = window.matchMedia;
    if (userPref && userPref("(prefers-color-scheme: dark)").matches) {
      theme = "dark";
    }
  }

  $('.jupyter-notebook-iframe-container iframe').each(function() {
    $(this).contents().find("head").append(cssLink);

    if (theme == "dark") {
      $(this).bind("load",function(){
        $(this).contents().find("body").attr({
          "data-jp-theme-light": "false",
          "data-jp-theme-name": "JupyterLab Dark"});
      });
    }
  });
});

