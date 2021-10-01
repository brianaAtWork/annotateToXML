//S100EXT:SurfacePropertyType
//S100:DataSetIdentificationType
//S100:DataSetStructureInformationType
//
//source xsd missing MetaFeatureType (DataCoverage)
//DataCoverage.geometry missing maxOccurs

var prop = Object.defineProperty
var controller = null

class SimpleType {
    constructor(name, description) {
        this.name = name
        this.description = description
    }

    clean(value) {
        return value
    }

    validate(value) {
        return false
    }

    get annotation() {
        //check if the element has a direct annotation
        var annotation = this.description.querySelector("annotation")

        if (!annotation) {
            annotation = this.typeElement ? this.typeElement.querySelector("annotation") : null
        }

        if (annotation) {
            return annotation.textContent.trim()
        }
        else {
            return ""
        }
    }

    //just return the type for the base class
    //meant to be reimplemented
    get dataElement() {
        var type = document.createElement("span")
        type.innerText = this.dataType

        return type
    }

    get dataType() {
        return this.description.attributes.type.value
    }

    get field() {
        var dataElement = this.dataElement

        var label = this.label
        label.append(": ", dataElement)

        var field = document.createElement("div")
        field.className = "field"
        field.append(label)

        if (this.annotation) {
            var tooltip = document.createElement("span")
            tooltip.className = "field-annotation"
            tooltip.innerText = "?"
            tooltip.title = this.annotation 
            field.append(tooltip)
        }

        return field
    }

    get label() {
        var name = document.createElement("label")
        name.innerText = this.titleCaseName

        if (this.required) {
            name.style.fontWeight = "bold"
        }

        return name
    }

    get multiple() {
        if (!("maxOccurs" in this.description.attributes)) {
            return false
        }
        else {
            return this.description.attributes.maxOccurs.value == "unbounded" 
        }
    }

    get required() {
        if (!("minOccurs" in this.description.attributes)) { 
            return false
        }
        else {
            return this.description.attributes.minOccurs.value > 0 
        }
    }

    get titleCaseName() {
        return this.name
            .replace(/[A-Z]/g, " $&")
            .replace("Rx N", "RxN")
            .toTitleCase()
            .replace(/^The /, "")
            .replace(/([A-Z]) /g, "$1")
            .replace(/([A-Z]+)([A-Z])/, "$1 $2")
    }

    get typeElement() {
        var type = this.description.attributes.type.value
        return this.description.getRootNode().querySelector(sprintf("simpleType[name='%s'], complexType[name='%s']", type, type))
    }
}

class BooleanSimpleType extends SimpleType{
    constructor(name, description) {
        super(name, description)
    }

    validate(value) {
        return typeof(value) == "boolean"
    }

    get dataElement() {
        var input = document.createElement("input")
        input.type = "checkbox"

        return input
    }
}

class DateSimpleType extends SimpleType {
    constructor(name, description) {
        super(name, description)
    }

    get dataElement() {
        var input = document.createElement("input")
        input.type = "date"

        //do check for date type

        return input
    }
}

class DecimalSimpleType extends SimpleType {
    constructor(name, description) {
        super(name, description)

        this.minimum = null
        this.maximum = null
    }

    clean(value) {
        return parseFloat(value)
    }

    validate(value) {
        return true
    }

    get dataElement() {
        var input = document.createElement("input")
        input.type = "number"
        input.style.width = "40px"

        if (this.maximum) {
            input.max = this.maximum
        }

        if (this.minimum) {
            input.min = this.minimum
        }

        return input
    }
}

class NonNegativeDecimalSimpleType extends DecimalSimpleType {
    constructor(name, description) {
        super(name, description)

        this.minimum = 0
    }

    validate(value) {
        return value > -1
    }
}

class Decimal0To360SimpleType extends DecimalSimpleType {
    constructor(name, description) {
        super(name, description)

        this.minimum = 0
        this.maximum = 360
    }

    validate(value) {
        return  value >= 0 && value <= 360
    }
}

class IntegerSimpleType extends DecimalSimpleType {
    clean(value) {
        return parseInt(value)
    }
}

class Integer0To360SimpleType extends IntegerSimpleType {
    constructor(name, description) {
        super(name, description)

        this.minimum = 0
        this.maximum = 360
    }

    validate(value) {
        return  value > -1 && value < 361
    }
}

class NonNegativeIntegerSimpleType extends IntegerSimpleType {
    constructor(name, description) {
        super(name, description)

        this.minimum = 0
    }

    validate(value) {
        return value > -1
    }
}


class PositiveIntegerSimpleType extends IntegerSimpleType {
    constructor(name, description) {
        super(name, description)

        this.minimum = 1
    }

    validate(value) {
        return  value > 0
    }
}

class RestrictedStringSimpleType extends SimpleType {
    constructor(name, description, restriction) {
        super(name, description)

        this.restriction = restriction
    }

    validate(value) {
        //FIXME add check for pattern restriction
        return this.restriction.querySelector(sprintf("enumeration[value='%s']", value)) != null
    }

