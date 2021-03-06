#!/usr/bin/env python3
#  Copyright 2016 Google Inc. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS-IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from fruit_test_common import *

def test_simple():
    expect_success(
    '''
struct X {
};

X x;

fruit::Component<> getComponent() {
  return fruit::createComponent()
    .addInstanceMultibinding(x);
}

int main() {

  Injector<> injector(getComponent());

  std::vector<X*> multibindings = injector.getMultibindings<X>();
  Assert(multibindings.size() == 1);
  Assert(multibindings[0] == &x);

  return 0;
}
''')

def test_with_annotation():
    expect_success(
    '''
struct Annotation {};

struct X {
};

using XAnnot = fruit::Annotated<Annotation, X>;

X x;

fruit::Component<> getComponent() {
  return fruit::createComponent()
    .addInstanceMultibinding<XAnnot>(x);
}

int main() {

  Injector<> injector(getComponent());

  std::vector<X*> multibindings = injector.getMultibindings<XAnnot>();
  Assert(multibindings.size() == 1);
  Assert(multibindings[0] == &x);

  return 0;
}
''')

def test_instance_vector():
    expect_success(
    '''
struct X {
};

std::vector<X> values = {X(), X()};

fruit::Component<> getComponent() {
  return fruit::createComponent()
    .addInstanceMultibindings(values);
}

int main() {

  Injector<> injector(getComponent());

  std::vector<X*> multibindings = injector.getMultibindings<X>();
  Assert(multibindings.size() == 2);
  Assert(multibindings[0] == &(values[0]));
  Assert(multibindings[1] == &(values[1]));

  return 0;
}
'''
)

def test_instance_vector_with_annotation():
    expect_success(
    '''
struct Annotation {};

struct X {
};

using XAnnot = fruit::Annotated<Annotation, X>;

std::vector<X> values = {X(), X()};

fruit::Component<> getComponent() {
  return fruit::createComponent()
    .addInstanceMultibindings<XAnnot>(values);
}

int main() {

  Injector<> injector(getComponent());

  std::vector<X*> multibindings = injector.getMultibindings<XAnnot>();
  Assert(multibindings.size() == 2);
  Assert(multibindings[0] == &(values[0]));
  Assert(multibindings[1] == &(values[1]));

  return 0;
}
''')

if __name__ == '__main__':
    import nose2
    nose2.main()
