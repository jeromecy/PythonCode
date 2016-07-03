//
//  localmodel.swift
//  single
//
//  Created by Jerome Cao on 3/07/16.
//  Copyright © 2016 Jerome Cao. All rights reserved.
//

import Foundation

class localmodel: NSObject {
    
    //properties
    
    var date: String?
    var base: String?
    var tran: String?
    var curr: NSNumber?
    
    
    //empty constructor
    
    override init()
    {
        
    }
    
    //construct with @name, @address, @latitude, and @longitude parameters
    
    init(date: String, base: String, tran: String, curr: NSNumber) {
        
        self.date = date
        self.base = base
        self.tran = tran
        self.curr = curr
        
    }
    
    
    //prints object's current state
    
    override var description: String {
        return "On date: \(date), 1: \(base), = \(curr) \(tran)"        
    }
    
    
}