    get dataElement() {
        var values = Array.from(this.restriction.querySelectorAll("enumeration")).map(e => e.attributes.value.value.trim()).sort()

        //restriction is a set of values
        if (values.length > 0) {
            var select = document.createElement("select")
            if (!values.includes("")) {
                values.unshift("")
            }
    
            values.forEach(function(value) {
                var option = document.createElement("option")
                option.attributes.value = value
                option.innerText = value.toTitleCase()
                select.append(option)
            })
    
            return select
        }
        //other kind of restriction, assuming there's a length for now
        else {
            var input = document.createElement("input")
            var length = this.restriction.querySelector("length")

            if (length) {
                input.maxLength = length.attributes.value.value
                input.minlength = length.attributes.value.value
            }

            return input
        }
    }
}

class StringSimpleType extends SimpleType {
    constructor(name, description) {
        super(name, description)
    }

    //security issues with free text?
    //maybe none if all data stays local?
    validate(value) {
        return true
    }

    get dataElement() {
        var textArea = document.createElement("textarea")
        textArea.style.height = "5em"
        textArea.style.marginLeft = "20px"
        textArea.style.verticalAlign = "top"
        textArea.style.width = "50%"

        return textArea
    }
}

var simpleTypeForElement = function(element) {
    var name = element.attributes.name.value
    var type = element.attributes.type.value

    //will need to make more complex checks later
    if (type == "xs:boolean") {
        return new BooleanSimpleType(name, element)
    }
    else if (type == "xs:date") {
        //needs to be returned as YYYY-MM-DD[time stuff]
        return new DateSimpleType(name, element)
    }
    else if (type == "xs:string") {
        return new StringSimpleType(name, element)
    }
    else if (type == "xs:decimal") {
        return new DecimalSimpleType(name, element)
    }
    else if (type == "NonNegativeDecimal") {
        return new NonNegativeDecimalSimpleType(name, element)
    }
    else if (type == "Decimal0.0To360.0") {
        return new Decimal0To360SimpleType(name, element)
    }
    else if (type == "xs:integer") {
        return new IntegerSimpleType(name, element)
    }
    else if (type == "xs:nonNegativeInteger") {
        return new NonNegativeIntegerSimpleType(name, element)
    }
    else if (type == "xs:positiveInteger") {
        return new PositiveIntegerSimpleType(name, element)
    }
    else if (type == "Integer0To360") {
        return new Integer0To360SimpleType(name, element)
    }
    else if (type == "gml:ReferenceType") {
        return new SimpleType(name, element)
    }
    //check non base types
    else {
        var typeElement = element.getRootNode().querySelector(sprintf("simpleType[name='%s'], complexType[name='%s']", type))

        if (!typeElement) {
            return new SimpleType(name, element)
        }
        else if (typeElement.querySelector("restriction")) {
            var restrictionType = typeElement.querySelector("restriction").attributes.base.value

            if (restrictionType == "xs:string") {
                return new RestrictedStringSimpleType(name, element, typeElement.querySelector("restriction"))
            }
            else {
                return new SimpleType(name, element)
            }
        }
        else {
            return new SimpleType(name, element)
        }
    }
}

class ComplexType {
    constructor(name, description) {
        this.name = name
        this.description = description
    }
    _loadElements() {
        var description = this.description
        
        this._elementsByBase = {"":[]}
    
        var elements = description.querySelectorAll("sequence > element")
    
        for (var i = 0; i < elements.length; ++i) {
                    this._elementsByBase[""].push(simpleTypeForElement(elements[i]))
        }
    
        while (description) {
            var extension = description.querySelector("extension")
            if (extension && !extension.attributes.base.value.includes(":")) {
                var base = extension.attributes.base.value
                this._elementsByBase[base] = []
    
                description = extension.ownerDocument.querySelector(sprintf("complexType[name='%s']", base))
            
                var elements = description.querySelectorAll("sequence > element")
    
                for (var i = 0; i < elements.length; ++i) {
                    this._elementsByBase[base].push(simpleTypeForElement(elements[i]))
                }
            }
            else {
                break
            }
        }
    }

    get annotation() {
        var annotation = this.description.querySelector("annotation")

        if (annotation) {
            return annotation.textContent.trim() 
        }
        else {
            return "No description available"
        }
    }

    get elementsByBase() {
        if (!this._elementsByBase) {
            this._loadElements()
        }
        return this._elementsByBase
    }
}

class View {
    constructor(id, elementType, mainElement, delegate) {
        this.id = id
        this.mainElement = mainElement
        this.delegate = delegate

        this.element = document.createElement(elementType)
        this.element.setAttribute("id", id)
    
        mainElement.append(this.element)
    }
}

class DraggedTextView extends View {
    constructor(id, mainElement, delegate) {
        super(id, "div", mainElement, delegate)
    
        this.element.setAttribute("contenteditable", "true")
        this.element.innerText = "Drag a text file or paste text"
    
        var view = this
        this.element.addEventListener("drop", function(e) {
            e.stopPropagation()
            e.preventDefault()
    
            var file = e.dataTransfer.files[0]
            var fileReader = new FileReader()
            
            fileReader.readAsText(file)
            fileReader.onload = function(readEvent) {
                view.element.innerText = readEvent.target.result
            }
        })
    }
}

