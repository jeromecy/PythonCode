//
//  homemodel.swift
//  single
//
//  Created by Jerome Cao on 3/07/16.
//  Copyright © 2016 Jerome Cao. All rights reserved.
//

import Foundation

protocol HomeModelProtocal: class {
    func itemsDownloaded(items: NSArray)
}


class homemodel: NSObject, NSURLSessionDataDelegate {
    
    //properties
    
    weak var delegate: HomeModelProtocal!
    
    var data : NSMutableData = NSMutableData()
    
    let urlPath: String = "http://52.192.140.108/union/server.php" //this will be changed to the path where service.php lives
    
    
    func downloadItems() {
        
        let url: NSURL = NSURL(string: urlPath)!
        var session: NSURLSession!
        let configuration = NSURLSessionConfiguration.defaultSessionConfiguration()
        
        
        session = NSURLSession(configuration: configuration, delegate: self, delegateQueue: nil)
        
        let task = session.dataTaskWithURL(url)
        
        task.resume()
        
    }
    
    func URLSession(session: NSURLSession, dataTask: NSURLSessionDataTask, didReceiveData data: NSData) {
        self.data.appendData(data);
        
    }
    
    func URLSession(session: NSURLSession, task: NSURLSessionTask, didCompleteWithError error: NSError?) {
        if error != nil {
            print("Failed to download data")
        }else {
            print("Data downloaded")
            self.parseJSON()
        }
        
    }
    
    func parseJSON() {
        
        var jsonResult: NSMutableArray = NSMutableArray()
        
        do{
            jsonResult = try NSJSONSerialization.JSONObjectWithData(self.data, options:NSJSONReadingOptions.AllowFragments) as! NSMutableArray
            
        } catch let error as NSError {
            print(error)
            
        }
        
        var jsonElement: NSDictionary = NSDictionary()
        let currencylist: NSMutableArray = NSMutableArray()
        
        //for(var i = 0; i < jsonResult.count; i++){
        for i in 0...4 {
            
            jsonElement = jsonResult[i] as! NSDictionary
            
            let local = localmodel()
            
            //the following insures none of the JsonElement values are nil through optional binding
            if  let date = jsonElement["date"] as? String,
                let base = jsonElement["base"] as? String,
                let tran = jsonElement["tran"] as? String,
                let curr = jsonElement["curr"] as? NSNumber
            {
                
                local.date = date
                local.base = base
                local.tran = tran
                local.curr = curr
                
            }
            
            currencylist.addObject(local)
            
            
        }
        
        dispatch_async(dispatch_get_main_queue(), { () -> Void in
            
            self.delegate.itemsDownloaded(currencylist)
            
        })
    }
}



