//
//  jasontest.m
//  unionpay
//
//  Created by Jerome Cao on 3/07/16.
//  Copyright © 2016 Jerome Cao. All rights reserved.
//

#import <Foundation/Foundation.h>

NSString *url_string = [NSString tringWithFormat:@"http://xaomng.com/high.json"];
NSData *data = [NSData dataWithContentsOfURL: [NSURL URLWithString:url_string]];
NSMutableArray *json = [NSJSONSerialization JSONObjectWithData:data options: kNilOptions error:&error];
NSLog(@"json: %@", json);