class TypeView extends View {
    constructor(id, mainElement, delegate) {
        super(id, "select", mainElement, delegate)
        this.element.setAttribute("size", 6)
    
        var tv = this
        delegate.typeNames.forEach(function(type) {
            var option = document.createElement("option")
            option.innerText = type
            option.onmouseenter = function() { 
                delegate.typeViewHoverStartForType(tv, type)
            }
            option.onmouseleave = function() {
                delegate.typeViewHoverEnd(tv)
            }
            tv.element.append(option)
        })
    
        this.element.onchange = function() {
            delegate.typeViewSelectedType(tv, tv.element.value)
        }
    }
}

class TypeAnnotationView extends View {
    constructor(id, mainElement, delegate) {
        super(id, "div", mainElement, delegate)
    }
}

class FormView extends View { 
    constructor(id, mainElement, delegate) {
        super(id, "form", mainElement, delegate)
    }
    formForComplexType(complexType) {
        this.element.innerHTML = ""
    
        var bases = Object.keys(complexType.elementsByBase).sort()
        
        var view = this
        bases.forEach(function(base) {
            if (base) {
                var line = document.createElement("hr")
                var baseName = document.createElement("div")
                baseName.style.textDecoration = "underline"
                baseName.innerText = sprintf("From %s", base.replace(/Type$/, ""))
                view.element.append(line, baseName)
            }
    
            complexType.elementsByBase[base].forEach(function(element) {
                view.element.append(element.field)
            })
        })
    }
}

//TypeViewDelegate
//  methods
//      typeViewHoverEnd(tv)
//      typeViewHoverStartForType(tv, type)
//      typeViewSelectedType(type)
//
//  instance variables
//      selectedType
//
//  properties
//      typeNames - sorted list of type names
class XSDController {
    constructor(xsds, namespace, mainElement) {
        this.xsds = xsds
        this.namespace = namespace
        this.mainElement = mainElement
    
        this.types = {}
        this.views = {}
    
        this.selectedType = null
    
        //convenience properties
        this._ns = null
        if (namespace.endsWith(":")) {
            this._ns = namespace
        }
        else {
            this._ns = sprintf("%s:", namespace)
        }

//      this._loadXSD("S127.xsd")
    
        //get types from xsd
        var c = this
        this.xsds.forEach(function(xsd) {
            xsd.querySelectorAll("schema > complexType").forEach(function(e) {
                var name = e.attributes.name.value
                var description = e
        
                //skip IMemberType and MemberType
                if (name.match(/^I?MemberType$/)) { return }
        
                //skip DatasetType
                if (name == "DatasetType") { return }
        
                c.types[name] = new ComplexType(name, description)
            })
        })
    
        //set up views
        this._addViews()
    }

    _addViews() {
        this.views.textEntry = new DraggedTextView("chapter_text", this.mainElement, this)
        this.views.typeSelection = new TypeView("complex_types", this.mainElement, this)
        this.views.annotation = new TypeAnnotationView("annotation", this.mainElement, this)
        this.views.form = new FormView("form", this.mainElement, this)
    }

    _loadXSD(filename) {
        console.log(filename)

        var c = this

        new Promise(function(resolve, reject) {
            $.ajax(sprintf("/media/xsd/%s", filename)).done(function(data) {
                c.xsds[filename] = data
                data.querySelectorAll("import").forEach(function(e) {
                    var path = e.attributes.schemaLocation.textContent.replace(/.*\//, "")

                    c._loadXSD(path)
                })
                data.querySelectorAll("schema > complexType").forEach(function(e) {
                    var name = e.attributes.name.value
                    var description = e
            
                    //skip IMemberType and MemberType
                    if (name.match(/^I?MemberType$/)) { return }
            
                    //skip DatasetType
                    if (name == "DatasetType") { return }
            
                    c.types[name] = new ComplexType(name, description)
                })
                resolve(data)
            })
        })
    }

    get typeNames() {
        return Object.keys(this.types).sort((a,b) => a.toLowerCase() > b.toLowerCase())
    }

    //general methods
    _annotatingHoverEnd() {
        if (this.selectedType) {
    //      this.views.annotation.element.innerText = this.types[this.selectedType].annotation
            this._updateAnnotationForType(this.selectedType)
        }
        else {
            this.views.annotation.element.innerText = ""
        }
    }
    _updateAnnotationForType(type) {
        this.views.annotation.element.innerText = this.types[type].annotation
    }
    
    //TypeViewDelegate
    typeViewHoverEnd(tv) {
        this._annotatingHoverEnd()
    }
    typeViewHoverStartForType(tv, type) {
        this._updateAnnotationForType(type)
    }
    typeViewSelectedType(tv, type) {
        this.selectedType = type
        this._updateAnnotationForType(type)
        this.views.form.formForComplexType(this.types[type])
    }
}

$(document).ready(function() {
    $.ajax("/media/xsd/S127.xsd").done(function(data, status, xhr) {
        controller = new XSDController([data], "S127", document.getElementById("coast"))
    })
    
//  controller = new XSDController("S127", document.getElementById("coast"))
})
