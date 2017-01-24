class myTemplate(object):
    name = "myTemplate"
    style = 'camelCase' # can also be snakeCase
    getter = """ 
    /**
    * Gets the %(description)s.
    *
    * @return %(type)s
    */
    public function get%(normalizedName)s()
    {
        return $this->%(name)s;
    }
"""

    setter = """ 
    /**
    * Sets the %(description)s.
    *
    * @param %(type)s $%(name)s the %(humanName)s
    *
    * @return self
    */
    public function set%(normalizedName)s(%(typeHint)s $%(name)s)
    {
        $this->%(name)s = $%(name)s;
    }
"""