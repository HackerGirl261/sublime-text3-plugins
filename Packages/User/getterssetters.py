import sublime, sublime_plugin, re, os

class GeneratorCommand(sublime_plugin.TextCommand):

  def fixup(self, string):
    return re.sub(r'\r\n|\r', '\n', string.decode('utf-8'))

  def formalName(self, rawName):
      return u"%s" % "".join([part.title() for part in rawName.split("_")])

  def run(self, edit):

    output = u"\n"

    setterTemplate = """
  public function set%s($%s)
  {
    $this->%s = $%s;
  }
"""

    getterTemplate = """
  public function get%s()
  {
    return $this->%s;
  }
"""

    propertyTemplate = """%s
%s
"""

    prefixPrivateSize = len(u"private $")
    prefixPublicSize = len(u"public $")
    prefixProtectedSize = len(u"protected $")

    # get current buffer
    bufferLength  = sublime.Region(0, self.view.size())
    bufferContent = self.view.substr(bufferLength).encode('utf-8')

    for line in bufferContent.split("\n"):
      if line.strip().startswith("private $") or line.strip().startswith("protected $") or line.strip().startswith("public $"):
          #trim of the private $ and trailing semi-colon
          if line.strip().startswith("private $"):
            realName = line.strip()[prefixPrivateSize:-1]
          elif line.strip().startswith("public $"):
            realName = line.strip()[prefixPublicSize:-1]
          elif line.strip().startswith("protected $"):
            realName = line.strip()[prefixProtectedSize:-1]
          #output += propertyTemplate % ( setterTemplate %(self.formalName(realName)), getterTemplate % (self.formalName(realName)))
          formalName = self.formalName(realName)
          setTemplate = setterTemplate %( formalName, realName, realName, realName)
          getTemplate = getterTemplate %( formalName, realName)
          output +=  propertyTemplate % (setTemplate, getTemplate)
    #(row,col) = self.view.rowcol(self.view.sel()[0].begin())
self.view.insert(edit, self.view.size(), self.fixup(output))