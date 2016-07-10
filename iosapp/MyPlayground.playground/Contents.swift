//: Playground - noun: a place where people can play

import UIKit

let url = NSBundle.mainBundle().URLForResource("data", withExtension: "json")
let data = NSData(contentsOfURL: url!)


func readJSONObject(object: [String: AnyObject]) {
    guard let title = object["dataTitle"] as? String,
        let version = object["swiftVersion"] as? Float,
        let users = object["users"] as? [[String: AnyObject]] else { return }
    _ = "Swift \(version) " + title
    
    for user in users {
        guard let name = user["name"] as? String,
            let age = user["age"] as? Int else { break }
        switch age {
        case 22:
            _ = name + " is \(age) years old."
        case 25:
            _ = name + " is \(age) years old."
        case 29:
            _ = name + " is \(age) years old."
        default:
            break
        }
    }
}

do {
    let object = try NSJSONSerialization.JSONObjectWithData(data!, options: .AllowFragments)
    if let dictionary = object as? [String: AnyObject] {
        readJSONObject(dictionary)
    }
} catch {
    // Handle Error
}




var myvar=20
let mar=20.0
myvar=30

let optionalInt: Int? = 9
let actualInt: Int = optionalInt!


let implicitInteger = 70
let implicitDouble = 70.0
let explicitDouble: Double = 70


var st="ab"
Int(st)

let vegetable = "red pepper"
switch vegetable {
case "celery":
    let vegetableComment = "Add some raisins and make ants on a log."
case "cucumber", "watercress":
    let vegetableComment = "That would make a good tea sandwich."
case let x where x.hasSuffix("pepper"):
    let vegetableComment = "Is it a spicy \(x)?"
default:
    let vegetableComment = "Everything tastes good in soup."
}


func greet(name: String, day: String) -> String {
    return "Hello \(name), today is \(day)."
}




greet("a",day: "today")



